# calibre add creates duplicates instead of updating

Date: 2026-09-04 10:22

---

`calibredb add book.epub` always adds a new record; it does not match an existing book by title. A small title difference (e.g. an apostrophe) is enough to create a duplicate.

```bash
calibredb list --fields=title
calibredb list --fields=title --search="title:Outsiders"
calibredb add updated.epub
calibredb remove 281 284   # remove old IDs, keep the new one
```

Close the Calibre GUI before batch syncing; an open library can block writes. Verify IDs before removing: lower IDs are usually the old entry, but confirm the title and format first.
