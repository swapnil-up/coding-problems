# xinput disable touchpad

Date: 2026-04-18 06:11

---
First find out the list of inputs:
xinput list 

Then disable with the id or name
xinput disable [touchpad_device_id]
xinput disable [touchpad_device_name]

If it works manually but not from an i3 `exec`, it's a race — the `exec` fires
before the device is registered in X. Delay it until the device exists:
```
exec --no-startup-id bash -c 'sleep 1; xinput disable "ELAN07E9:00 04F3:32F4 Touchpad"'
```
