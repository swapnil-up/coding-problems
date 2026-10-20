# capture value before clearing it in delayed callback

Date: 2026-04-17 06:11

---

A delayed callback that reads reactive state after the state has been reset receives `null`:

```ts
function closeGame() {
  gameType.value = null
  setTimeout(() => playGame(gameType.value), 300) // null
}
```

Capture the value before clearing it:

```ts
function closeGame() {
  const nextType = gameType.value
  gameType.value = null
  setTimeout(() => playGame(nextType), 300)
}
```

The template then sees a valid game type on the next open. This pattern applies to any “close then reopen” transition: modal IDs, selected rows, form drafts, and router params.

If the callback should observe the latest state instead, pass a getter or read from the source of truth inside the callback, but do not assume a mutable ref still holds the pre-reset value.
