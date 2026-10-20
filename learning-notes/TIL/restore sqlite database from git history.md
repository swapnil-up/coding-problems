# restore sqlite database from git history

Date: 2026-10-06 12:03

---

If a tracked SQLite file is empty in the working tree and at `HEAD`, the data may still exist in an older commit. Find the newest commit that actually has rows:

```bash
git log --oneline -- database/database.sqlite
git show 173dc61:database/database.sqlite > /tmp/restored.sqlite

sqlite3 /tmp/restored.sqlite 'PRAGMA integrity_check;'
sqlite3 /tmp/restored.sqlite 'select count(*) from posts;'
```

Only copy it over the live file after the integrity check and a row-count sanity check:

```bash
cp database/database.sqlite /tmp/database.sqlite.empty.bak
cp /tmp/restored.sqlite database/database.sqlite
```

`git log -- database.sqlite` is the important step: `HEAD` being empty does not mean the file was never populated. Pick the most recent commit with the expected tables and row counts, then compare its schema with the current migrations before using it.
