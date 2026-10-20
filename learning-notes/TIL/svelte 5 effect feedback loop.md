# svelte 5 effect feedback loop

Date: 2026-06-04 06:41

---

An `$effect` that calls a parent callback which updates state read by the same effect can loop until Svelte throws a depth error:

```ts
$effect(() => {
  onrender(performance.now() - startedAt) // parent updates renderTimes
})
```

The parent re-render invalidates the effect, which calls `onrender` again.

Break the synchronous cycle by deferring the write to the next frame:

```ts
$effect(() => {
  const elapsed = performance.now() - startedAt
  requestAnimationFrame(() => onrender(elapsed))
})
```

Alternatively, keep the metric in a non-reactive variable, or use `untrack` around the write. The key is that the effect must not synchronously update state that it also reads. The deferred value is still accurate because `elapsed` is captured before scheduling.
