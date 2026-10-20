# compile sdk 35 with agp 8.2

Date: 2026-05-24 12:25

---

An older project can compile against Android 15 without upgrading AGP, but set all three consistently:

```kotlin
android {
    compileSdk = 35
    defaultConfig { targetSdk = 35 }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions { jvmTarget = "17" }
}
```

AGP 8.2.1 warns that compileSdk 35 is untested but auto-installs platform 35 and builds. Silence it with `android.suppressUnsupportedCompileSdk=35` in `gradle.properties` if needed. Run tests and check for `@Deprecated` warnings from the newer compiler.
