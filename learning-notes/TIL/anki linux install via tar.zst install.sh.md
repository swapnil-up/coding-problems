# Anki's Linux install is now a .tar.zst + install.sh

Date: 2026-10-27

---

Anki no longer ships the old-style Linux package for a plain `apt`/manual copy.
The current release is a **`.tar.zst`** bundle containing an `install.sh` that
installs into `/usr/local/share/anki` (launcher at `/usr/local/bin/anki`).

From scratch:

```bash
curl -L -o /tmp/anki.tar.zst \
  https://github.com/ankitects/anki/releases/download/26.09.3/anki-26.09.3-linux-x86_64.tar.zst
mkdir -p /tmp/anki
tar --use-compress-program=unzstd -xf /tmp/anki.tar.zst -C /tmp/anki
sudo /tmp/anki/anki-26.9.3-linux-x86_64.tar/install.sh
```

If you've already extracted it, the one-liner is just:

```bash
sudo /tmp/anki-new/anki-26.9.3-linux-x86_64.tar/install.sh
```

Notes:

- `tar` needs `unzstd` (`sudo apt install zstd`) for `.tar.zst`.
- `install.sh` **removes the old install** automatically and leaves your
  collection at `~/.local/share/Anki2` untouched.
- It creates the `.desktop` file and pixmap too — verify with
  `anki --version`.
- Grab the current asset URL from
  `https://api.github.com/repos/ankitects/anki/releases/latest`.
