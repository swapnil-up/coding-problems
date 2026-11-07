# playwright video timestamps scrambled on reencode

Date: 2026-11-07 23:43

---

Playwright's `browser.new_context(record_video_dir=...)` writes a WebM whose
frames are in the **correct order** but carry **non-monotonic / scrambled
timestamps**. The recorder duplicates the previous frame `round(fps × Δt)` times
and the rounding accumulates (upstream: microsoft/playwright#35776). Sequential
playback looks fine, which is what makes it sneaky — but every ffmpeg transcode
**reorders frames by those timestamps**, so `-ss` seeks and frame-index
extraction land on the wrong content.

Giveaway symptom: on the transcoded MP4, `ffmpeg -ss 28 -i out.mp4` shows
footage from ~54s, while `select='eq(n,700)'` shows yet another place — index
and time disagree with each other and with the wall clock.

## Fix

Renumber timestamps from decode order so the output stage has nothing to
reorder, and disable B-frame reordering:

```
ffmpeg -i raw.webm -vf "setpts=N/25/TB" -c:v libx264 -x264-params bframes=0 \
  -crf 20 -pix_fmt yuv420p -movflags +faststart -an demo.mp4
```

`setpts=N/25/TB` assigns each frame PTS = `frame_number / 25`, i.e. the storage
order becomes the timeline. `bframes=0` stops libx264 from introducing its own
presentation-vs-decode reordering.

## Verify (mandatory)

Index and seek must agree, and both must match the wall clock:

```
ffmpeg -ss 28 -i demo.mp4 -frames:v 1 /tmp/t28.png
ffmpeg -i demo.mp4 -vf "select='eq(n\,700)'" -vsync 0 -frames:v 1 /tmp/n700.png
```

A 1 fps contact sheet is the fastest full eyeball:

```
ffmpeg -i demo.mp4 -vf "fps=1,scale=240:-1,tile=6x12" -frames:v 1 sheet.png
```

Two traps when verifying: `-ss` placed before `-i` (input seek) is unreliable on
these files, and **md5 across codecs is meaningless** (VP8 vs H.264 pixels
differ) — compare content visually, not hashes.

Bonus: validate any extraction method against a synthetic clip with burned-in
timestamps (`testsrc2` + `drawtext=text='%{pts\:hms}'`) before trusting it.
