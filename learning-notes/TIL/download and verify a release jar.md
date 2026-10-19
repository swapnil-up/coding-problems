# download and verify a release jar

Date: 2026-10-16 22:13

---

Grab a GitHub release asset and check it isn't corrupted:

```
curl -L -O https://github.com/<user>/<repo>/releases/download/<tag>/<file>.jar
sha256sum <file>.jar
# compare against the published SHA-256
```

Example — MegaBasterd 8.61 to `~/Downloads/` (79 MB, hash matched), then run with
the installed JDK:

```
java -jar ~/Downloads/MegaBasterd_8.61.jar
```

`-L` follows redirects (GitHub release URLs redirect to the asset host).
