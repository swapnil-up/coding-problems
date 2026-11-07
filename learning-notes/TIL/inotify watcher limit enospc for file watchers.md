# ENOSPC "file watchers reached" is inotify, not disk

Date: 2026-11-07

---

A Node dev server (Vite / TinaCMS) crashes at startup with:

```text
Error: ENOSPC: System limit for number of file watchers reached, watch '.../tina'
    at FSWatcher.<computed> (node:internal/fs/watchers:323:19)
```

Despite `ENOSPC` ("no space"), this has **nothing to do with disk**. It means the
per-user **inotify watch** quota is exhausted. On a default Ubuntu box
`fs.inotify.max_user_watches` is **65536**, and a big editor can eat almost all
of it: VS Code was holding ~65k watches by itself, leaving nothing for the dev
server.

Check the limit and who is holding watches:

```bash
cat /proc/sys/fs/inotify/max_user_watches /proc/sys/fs/inotify/max_user_instances

# per-process inotify watch counts
for pid in $(ls /proc | grep -E '^[0-9]+$'); do
  c=0
  for f in /proc/$pid/fdinfo/*; do
    grep -qs '^inotify' "$f" 2>/dev/null && c=$((c + $(grep -c '^inotify wd:' "$f")))
  done
  [ "$c" -gt 0 ] && echo "$c $(cat /proc/$pid/comm 2>/dev/null)"
done | sort -rn | head
```

Raise the limits (persist across reboots):

```bash
sudo sysctl -w fs.inotify.max_user_watches=524288 fs.inotify.max_user_instances=1024
echo "fs.inotify.max_user_watches=524288" | sudo tee /etc/sysctl.d/60-inotify.conf
```

You can also just watch less — e.g. TinaCMS has `tinacms dev --noWatch`.
