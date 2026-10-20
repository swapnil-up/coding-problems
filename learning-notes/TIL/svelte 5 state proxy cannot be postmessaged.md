# svelte 5 state proxy cannot be postmessaged

Date: 2026-06-03 19:49

---

Svelte 5 wraps `$state` objects in a deep `Proxy` for reactivity. `postMessage` uses the structured clone algorithm, which cannot clone proxies:

```text
Uncaught DOMException: Proxy object could not be cloned.
```

Take a plain snapshot at the worker boundary:

```ts
const plainWorld = $state.snapshot(world)
worker.postMessage({ type: "tick", world: plainWorld })
```

or clone a derived plain object:

```ts
const plainWorld = structuredClone($state.snapshot(world))
```

Store plain objects inside the simulation, and only wrap them in `$state` at the UI layer. `structuredClone(world)` directly on the proxy may still fail; snapshot first. The same rule applies to IndexedDB writes and other structured-clone APIs.
