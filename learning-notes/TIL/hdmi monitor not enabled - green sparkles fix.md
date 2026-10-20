# hdmi monitor not enabled - green sparkles fix

Date: 2026-10-01 14:33

---

Monitor connected but dark, and `xrandr` shows `HDMI-1 connected` with no active
mode. It isn't an FPS problem — the output was never enabled:

```
xrandr --output HDMI-1 --auto --right-of eDP-1
```

With the output lit, the screen had green sparkles. That was a colour format
issue on the link, not a failing GPU. Force 8-bit colour and full RGB range:

```
xrandr --output HDMI-1 --set "max bpc" 8
xrandr --output HDMI-1 --set "Broadcast RGB" Full
```

Check the current values with:

```
xrandr --props | grep -A3 -E 'max bpc|Broadcast RGB'
```

Both settings reset when the output is re-enabled (replug/resume), so re-apply
them from an autorandr `postswitch` hook or i3 startup script. `autorandr` can
also save the layout per monitor setup.

If the wallpaper looks tiled or split after enabling the screen, the root
pixmap is still sized for the old layout. Re-run `feh --bg-center <image>` after
the layout change.
