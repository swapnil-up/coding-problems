# Personal Scratchpad

A place to practice, learn, and figure things out. Not a portfolio.

---

## Directories

| Folder | What it's for |
|--------|-------------|
| `leetcode/` | LeetCode problems |
| `HackerRank/` | HackerRank warmups |
| `CodeWarsSolutions/` | CodeWars katas |
| `learning-notes/` | TILs, course notes, random learnings |
| `workbooks/` | Drills and practice sets |
| `miniprojects/` | Small projects for understanding concepts |

---

## Current State

| Section | Count |
|---------|-------|
| LeetCode | 15 |
| HackerRank | 23 |
| CodeWars | ~ |
| TILs | 12 |
| Workbooks | 2 |
| Mini-projects | 3 |

### Recent Activity
<!-- Auto-updated by .githooks/pre-commit -->

---

## Setup

Git hook runs on commit to remind you to update the state above.

**To disable:**
```bash
git config core.hooksPath .git/hooks
```

---

## Philosophy

This repo tracks that I'm still learning, even when nothing gets committed. It's messy, unfinished, and that's the point.

---

## Git Subtree Workflow

Some `miniprojects/` were built as standalone repos outside this monorepo; they use `git subtree` to keep history intact.

**Who:** Me, hacking in a standalone scratch repo on disk.

**What:** Merge standalone repo commits into a subdirectory here — no submodules, no symlinks, no URLs pushed to GitHub.

**When:** After changes in the standalone repo are committed.

**Where:** `dump/<name>/` → `miniprojects/<name>/`.

**Why:** Keep the sandbox private (full config, personal data, failed experiments) while the monorepo stays clean.

**How:**

```bash
# First time (already done for bookmarks-sorter):
git subtree add --prefix=miniprojects/<name> /path/to/standalone/repo master

# Each subsequent round — hack, commit in standalone, then here:
git subtree pull --prefix=miniprojects/<name> /path/to/standalone/repo master
```

**⚠ Caution:** `subtree pull` assumes the standalone repo's history is **append-only**. Rebasing, force-pushing, or squashing commits there will create merge conflicts. Treat the standalone repo as linear — new commits on top, never rewrite.