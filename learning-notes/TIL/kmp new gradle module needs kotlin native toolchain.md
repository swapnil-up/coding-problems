# A new KMP Gradle module triggers an uncached Kotlin/Native toolchain download

Date: 2026-11-03

---

Adding a fresh module to a Kotlin Multiplatform project can fail an **offline**
build for a surprising reason: the new module brings its own Kotlin/Native
target compilation, which wants a **Kotlin/Native prebuilt toolchain** that isn't
cached yet. `./gradlew --offline ...` then can't download it and fails.

Options:

1. **Avoid the new module.** Put the code into an existing module that already
   compiles native. In this case a `MutableClock` test helper was going to get
   its own `core:test-utils`, but it was moved into `core:platform` instead — same
   dedup, no new toolchain.
2. **Point Gradle at the cached toolchain** with
   `-Pkotlin.native.home`:

```bash
./gradlew --offline --no-daemon --no-configuration-cache \
  -Pkotlin.native.home="$HOME/.konan/kotlin-native-prebuilt-linux-x86_64-2.4.0" \
  :core:platform:check
```

Inspect what's available:

```bash
ls ~/.konan
find ~/.gradle/caches -iname '*kotlin-native-prebuilt*'
```

Takeaway: in constrained/offline environments, "just add a module" has a hidden
cost for KMP — reuse an existing module unless you can fetch the native toolchain.
