# bluetoothctl disconnect and tray applet

Date: 2026-08-23 13:52

---

Disconnect a Bluetooth device from the CLI:

```
bluetoothctl disconnect
```

For a tray icon with quick connect/disconnect, use Blueman:

```
sudo apt install blueman
blueman-applet &        # start the tray applet
```

To keep it around, autostart `blueman-applet` (i3 `exec --no-startup-id` or an
XDG autostart `.desktop`).
