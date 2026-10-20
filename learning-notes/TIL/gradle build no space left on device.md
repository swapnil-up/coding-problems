# gradle build no space left on device

Date: 2026-06-04 07:16

---

“No space left on device” during an Android build is usually Gradle caches and downloaded distributions, not the project.

Check what is consuming space:

```bash
df -h
du -sh ~/.gradle/caches ~/.gradle/wrapper/dists 2>/dev/null
du -sh .gradle */build 2>/dev/null
```

Clear old caches and wrapper distributions that can be re-downloaded:

```bash
rm -rf ~/.gradle/caches/* ~/.gradle/wrapper/dists/*
./gradlew clean
```

If only the project's build outputs are large, remove `build/` directories instead. After freeing space, rerun the exact failing task and confirm `df -h` before assuming the build is fixed. A build that fails at a different task after cleanup may have been partially written; a clean build is safer than resuming.
