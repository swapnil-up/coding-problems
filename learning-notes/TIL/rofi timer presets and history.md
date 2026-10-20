# rofi timer presets and history

Date: 2026-09-28 09:54

---

The timer menu reads presets from `~/.config/timers/presets`, one `name|duration` per line:

```
gtg|60m
deep work|25m
```

Duration accepts `1h`, `20m`, `90s`; a bare number means minutes. Entries appear as `Set: <name>` and start in one click.

Run history comes from `~/.local/state/timer-daemon.log` (`start` events written by `timer-daemon`). The menu reads it newest-first; `View History` offers today or last 100.

If presets don't appear, the package isn't stowed:

```bash
stow -R -t ~ -d config timer
```

Check `bash -n scripts/rofi/rofi-timer-menu.sh` after edits.
