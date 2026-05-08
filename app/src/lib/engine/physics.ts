import type { Cell, CellType, World } from './data';

export function wrapCoordinate(value: number, max: number): number {
	((value % max) + max) % max;
	return ((value % max) + max) % max;
}

export function getNeighbors(x: number, y: number, width: number, height: number): Array<{ x: number; y: number }> {
	const directions = [
		{ x: -1, y: -1 }, { x: 0, y: -1 }, { x: 1, y: -1 },
		{ x: -1, y: 0 },                 { x: 1, y: 0 },
		{ x: -1, y: 1 },  { x: 0, y: 1 },  { x: 1, y: 1 }
	];

	return directions.map(d => ({
		x: wrapCoordinate(x + d.x, width),
		y: wrapCoordinate(y + d.y, height)
	}));
}

export function findCellAt(cells: readonly Cell[], x: number, y: number): Cell | undefined {
	return cells.find(c => c.x === x && c.y === y);
}

export function findEmptyNeighbors(
	cells: readonly Cell[],
	x: number,
	y: number,
	width: number,
	height: number
): Array<{ x: number; y: number }> {
	const neighbors = getNeighbors(x, y, width, height);
	return neighbors.filter(n => !findCellAt(cells, n.x, n.y));
}

export function applyEntropy(cell: Cell, settings: World['settings']): Cell {
	const baseRate = cell.type === 'SEEKER' ? settings.entropyRateSeeker : settings.entropyRatePlant;
	const decay = Math.max(1, Math.floor(cell.energy * (baseRate / 100)));
	return { ...cell, energy: Math.max(0, cell.energy - decay) };
}

export function applyMoveCost(cell: Cell, moved: boolean, settings: World['settings']): Cell {
	if (!moved) return cell;
	return { ...cell, energy: Math.max(0, cell.energy - settings.moveCost) };
}

export function checkFeeding(
	seeker: Cell,
	cells: readonly Cell[],
	settings: World['settings']
): { newSeeker: Cell; plantToDust: number[] } | null {
	const neighbors = getNeighbors(seeker.x, seeker.y, 100, 100);
	const plant = cells.find(c => c.type === 'PLANT' && neighbors.some(n => n.x === c.x && n.y === c.y));

	if (!plant) return null;

	const newSeeker: Cell = {
		...seeker,
		energy: Math.min(100, seeker.energy + settings.eatGain)
	};

	return { newSeeker, plantToDust: [plant.id] };
}

export function checkReproduction(
	cell: Cell,
	cells: readonly Cell[],
	settings: World['settings']
): Cell | null {
	if (cell.type !== 'PLANT') return null;
	if (cell.energy < settings.reproductionThreshold) return null;

	const emptySpots = findEmptyNeighbors(cells, cell.x, cell.y, 100, 100);
	if (emptySpots.length === 0) return null;

	return {
		...cell,
		energy: cell.energy - settings.reproductionCost
	};
}

export function computeNewPosition(
	cell: Cell,
	cells: readonly Cell[],
	settings: World['settings'],
	randomDir: { x: number; y: number }
): { newCell: Cell; moved: boolean } {
	if (cell.type === 'PLANT') {
		return { newCell: cell, moved: false };
	}

	const neighbors = getNeighbors(cell.x, cell.y, 100, 100);
	const plantNeighbor = cells.find(c => c.type === 'PLANT' && neighbors.some(n => n.x === c.x && n.y === c.y));

	let targetDir: { x: number; y: number } | null = null;

	if (plantNeighbor) {
		targetDir = {
			x: Math.sign(plantNeighbor.x - cell.x),
			y: Math.sign(plantNeighbor.y - cell.y)
		};
	}

	const finalDir = targetDir ?? randomDir;
	const newX = wrapCoordinate(cell.x + finalDir.x, 100);
	const newY = wrapCoordinate(cell.y + finalDir.y, 100);

	const occupied = cells.some(c => c.x === newX && c.y === newY && c.id !== cell.id);
	if (occupied) {
		return { newCell: cell, moved: false };
	}

	const newCell: Cell = {
		...cell,
		x: newX,
		y: newY,
		metadata: {
			...cell.metadata,
			lastDirection: finalDir,
			age: cell.metadata.age + 1
		}
	};

	return { newCell: newCell, moved: true };
}