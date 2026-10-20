# sqldelight schema version must change for migrations

Date: 2026-06-18 21:46

---

`AndroidSqliteDriver` compares the stored database version with `Schema.version` when opening the database. If a new `.sq` file adds a table but the schema version stays the same, the driver skips both `create` and `migrate`; existing installs keep the old tables and queries fail with “no such table”.

Fix options:

1. **Proper migration:** bump the schema version and add a `.sqm` migration:

```sql
-- 1.sqm
CREATE TABLE IF NOT EXISTS savings_goals (...);
```

2. **Idempotent bootstrap:** call `Schema.create(driver)` after creating the driver:

```kotlin
val driver = AndroidSqliteDriver(MoolDatabase.Schema, context, "mool.db")
MoolDatabase.Schema.create(driver)
```

Option 2 only works if every `CREATE` uses `IF NOT EXISTS`; it does not replace versioned migrations for columns, indexes, or data changes. The same version check applies to `NativeSqliteDriver` on iOS.
