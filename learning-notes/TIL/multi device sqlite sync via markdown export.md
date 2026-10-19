# multi device sqlite sync via markdown export

Date: 2026-07-17 11:20

---

`posts/` (Laravel / Artisan) — SQLite is a single binary file that doesn't merge
in git, so syncing DB state across devices is painful. The pattern that works:
**keep markdown as the source of truth**, use the DB only for local dev.

Round-trip:

```
Write .md on Device A
  → php artisan posts:import     → DB (local dev)
  → php artisan posts:export     → .md files (reconstructed YAML frontmatter)
    → git commit/push → pull on Device B
      → php artisan posts:import → DB on Device B
```

`posts:export` writes each row back to its stored `source_path` (or `--dir`),
and because `posts:import` is idempotent, re-importing exported files is clean.
`posts/` is gitignored; only the `.md` files are tracked.

Rule: if state must travel between machines, serialize it to a **diffable text
format** — don't try to sync the binary DB.
