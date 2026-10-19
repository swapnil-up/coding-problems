# i3 power button shutdown

Date: 2026-09-08 21:43

---

Power button does nothing because `systemd-logind` isn't configured to handle it.
Enable it:

```
echo "HandlePowerKey=poweroff" | sudo tee -a /etc/systemd/logind.conf
sudo systemctl restart systemd-logind
```

If i3 intercepts the key first, add a binding in `~/.config/i3/config`:

```
bindsym XF86PowerOff exec systemctl poweroff
```

then reload i3 with `$mod+Shift+r`.

System mode (power/logout controls) is opened with `$mod+Shift+BackSpace`.
