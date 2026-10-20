# r8 minify a kmp android release build

Date: 2026-06-11 22:30

---

Enabling R8 cut a debug APK from 15 MB to a 2.8 MB release APK (~5x):

```kotlin
buildTypes {
    getByName("release") {
        isMinifyEnabled = true
        proguardFiles(
            getDefaultProguardFile("proguard-android-optimize.txt"),
            "proguard-rules.pro",
        )
    }
}
```

Keep rules needed by the app: Android entry points, kotlinx.serialization serializers/Companion, SQLDelight generated classes, Koin-DSL-constructed classes, expect/actual implementations, Koin annotations, and `@Composable` methods. `-keepattributes *Annotation*` and `RuntimeVisibleAnnotations` are required for reflection/serialization.

R8 warnings about Kotlin metadata (newer Kotlin than R8's parser) are non-fatal if the build succeeds; don't disable minification just to silence them. Always run unit tests and install the release build; missing keep rules usually appear at runtime, not compile time.
