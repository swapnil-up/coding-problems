# gh auth refresh adds OAuth scopes to an existing login

Date: 2026-10-30

---

When a `gh` command fails because the token is missing a scope (e.g. deleting a
repo needs `delete_repo`), you don't have to log out — refresh the existing
login with the scope(s) you need:

```bash
gh auth refresh -h github.com -s delete_repo
```

- Repeat `-s` for multiple scopes: `-s delete_repo -s workflow`.
- `gh auth refresh` re-runs the OAuth device/browser flow but keeps you logged in
  with the added scopes.
- Check what you currently have with `gh auth status`.

Handy pairing: list your repos with `gh repo list` and remove with
`gh repo delete <owner>/<repo> --yes` once `delete_repo` is granted.
