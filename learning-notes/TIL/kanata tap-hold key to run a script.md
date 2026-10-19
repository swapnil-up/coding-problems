# kanata tap-hold key to run a script

Date: 2026-06-27 10:12

---

Using a key as both a modifier (hold) and a script trigger (tap) with kanata.

In `kanata.kbd`, make the mod key a `tap-hold` that sends an unused F-key on a
quick tap and the real modifier on a hold. Example — the physical Win/Alt key
becomes "tap = F23, hold = Super (`$mod`)":

```
lmet (tap-hold $tap-time $hold-time f23 lmet)
```

Then catch that F-key in i3:

```
bindsym F23 exec --no-startup-id ~/github/scripts/scripts/utils/whisper-toggle.sh
```

Quick tap (<150ms) → runs the script; hold (>200ms) → normal `$mod` behaviour.

If `F23` collides with something, `XF86AudioMicMute` is a semantically-nice
alternative (already a known keysym) or any other F13–F23.

The concrete use here is the whisper tap-to-talk toggle — see the
`whisper toggle - pid file and sigusr1` note.
