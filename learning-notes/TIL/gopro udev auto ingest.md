# gopro udev auto ingest

Date: 2026-08-06 22:51

---

Automate GoPro SD-card ingest with a udev rule plus a small shell script:

```udev
# /etc/udev/rules.d/99-gopro.rules
ACTION=="add", SUBSYSTEM=="block", ATTRS{idVendor}=="...", \
  RUN+="/home/swap/github/scripts/scripts/editor/gopro-ingest.sh"
```

The ingest script should:

1. Find the mounted `DCIM/100GOPRO` directory.
2. Copy `.MP4`/`.JPG` files into `~/vedit/raw`.
3. Rename to a stable timestamped name.
4. Skip files that already exist.

Use `ffprobe -show_entries format_tags=creation_time` first, then fall back to the file mtime:

```bash
ts=$(ffprobe -v error -show_entries format_tags=creation_time \
  -of default=nw=1:nk=1 "$file" 2>/dev/null)
ts=${ts:-$(date -r "$file" +%Y%m%d_%H%M%S)}
dest="$VEDIT_RAW/${ts}_$(basename "$file")"
cp -n "$file" "$dest"
```

Make the script executable, use absolute paths in the udev rule, and test idempotency by running it twice. A `cp` without `-n` or an existence check silently creates duplicates.
