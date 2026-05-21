# Bookmark Sorter

Classify your Firefox bookmark export into topic-based folders with Firefox `TAGS` attributes.

## Quick start

1. Export your Firefox bookmarks to HTML (`Ctrl+Shift+O` → Import and Backup → Export Bookmarks to HTML) and save as `bookmarks.html` in this directory.

2. Copy the example config and customize it:
   ```
   cp bookmarks_config.example.py bookmarks_config.py
   ```
   Edit `bookmarks_config.py` to add the domains, keywords, and topics that match your interests.

3. Run:
   ```
   python3 organize_bookmarks.py
   ```

4. Import the output back into Firefox:
   - `Ctrl+Shift+O` → Import and Backup → Import Bookmarks from HTML
   - Pick `bookmarks-organized.html`

## Output

| File | Description |
|------|-------------|
| `bookmarks-organized.html` | All topics as folders, import-ready |
| `bookmarks-{topic}.html` | Individual per-topic files |

Every bookmark gets a `TAGS="topic1,topic2"` attribute so Firefox preserves cross-topic relationships.

## How it works

- **Domain matching** — known domains (e.g., `github.com`) map directly to topics
- **Folder hinting** — bookmarks inside folders with keywords (e.g., "programming") inherit that topic
- **Keyword tagging** — title keywords add secondary tags without changing the primary folder

## Files committed to git

Only these files are tracked:

- `organize_bookmarks.py` — the engine
- `bookmarks_config.example.py` — dummy example config
- `.gitignore` — keeps your private data out
- `README.md` — this file

Everything else (`bookmarks.html`, `bookmarks_config.py`, all `bookmarks-*.html` output) is gitignored.
