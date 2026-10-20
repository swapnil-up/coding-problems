# sqldelight needs a databases block

Date: 2026-06-11 21:29

---

SQLDelight generates database code from `.sq` files only when a database is declared in Gradle:

```kotlin
sqldelight {
    databases {
        create("MoolDatabase") {
            packageName.set("com.mool.core.database")
        }
    }
}
```

Without the `databases { }` block, the plugin may warn but still build, while no `MoolDatabase` class or query classes are generated. Imports then fail or the app keeps using an older generated API.

After adding the block:

```bash
./gradlew :core:database:generateCommonMainMoolDatabaseInterface
./gradlew :core:database:build
```

Check that generated sources exist under `build/generated/sqldelight/`. If `.sq` files exist but no generated code does, inspect the module's `build.gradle.kts` for the missing block before changing schemas or dependencies.
