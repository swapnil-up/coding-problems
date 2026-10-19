# ble.sh bash line editor

Date: 2026-06-16 17:29

---

`ble.sh` gives bash autocompletion + syntax highlighting (replacing what OMZ/zsh
gave). Install:

```
git clone --recursive --depth 1 --shallow-submodules https://github.com/akinomyoga/ble.sh.git
make -C ble.sh install PREFIX=~/.local
```

Enable in `~/.bashrc`:

```
source ~/.local/share/blesh/ble.sh
```

Trick used here: to avoid ble.sh interfering with startup programs that inspect
the terminal, source it **detached** early and attach at the end of `.bashrc`:

```
source ~/.local/share/blesh/ble.sh --attach=none
# ... other shell init ...
ble-attach
```
