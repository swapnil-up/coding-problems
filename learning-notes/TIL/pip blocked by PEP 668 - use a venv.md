# pip blocked by PEP 668 - use a venv

Date: 2026-08-12 23:31

---

On modern distros a system-wide `pip install` fails with:

```
error: externally-managed-environment
```

(PEP 668 — the Python install is managed by the OS package manager.)

Fixes, best first:

- **venv** (isolated, recommended):
  ```
  python3 -m venv ~/.venvs/whisper
  source ~/.venvs/whisper/bin/activate
  pip install openai-whisper
  ```
- **pipx** for a single CLI app: `pipx install <pkg>`
- **distro package** if one exists.
- `--break-system-packages` works but can clobber system Python deps — last resort.

Whisper note: the `large` model is ~3 GB and slow on CPU; the smaller models
(`base`, `small`) transcribe much faster at some accuracy cost.
