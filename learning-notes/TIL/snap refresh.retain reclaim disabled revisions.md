# Reclaim disk from disabled snap revisions with refresh.retain

Date: 2026-10-23

---

Snap keeps the **previous revision** of every installed snap around as a
fallback, and on a machine with many snaps those disabled revisions add up to a
couple of GB.

List them and see the total:

```bash
snap list --all            # the second-to-last column shows disabled/previous revisions
```

Keep only the most recent revision going forward (default is 3, minimum is 2),
then prune:

```bash
sudo snap set system refresh.retain=2
sudo snap refresh          # drops old disabled revisions on refresh
```

To remove disabled revisions immediately without waiting for a refresh, delete
them by revision:

```bash
snap list --all | awk '/disabled/{print $1, $3}' | while read name rev; do
  sudo snap remove "$name" --revision="$rev"
done
```

Related space hogs found at the same time: `~/.gradle/caches` (~9 GB, including
old Kotlin/Gradle versions), the Android SDK + AVD snapshots, and `/var` logs.
