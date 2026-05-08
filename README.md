# The Entropy Engine

A functional ecosystem simulation built with *Grokking Simplicity* principles.

## What It Is

A "Digital Aquarium" where you define the laws of nature, not individual behaviors. Cells (Seekers, Plants, Dust) are pushed through pure mathematical rules—entropy decay, eating, reproduction, Brownian motion. Each tick produces a completely new, frozen snapshot of the world.

## The Goal

A visual engine where:
- Plants grow based on energy
- Seekers hunt plants to survive  
- Entropy drains energy from everything
- A "God Mode" dashboard lets you tweak physics in real-time
- Deterministic replayability (same seed = same outcome)

## Tech Stack

- **Svelte 5** — UI framework
- **TypeScript** — Logic (pure calculations)
- **Canvas API** — Rendering

## Architecture (Stratified Design)

| Layer | Responsibility |
| ----- | -------------- |
| **I/O** | Rendering, user controls |
| **Timeline** | History, pause, rewind |
| **Evolution** | Maps rules over entire grid |
| **Rules** | Individual logic (entropy, eating, movement) |
| **Primitives** | Grid math (neighbors, wrapping) |

## Key Principles

1. **Immutability** — Never mutate state. Return new versions.
2. **Pure Functions** — No `Math.random()` or `new Date()` in physics. Pass seeds in.
3. **Separation** — Calculations (logic) separate from Actions (side effects).
4. **Deterministic** — Same seed + same rules = same outcome.

## Core Types

```typescript
type CellType = 'SEEKER' | 'PLANT' | 'DUST';

interface Cell {
  id: number;
  type: CellType;
  energy: number;
  x: number;
  y: number;
  metadata: { lastDirection?: {x, y}, age: number };
}

interface World {
  tick: number;
  cells: Cell[];
  settings: { entropyRate: number };
}
```
