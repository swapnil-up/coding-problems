# pillow fit text into rectangle

Date: 2026-07-10 15:15

---

To fit text into a fixed rectangle, measure each candidate font size with `textbbox` rather than guessing from character count:

```python
from PIL import ImageFont

def fits(draw, text, font_path, size, max_w, max_h):
    font = ImageFont.truetype(font_path, size)
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    return right - left <= max_w and bottom - top <= max_h

best = 0
for size in range(80, 15, -1):
    if fits(draw, text, font_path, size, max_w, max_h):
        best = size
        break
```

A one-line fit at 16px may be technically valid but unreadable. Add a minimum readable size, then try splitting into two lines:

```python
if best < 35:
    # split on a word boundary, try two-line sizes from 80 down
    ...
```

Use the actual font file, not Pillow's default font. Account for the bbox's nonzero top/left when centering, and test the longest name in the dataset, not an average one.
