# remux iphone mov to mp4

Date: 2026-10-11 15:09

---

iPhone `.MOV` files are usually HEVC + AAC, which MP4 supports, so no re-encode
is needed. Remuxing is instant and lossless:

```
ffmpeg -i input.MOV -map 0:v:0 -map 0:a:0 -c copy -movflags +faststart output.mp4
```

`-map 0:v:0 -map 0:a:0` keeps only the first video and audio stream. That drops
Apple-only tracks such as `apac` spatial audio and `mebx` metadata, which is why
the MP4 can be smaller.

Verify before deleting the original:

```
ffprobe -v error -show_entries format=duration -of default=nw=1 output.mp4
ffmpeg -v error -i output.mp4 -f null -   # full decode check
```
