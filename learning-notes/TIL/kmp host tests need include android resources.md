# kmp host tests need include android resources

Date: 2026-06-06 06:34

---

Android host tests in a KMP `androidLibrary` module do not get Android resources by default. Tests that touch resources, `ApplicationProvider`, or resource-backed Compose code fail unless resources are explicitly enabled:

```kotlin
androidLibrary {
    withHostTest {
        isIncludeAndroidResources = true
    }
}
```

Then run the host test task:

```bash
./gradlew :shared:testAndroidHostTest
```

`testAndroidHostTest` is the correct task for `androidHostTest` sources; `allTests` may not include it depending on the KMP/AGP setup.

Enable this only for host tests that need resources. If a pure JVM test fails with `AndroidManifest.xml` or `Resources$NotFoundException`, check this flag before moving the test to `androidUnitTest`.
