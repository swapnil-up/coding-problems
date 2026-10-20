# svelte worker stale tick race

Date: 2026-06-04 07:02

---

When a worker computes simulation ticks, a reset can happen while an old tick is still in flight. The stale result then overwrites the new world.

Use a generation counter:

```ts
let generation = 0

function reset(world) {
  generation++
  currentWorld = cloneWorld(world)
}

function tick() {
  const gen = generation
  worker.postMessage({ type: "tick", world: currentWorld, generation: gen })
}

worker.onmessage = (event) => {
  if (event.data.generation !== generation) return
  currentWorld = event.data.world
}
```

Increment on reset and on settings changes that invalidate in-flight work, and have the worker echo the generation back. Terminating and recreating the worker also works, but is heavier and loses warm state.

This is the same pattern as request IDs: every async response must carry the epoch it belongs to.
