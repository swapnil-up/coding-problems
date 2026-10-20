# gnome text scaling factor

Date: 2026-08-18 05:24

---

To fit more on screen in GNOME, lower the text scaling factor (1.0 = normal):

```
gsettings get org.gnome.desktop.interface text-scaling-factor
gsettings set org.gnome.desktop.interface text-scaling-factor 0.9
```

0.9 makes the UI ~10% smaller. Useful range is roughly 0.8–1.1. Some open apps
need a restart to pick up the change.

`scaling-factor` (integer) is the display/DPI scale and only really supports
1 or 2; use `text-scaling-factor` for fine-grained shrinking.
