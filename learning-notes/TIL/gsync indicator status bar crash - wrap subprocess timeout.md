# gsync indicator status bar crash - wrap subprocess timeout

Date: 2026-07-20 16:51

---

`scripts/` — the i3 status bar showed **"process exited unexpectedly"** and stuck.

Cause: the status wrapper calls `gsync-indicator` via
`subprocess.run(..., timeout=10)` with **no try/except**. If the indicator hangs
past 10s (stuck on a bad repo), `TimeoutExpired` propagates and kills the whole
wrapper — i3status then dies.

Fix: wrap the call and degrade gracefully:

```python
try:
    result = subprocess.run([...], timeout=10, capture_output=True, text=True)
    # use result
except (subprocess.TimeoutExpired, Exception):
    # keep the bar alive; send a notify instead of crashing
```

Lesson: any subprocess a long-lived wrapper depends on needs a timeout **and**
exception handling — a status bar must never take down the process.
