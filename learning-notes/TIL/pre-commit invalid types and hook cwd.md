# pre-commit invalid types and hook cwd

Date: 2026-04-15 19:03

---

Two failures that look unrelated:

1. `types: [typescript]` is invalid. pre-commit's `types` values come from `identify`, which has no `typescript` tag. Use `files` instead:

```yaml
- id: frontend-lint
  files: ^frontend/.*\.(ts|tsx|js|jsx)$
```

2. Local hooks run from the repo root, not the subproject. A hook that runs `ruff` from `backend/.venv` fails with `Failed to spawn: ruff`. Either `cd` or use uv's directory flag:

```yaml
entry: bash -c 'cd backend && uv run ruff check .'
# or
entry: uv run --directory backend ruff check .
```

`dirs:` is not a valid local-hook key; pre-commit warns "Unexpected key(s)".
