# i3lock time based colors

Date: 2026-07-17 23:14

---

`i3lock` (v2.x) only supports `-c <color>` / `-i <image>` — no time-based colour.
To stop getting flashbanged by a white screen at night, wrap it: a script picks
a colour from the hour and calls `i3lock -c "$color"`.

`scripts/i3lock-wrapper`:

```bash
#!/usr/bin/env bash

HOUR=$(date +%H)

if [ "$HOUR" -ge 6 ] && [ "$HOUR" -lt 12 ]; then
    COLOR="#87CEEB"
elif [ "$HOUR" -ge 12 ] && [ "$HOUR" -lt 17 ]; then
    COLOR="#F5DEB3"
elif [ "$HOUR" -ge 17 ] && [ "$HOUR" -lt 20 ]; then
    COLOR="#D2691E"
else
    COLOR="#1a1a2e"
fi

exec i3lock -c "$COLOR" "$@"
```

| Time | Colour |
|------|--------|
| 06-11 morning | `#87CEEB` sky blue |
| 12-16 afternoon | `#F5DEB3` warm wheat |
| 17-19 evening | `#D2691E` orange/dusk |
| 20-05 night | `#1a1a2e` dark, saves eyes |

Point the i3 lock binds at the wrapper and stow:

```
stow -R -t ~ -d config i3
```

Call the **wrapper**, not `i3lock` directly — bare `i3lock` still goes white.
Alternative if you want more: the `i3lock-color` fork adds `--clock`, per-element
colours, etc.
