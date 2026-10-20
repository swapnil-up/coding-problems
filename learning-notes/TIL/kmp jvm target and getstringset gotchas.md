# kmp jvm target and getstringset gotchas

Date: 2026-06-09 23:13

---

Two failures when moving code into `commonMain`:

1. **JVM target mismatch.** If the root/convention plugin builds with JVM 17 and a module builds with JVM 11, inline functions fail:

```
Cannot inline bytecode built with JVM target 17 into bytecode that is being built with JVM target 11
```

Align every module: `compilerOptions { jvmTarget = JvmTarget.JVM_11 }` (or all 17) and matching `sourceCompatibility`/`targetCompatibility`.

2. **`getStringSet`/`putStringSet` are Android-only.** `SharedPreferences` is not in common code. Store a delimited string (`joinToString(",")`) or move the API behind `expect/actual`. `getString`/`putString` alone won't cover sets.

A convention plugin can also conflict with the Compose plugin in non-Compose modules; if a module fails with `MissingMethodException`, don't apply the shared convention plugin there.
