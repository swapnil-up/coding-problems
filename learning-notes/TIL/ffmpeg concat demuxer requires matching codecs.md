# ffmpeg concat demuxer requires matching codecs

Date: 2026-05-23 11:49

---

The concat demuxer is the fast path for joining clips without re-encoding:

```bash
printf "file '%s'\n" clip1.mp4 clip2.mp4 > list.txt
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4
```

It only works reliably when every input has the same codecs, resolution, pixel format, timebase, and audio parameters. Mixing phone clips, screen recordings, and edited exports often produces corrupted timestamps, missing audio, or a file that stops after the first clip.

When parameters differ, use the concat filter and re-encode:

```bash
ffmpeg -i clip1.mp4 -i clip2.mp4 \
  -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 23 -c:a aac output.mp4
```

Probe first (`ffprobe -show_streams`) and fall back to re-encoding instead of assuming `-c copy` will work.
