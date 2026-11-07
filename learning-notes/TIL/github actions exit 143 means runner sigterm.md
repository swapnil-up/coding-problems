# GitHub Actions exit code 143 means the runner got SIGTERM (often OOM)

Date: 2026-11-05

---

A job that dies in well under the timeout, with **no Python traceback**, and this
tail is almost always the runner being killed — not your code raising:

```text
##[error]The runner has received a shutdown signal.
##[error]Process completed with exit code 143.
```

Read the exit codes:

| Code | Meaning |
|---|---|
| **143** | `128 + 15` → process received **SIGTERM** (the runner supervisor shutting the job down) |
| **137** | `128 + 9` → **SIGKILL / OOM-killer** |
| 124 | timeout |

"No traceback + died in ~1 min" excludes a normal exception and excludes the
`timeout-minutes` limit. The usual cause is **memory**: a `ubuntu-latest` runner
for a public repo is ~4 vCPU / **16 GB**, shared with the OS, pip cache, and any
model caches restored earlier. Blow through it and the supervisor SIGTERMs you.

Debugging checklist:
- Confirm all failing runs share the *same step and same input document*.
- Strace the exit code (`143`) rather than looking for an exception.
- Reproduce the exact path locally under a memory cap:
  `systemd-run --user --scope -p MemoryMax=14G -- ...`
- Compare a passing run's peak usage to a failing one.

In this case the culprit was `pdf2image.convert_from_path` rasterising a
328-page PDF into 12.7 GB of page images — killed on the first OCR page.
