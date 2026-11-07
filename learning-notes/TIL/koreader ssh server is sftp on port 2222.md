# koreader ssh server is sftp on port 2222

Date: 2026-11-02 13:55

---

KOReader's network transfer server listens on port `2222` and speaks SSH/SFTP, not FTP. An `ftp://host:2222` URL will fail; use `sftp` or set FileZilla's protocol to **SFTP**.

```bash
sftp -P 2222 root@192.168.1.103
```

```text
get /mnt/us/koreader/settings/statistics.sqlite3
```

On Kindle the KOReader settings folder is `/mnt/us/koreader/settings/`. The reading stats live in `statistics.sqlite3`.

## "Login without password" still prompts

Even when KOReader is set to login without a password, the SSH client still has to send a password. `ssh -o BatchMode=yes` disables password auth entirely, so it fails with:

```text
Permission denied (publickey,password)
```

To supply a password non-interactively, use `SSH_ASKPASS` with `setsid` so OpenSSH has no TTY to prompt on:

```bash
printf '#!/bin/sh\necho root\n' > /tmp/askpass
chmod +x /tmp/askpass

DISPLAY=:0 SSH_ASKPASS=/tmp/askpass SSH_ASKPASS_REQUIRE=force \
  setsid -w sftp -P 2222 root@192.168.1.103 <<'EOF'
get /mnt/us/koreader/settings/statistics.sqlite3 storage/koreader/statistics.sqlite3
bye
EOF
```

Add `-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null` when scripting against a device whose host key changes or should not be persisted.
