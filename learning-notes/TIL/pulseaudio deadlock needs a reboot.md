# pulseaudio deadlock needs a reboot

Date: 2026-10-08 06:26

---

After a stream was removed, `pulsemixer` crashed and all audio stopped.
`systemctl restart pulseaudio` / `pulseaudio -k` did not help.

Diagnose:

```
pactl info                      # connection refused / EAGAIN
ps -eLo pid,tid,stat,comm | grep -i pulse
sudo cat /proc/<pid>/task/<tid>/stack
sudo lsof /dev/snd/*
```

The PulseAudio ALSA sink thread was wedged inside the kernel, so it survived
SIGKILL, stayed a zombie, and kept `/dev/snd/pcmC0D0p` busy with `EBUSY`.
Userspace cannot recover a thread stuck in the kernel — only a reboot frees it:

```
sudo reboot
```

A kernel-wedged process is also why the pidfile and D-Bus name linger; deleting
them does not release the device.
