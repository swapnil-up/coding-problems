# laptop mic grainy audio fix - alsa double gain

Date: 2026-10-19 19:02

---

Grainy / distorted / "robot" laptop mic is usually **hard clipping** from double
gain staging on the internal mic. On this laptop (Realtek ALC236, card 1) both
`Capture` and `Internal Mic Boost` were at 100%:

- `Capture` 100% = **+30 dB**
- `Internal Mic Boost` 100% = **+30 dB**
- total **+60 dB** → the ADC clips before anything downstream can fix it

Confirm it with a recording + `volumedetect` (`max_volume: 0.0 dB` and lots of
`histogram_0db` = clipped):

```
arecord -c 2 -r 48000 -f S16_LE -d 3 /tmp/mic_test.wav
ffmpeg -hide_banner -i /tmp/mic_test.wav -af volumedetect -f null - 2>&1 | grep -E 'mean_volume|max_volume|histogram_0db'
```

Fix it by removing the boost and lowering capture gain:

```
amixer -c 1 sset 'Internal Mic Boost' 0
amixer -c 1 sset 'Capture' 40
```

Afterwards the same recording sat around `max -13.7 dB` — clean headroom, no
clipping. Note that software (PipeWire) volume **cannot** un-clip a signal that
already clipped at the ADC, so the hardware gain is what matters.

Persist across reboots:

```
sudo alsactl store
```

Check the saved state took effect (values should read `0`, not `3`):

```
grep -A3 'Internal Mic Boost Volume' /var/lib/alsa/asound.state
```
