# Firefox snap and Firefox Dev Edition don't share a profile

Date: 2026-10-27

---

Firefox (snap) and Firefox Developer Edition keep **separate** profiles, so
removing one does not touch the other's data:

| Install | Profile location |
|---|---|
| Firefox (snap) | `~/snap/firefox/common/.mozilla/firefox` |
| Firefox Dev Edition | `~/.mozilla/firefox` |

Consequence: `snap remove firefox` **deletes** `~/snap/firefox` (which can be
multiple GB and may hold bookmarks/history). Back it up first if you care.

```bash
# check what exists and how big
du -sh ~/snap/firefox ~/.mozilla/firefox 2>/dev/null
ls -d ~/snap/firefox/common/.mozilla/firefox ~/.mozilla/firefox 2>/dev/null

# remove only the snap/apt Firefox, keep Dev Edition
sudo snap remove firefox && sudo apt-get remove -y firefox
```

Also update any launcher/window-manager bindings to point at `firefox-dev` only
(i3, rofi launcher, VS Code), and drop `firefox` from the bootstrap manifest.
