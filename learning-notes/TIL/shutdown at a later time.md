# shutdown at a later time

Date: 2026-09-09 07:32

---

```bash
sudo shutdown -h +20    # power off in 20 minutes
sudo shutdown -h 23:30  # at a specific time
sudo shutdown -c        # cancel a pending shutdown
```

`-h` halts/powers off; `-r` reboots. The `+N` form is minutes from now. The command schedules a systemd shutdown timer, so the shell can exit immediately.
