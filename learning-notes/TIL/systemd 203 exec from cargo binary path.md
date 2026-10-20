# systemd 203 exec from cargo binary path

Date: 2026-07-08 05:23

---

`status=203/EXEC` means systemd could not execute the binary in `ExecStart`. Here the service expected `~/.local/bin/kanata`, but cargo had installed it at `~/.cargo/bin/kanata`.

Find the real path and make the unit point at it:

```bash
command -v kanata
readlink -f "$(command -v kanata)"
systemctl --user cat kanata.service
```

Either use the absolute cargo path in `ExecStart`, or create a stable symlink:

```bash
ln -s ~/.cargo/bin/kanata ~/.local/bin/kanata
systemctl --user daemon-reload
systemctl --user restart kanata.service
```

Also check flags when a service suddenly fails after an upgrade: `--no-wait` had been renamed to `-n`, so the old unit exited during argument parsing. `systemctl --user status` plus the unit's `ExecStart` is usually enough to distinguish a missing binary from a bad flag.
