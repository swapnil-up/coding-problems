# github actions token cannot push gh-pages

Date: 2026-06-23 21:12

---

`peaceiris/actions-gh-pages@v4` failed with:

```
remote: Permission to <user>/<repo>.git denied to github-actions[bot].
```

The default `GITHUB_TOKEN` is read-only unless the repo allows it to write.

Fix (no code change): repo **Settings → Actions → General → Workflow
permissions → Read and write permissions**.

Alternatives: use a PAT with `repo` scope and pass it as `personal_token`, or an
SSH deploy key via `deploy_key`. The settings toggle is usually enough.
