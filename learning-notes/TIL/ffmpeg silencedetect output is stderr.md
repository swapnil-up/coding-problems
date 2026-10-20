# ffmpeg silencedetect output is stderr

Date: 2026-08-06 23:33

---

`silencedetect` writes its events to stderr, not stdout:

```bash
ffmpeg -i input.mp4 -af silencedetect=noise=-30dB:d=0.5 -f null - 2> silence.log
```

The relevant lines look like:

```text
[silencedetect @ ...] silence_start: 1.23
[silencedetect @ ...] silence_end: 3.45 | silence_duration: 2.22
```

Parse stderr, not the normal media output:

```python
def parse_silencedetect(stderr):
    intervals, start = [], None
    for line in stderr.splitlines():
        if "silence_start:" in line:
            start = float(line.split("silence_start:")[1].split()[0])
        elif "silence_end:" in line and start is not None:
            end = float(line.split("silence_end:")[1].split()[0])
            intervals.append((start, end))
            start = None
    return intervals
```

Keep the parser pure so it can be tested with a captured log. Validate that cuts stay inside the media duration and that intervals are sorted before generating trim markers.
