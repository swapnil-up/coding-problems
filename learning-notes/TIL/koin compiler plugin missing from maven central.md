# koin compiler plugin missing from maven central

Date: 2026-06-12 08:09

---

The Koin compiler plugin version needed for Kotlin 2.4 / Koin 4.2 (1.0.0/1.0.1) may not be published to Maven Central yet. A local `publishToMavenLocal()` makes the app build, but CI starts from a clean `~/.m2` and fails to resolve the plugin.

Workaround in CI before the Gradle build:

```bash
git clone https://github.com/InsertKoinIO/koin-compiler-plugin.git /tmp/koin-plugin
cd /tmp/koin-plugin
JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 ./gradlew publishToMavenLocal
```

Then add `mavenLocal()` to `pluginManagement` and `dependencyResolutionManagement` repositories. The plugin build needs JDK 17+, even if the app uses JDK 21. Remove the clone/publish step once the artifact is on Maven Central; `~/.m2` is not cached by `gradle/actions/setup-gradle` by default.
