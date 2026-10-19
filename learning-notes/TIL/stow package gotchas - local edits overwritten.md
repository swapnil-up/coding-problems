# stow package gotchas - local edits overwritten

Date: 2026-08-29 07:37

---

`scripts/` dotfiles — the timer `presets` file kept losing local edits.

Cause: the stow package symlinks the **whole** `~/.config/timers/` directory to
the repo, so `presets` *is* the repo file. Editing it locally and not committing
means another device (after a pull/re-stow) only sees the committed version.
There is no separate "local" copy.

Rules of thumb:

- Don't let `stow` manage a file you edit locally and expect to persist —
  **commit it**, or keep it out of the package.
- Stow-symlinked dirs also collect **app runtime state** (espanso `state.json`,
  nvim `swap/`/`undodir/`/`shada/`). `.gitignore` those, or they show up as dirty
  changes in the repo.
- Broken symlinks left behind after removing a package file: `stow -R` doesn't
  always clean them; check for dangling links in `~/.config` after removing
  packages.
