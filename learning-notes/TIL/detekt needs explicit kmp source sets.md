# detekt needs explicit kmp source sets

Date: 2026-06-12 19:59

---

Declaring Detekt in the version catalog is not enough; it must be applied and configured. For KMP, Detekt 1.23.7 doesn't understand Kotlin source sets, so point it at each one explicitly:

```kotlin
subprojects {
    apply(plugin = "io.gitlab.arturbosch.detekt")
    configure<DetektExtension> {
        source.setFrom(files(
            "src/commonMain/kotlin",
            "src/androidMain/kotlin",
            "src/iosMain/kotlin",
        ))
    }
}
```

Skip empty modules (e.g. `:app:ios`) or Detekt fails with "no source files". Disable KMP-incompatible rules in `detekt.yml`: `MatchingDeclarationName` (because of `.android.kt`/`.ios.kt`) and `ForbiddenComment` if TODOs are allowed. Add a CI `lint` job running `./gradlew detekt` in parallel with tests/build. Without the plugin applied, `./gradlew detekt` fails even though the version is in the catalog.
