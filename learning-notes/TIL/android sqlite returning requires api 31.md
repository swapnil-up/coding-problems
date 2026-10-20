# android sqlite returning requires api 31

Date: 2026-06-05 22:43

---

SQLite `INSERT ... RETURNING` was added in SQLite 3.35.0 (March 2021). Android only ships that version from **API 31**, so it is not safe with `minSdk 26`.

For lower API levels, use a transaction and `lastInsertId()`:

```kotlin
var id = 0L
queries.transaction {
    queries.insert(...)
    id = queries.lastInsertId().executeAsOne()
}
```

The transaction makes the insert and ID lookup atomic. SQLDelight 2.3.2 does not expose `transactionWithReturn` on `Transactable`, despite some documentation suggesting it exists.

Keep this pattern until the minimum SDK is raised to 31. Test on an API 26–30 emulator, not just the latest device.
