# AGENTS.md

## Warning

⚠️ **Don't traverse `playground/*/node_modules/`** - it's 170+ levels deep and will crash tools. Use `--depth 1` or glob patterns only.

## Repo Purpose

This is a personal scratchpad. It's messy and that's okay. The goal is to show I'm still learning, even when not adding to a repo.

## Interaction

### Updates
- Use `repo-status` skill for README/TIL index updates
- Key: `./skills/repo-status.md` or load the skill

### TIL Index
1. Read `learning-notes/TIL/*.md`
2. Group by category: Git, CLI/System, Media, Development
3. Update `learning-notes/TIL/README.md`

### Quick Counts
```bash
find leetcode -name "*.py" | wc -l
find learning-notes/TIL -name "*.md" | wc -l
```