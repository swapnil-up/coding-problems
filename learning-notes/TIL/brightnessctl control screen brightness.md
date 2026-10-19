# brightnessctl control screen brightness

Date: 2026-06-16 15:49

---

Change screen brightness from the terminal / i3 keybinds with `brightnessctl`
(installs via `apt install brightnessctl`):

```
brightnessctl set +10%     # up
brightnessctl set 5%-      # down
brightnessctl set 50%      # absolute
```

Needs membership of the `video` group (add with `usermod -aG video $USER`), then
log out/in. Without it, prefix with `sudo`.

i3 example:

```
bindsym XF86MonBrightnessUp exec brightnessctl set +10%
bindsym XF86MonBrightnessDown exec brightnessctl set 10%-
```

Note: the **keyboard** backlight is a separate thing and on this laptop is
firmware-controlled (no sysfs/ACPI interface) — use `Fn+F5` or the BIOS setting.
