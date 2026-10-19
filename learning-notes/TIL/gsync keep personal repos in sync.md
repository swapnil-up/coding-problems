# gsync keep personal repos in sync

Date: 2026-07-17 11:35

---

`scripts/` — `~/.local/bin/gsync` keeps personal repos in sync across two
machines without merge-conflict pain. It:

1. scans every dir in `~/github/`
2. finds repos that have a `swapnil-up` remote
3. `git stash` uncommitted changes
4. `git pull --rebase`
5. `git push`
6. restores the stash

Gotcha when writing it: under `set -e`, `((skip_count++))` returns exit status
**1** when the *pre-increment* value is 0, which kills the script. Use
`((++skip_count))` or append `|| true`.
