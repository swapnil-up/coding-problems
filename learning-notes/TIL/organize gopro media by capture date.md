# organize gopro media by capture date

Date: 2026-08-18 14:51

---

`scripts/editor/gopro-organize.sh` — sorts a flat GoPro folder into
`photos/YYYY-MM-DD/` and `video/YYYY-MM-DD/`, renaming each file
`YYYY-MM-DD_HHMMSS_goproNNNN.ext`, then deletes `.THM` thumbnails.

Capture timestamp sources (in order, with mtime fallback):

- **video (MP4)** — `ffprobe`:
  ```
  ffprobe -v error -show_entries format_tags=creation_time \
      -of default=nk=1:nw=1 "$file" | head -n1
  ```
  gives e.g. `2024-06-17T10:55:42.000000Z`.
- **photo (JPG)** — EXIF `DateTimeOriginal` via Python/PIL:
  ```python
  from PIL import Image
  from PIL.ExifTags import TAGS
  exif = Image.open(path)._getexif()
  dt = next(v for k, v in exif.items() if TAGS.get(k) == "DateTimeOriginal")
  # '2024:06:17 10:55:42'
  ```
- **fallback** — `date -r "$file" +%Y-%m-%d_%H%M%S` (file mtime).

Notes: GoPro timestamps are usually in **UTC** unless the camera's clock was
set to local, so a date can shift near midnight. One shoot date per folder falls
out naturally because the capture date is what's grouped on. The script is
idempotent (safe to re-run on a new batch).
