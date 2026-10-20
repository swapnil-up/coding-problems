# debug whisper transcript truncation

Date: 2026-04-18 10:38

---

When a transcription script sometimes cuts off, don't assume audio length. Save the full transcript before handing it to the clipboard or a notification, then log lengths at each step:

```bash
printf '%s' "$text" > /tmp/whisper_last.txt
printf 'chars=%s\n' "${#text}" >> /tmp/whisper_debug.log
xclip -selection clipboard <<<"$text"
notify-send -t 0 "whisper" "${text:0:200}"
```

Check `/tmp/whisper_last.txt`: if it is complete, the loss is in `xclip`/`notify-send` (notification daemons truncate long bodies); if it is short, the loss is upstream. Also export `DISPLAY` explicitly when launched from a keybind or launcher, and pass `-t 0` to `notify-send` so long text doesn't expire.
