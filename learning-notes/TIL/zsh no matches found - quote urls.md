# zsh no matches found - quote urls

Date: 2026-10-04 18:38

---

Running `mpv https://...?v=...` in zsh fails with:

```
zsh: no matches found: https://www.youtube.com/watch?v=...
```

zsh expands glob patterns even when no file matches, and `?` is a
single-character glob. Bash leaves an unmatched pattern alone, which is why the
same command works there.

Two fixes:

```
mpv 'https://www.youtube.com/watch?v=...'   # quote it
```

or disable the failure globally in `~/.zshrc`:

```
setopt NO_NOMATCH
```

Quoting is safer for one-offs; `NO_NOMATCH` is the quality-of-life fix if you
paste URLs into commands often.
