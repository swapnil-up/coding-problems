# systemd user service wantedby target mismatch

Date: 2026-09-02 10:41

---

A systemd **user** service wasn't auto-starting. Two bugs in the unit:

1. `After=graphical-session.target` but `WantedBy=default.target` — the `After=`
   and `WantedBy=` targets must match, otherwise the service is pulled in before
   the graphical session exists and dies. Fix:

```
[Unit]
After=graphical-session.target

[Install]
WantedBy=graphical-session.target
```

2. The enable symlink in `~/.config/systemd/user/` was missing (a failed `stow`
   run had removed it). Recreate it and reload:

```
systemctl --user daemon-reload
systemctl --user enable --now <service>
systemctl --user status <service>
```

Check the effective target and that `After=` / `WantedBy=` agree.
