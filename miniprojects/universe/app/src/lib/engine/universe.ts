import type { Cell, World, WorldSettings } from './data';
import { DEFAULT_SETTINGS, GRID_SIZE, INITIAL_SEEKERS, INITIAL_PLANTS } from './data';
export { GRID_SIZE } from './data';
import { wrapCoordinate, getNeighbors, findCellAt, applyEntropy } from './physics';

function seededRandom(seed: number): () => number {
	return function () {
		seed = (seed * 1103515245 + 12345) & 0x7fffffff;
		return seed / 0x7fffffff;
	};
}

export function createInitialWorld(
	width: number = GRID_SIZE,
	height: number = GRID_SIZE,
	settings: WorldSettings = DEFAULT_SETTINGS,
	seed: number = 12345
): World {
	const cells: Cell[] = [];
	let id = 0;
	const random = seededRandom(seed);

	for (let i = 0; i < INITIAL_SEEKERS; i++) {
		cells.push({
			id: id++,
			type: 'SEEKER',
			energy: 50 + Math.floor(random() * 30),
			x: Math.floor(random() * width),
			y: Math.floor(random() * height),
			metadata: { age: 0 }
		});
	}

	for (let i = 0; i < INITIAL_PLANTS; i++) {
		cells.push({
			id: id++,
			type: 'PLANT',
			energy: 40 + Math.floor(random() * 40),
			x: Math.floor(random() * width),
			y: Math.floor(random() * height),
			metadata: { age: 0 }
		});
	}

	return { tick: 0, width, height, cells, settings };
}

export function nextTick(
	world: World,
	randomDir: () => { x: number; y: number }
): World {
	const posMap = new Map<string, Cell>();
	for (const c of world.cells) {
		posMap.set(`${c.x},${c.y}`, c);
	}

	const deadIds = new Set<number>();
	const survivors: Cell[] = [];

	for (const cell of world.cells) {
		if (cell.energy <= 0) {
			deadIds.add(cell.id);
			continue;
		}

		let current = cell;

		// Seekers eat plants
		if (cell.type === 'SEEKER') {
			const neighbors = getNeighbors(cell.x, cell.y, world.width, world.height);
			for (const n of neighbors) {
				const neighbor = findCellAt(world.cells, n.x, n.y);
				if (neighbor && neighbor.type === 'PLANT' && !deadIds.has(neighbor.id)) {
					current = { ...current, energy: Math.min(100, current.energy + 20) };
					deadIds.add(neighbor.id);
					break;
				}
			}
		}

		// Move
		if (current.type === 'SEEKER') {
			const dir = randomDir();
			const newX = wrapCoordinate(current.x + dir.x, world.width);
			const newY = wrapCoordinate(current.y + dir.y, world.height);
			if (!posMap.has(`${newX},${newY}`) || posMap.get(`${newX},${newY}`)?.id === current.id) {
				current = { ...current, x: newX, y: newY };
			}
		}

		// Entropy - use physics calculation
		current = applyEntropy(current, world.settings);

		if (current.energy > 0) {
			survivors.push(current);
		} else {
			deadIds.add(current.id);
		}
	}

	return {
		tick: world.tick + 1,
		width: world.width,
		height: world.height,
		cells: survivors,
		settings: world.settings
	};
}