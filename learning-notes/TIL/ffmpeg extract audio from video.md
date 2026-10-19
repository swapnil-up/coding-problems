# ffmpeg extract audio from video

Date: 2026-06-27 21:34

---

Pull the audio track out of a video file, keeping the original quality:

```
ffmpeg -i input.mp4 -q:a 0 -map a output.mp3
```

- `-map a` selects only audio streams
- `-q:a 0` is the best VBR quality for the target codec

For a copy with no re-encode (when the container is compatible):

```
ffmpeg -i input.mp4 -vn -acodec copy output.m4a
```
