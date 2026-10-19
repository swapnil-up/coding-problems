# whisper toggle - pid file and sigusr1

Date: 2026-06-27 10:12

---

`scripts/utils/` — tap-to-talk toggle for the whisper transcription script.

`whisper.sh` was using a fixed temp path, so overlapping runs clobbered each
other. Make it PID-unique:

```
TEMP_AUDIO="/tmp/whisper_audio_$$.wav"    # was /tmp/whisper_audio.wav
```

`whisper-toggle.sh` (new) turns it into a one-key toggle using a PID file at
`/tmp/whisper_toggle.pid`:

- **first press** → start `whisper.sh` in the background, save its PID, notify
  "Listening…"
- **second press** → `SIGUSR1` the PID to stop recording → transcription runs →
  "Copied"
- handle a **stale PID file** gracefully (process no longer alive → treat as idle)

Triggered by a quick tap of the kanata tap-hold key (`f23`) caught in i3 — see
the `kanata tap-hold key to run a script` note.

Apply:

```
stow -R -t ~ -d config kanata
i3-msg reload
```
