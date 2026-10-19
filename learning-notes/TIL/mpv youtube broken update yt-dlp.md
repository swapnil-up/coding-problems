# mpv youtube broken update yt-dlp

Date: 2026-07-17 11:55

---

mpv failing to play YouTube is usually **yt-dlp being too old** for YouTube's
current API, not mpv itself. Check the version:

```
yt-dlp --version
```

If it's months/years old, update it (user-local install is easiest):

```
yt-dlp -U            # or: pipx upgrade yt-dlp / pip install -U yt-dlp
```

mpv may still call a stale copy. Point it explicitly at the updated binary in
`~/.config/mpv/mpv.conf`:

```
ytdl-format=bestvideo+bestaudio/best
script-opts=ytdl_hook-ytdl_path=/home/swap/.local/bin/yt-dlp
```

Test:

```
mpv https://www.youtube.com/watch?v=...
```
