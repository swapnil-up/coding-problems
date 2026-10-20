# vue watch on timer state creates multiple intervals

Date: 2026-04-17 18:50

---

Watching both the running flag and the countdown recreates the interval on every tick:

```ts
// broken
watch([isRunning, timeLeft], () => {
  if (isRunning.value) {
    setInterval(() => timeLeft.value--, 1000)
  }
})
```

Each decrement triggers the watcher again, starting another interval without clearing the previous one. The timer then runs several times per second and gets faster over time.

Watch only the control state and manage one interval:

```ts
let timer: ReturnType<typeof setInterval> | undefined

watch(isRunning, (running) => {
  clearInterval(timer)
  if (running) {
    timer = setInterval(() => timeLeft.value--, 1000)
  }
})

onUnmounted(() => clearInterval(timer))
```

Always clear before assigning and on unmount. If the interval callback must update reactive state that the watcher reads, keep that state out of the watch sources.
