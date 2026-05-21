<script lang="ts">
	import type { World } from '$lib/engine/data';

	interface Props {
		world: World;
		cellSize?: number;
	}

	let { world, cellSize = 20 }: Props = $props();

	let canvas: HTMLCanvasElement;

	const COLORS: Record<string, string> = {
		SEEKER: '#e74c3c',
		PLANT: '#2ecc71',
		DUST: '#95a5a6'
	};

	$effect(() => {
		if (!canvas) return;
		const ctx = canvas.getContext('2d');
		if (!ctx) return;

		ctx.fillStyle = '#1a1a1a';
		ctx.fillRect(0, 0, world.width * cellSize, world.height * cellSize);

		for (const cell of world.cells) {
			const color = COLORS[cell.type] || '#fff';
			const alpha = Math.max(0.3, cell.energy / 100);
			ctx.fillStyle = color;
			ctx.globalAlpha = alpha;
			ctx.fillRect(
				cell.x * cellSize,
				cell.y * cellSize,
				cellSize - 1,
				cellSize - 1
			);
		}
		ctx.globalAlpha = 1;
	});
</script>

<canvas
	bind:this={canvas}
	width={world.width * cellSize}
	height={world.height * cellSize}
	class="simulation-canvas"
></canvas>

<style>
	.simulation-canvas {
		display: block;
		image-rendering: pixelated;
		border: 1px solid #333;
	}
</style>