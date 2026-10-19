# rtv tuir configparser readfp fix

Date: 2026-08-05 12:52

---

`rtv` / `tuir` crashes on modern Python with:

```
ConfigParser readfp error
```

`readfp()` was removed in Python 3.12. The fix already exists upstream as
**MR !15** on `gitlab.com/ajak/tuir` — but the project is effectively dead
(last master commit ~2020), so **don't bother submitting a PR**.

Options:

- Use the distro package — Debian/Ubuntu ship a patched `tuir`:
  ```
  sudo apt install tuir
  ```
- Patch the local pipx install (one-line `sed` fix).
- Fork locally, apply the change, `pipx install .`.
