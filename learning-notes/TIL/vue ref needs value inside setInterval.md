# vue ref needs value inside setInterval

Date: 2026-05-14 07:21

---

A Vue `ref` is an object wrapper. Reading `.length` directly gives `undefined`, and `undefined % 3` is `NaN`, so a carousel index silently stops updating:

```ts
// broken: heroImages is a ref
idx = (idx + 1) % heroImages.length

// fixed
idx = (idx + 1) % heroImages.value.length
```

This is easy to miss inside a `setInterval` callback because there is no exception; the timer keeps firing and the UI simply never changes.

Use `.value` for reads and writes in script code. In templates, Vue unwraps refs automatically, which is why the same expression can work there and fail in a timer. If the value is a computed ref, also check that its dependencies actually change.
