# pdf2image convert_from_path rasterises every page at once

Date: 2026-11-05

---

`pdf2image.convert_from_path()` renders **all** pages into an in-memory list of
PIL images and only returns once the whole PDF is done. On a large scanned PDF
that list alone is enormous.

Measured on a real 328-page book (3.9 MB PDF, 300 dpi):

| Path | Peak RSS | Time |
|---|---|---|
| `convert_from_path(pdf, dpi=300)` (all pages) | **12.7 GB** | 69 s |
| Full CI path (rasterise + PaddleOCR engine + page 1) | **>14 GB** | OOM-killed (exit 137) |

The fix is to rasterise in batches with `first_page` / `last_page`, so only a
handful of page images exist at any moment:

```python
from pdf2image import convert_from_path

BATCH = 10

def pdf_to_images(pdf_path, dpi=300):
    # count pages first, then walk the document in fixed-size chunks
    for first in range(1, page_count + 1, BATCH):
        last = min(first + BATCH - 1, page_count)
        for img in convert_from_path(pdf_path, dpi=dpi, first_page=first, last_page=last):
            yield img
```

Same 328-page PDF, 10-page batches: **0.75 GB peak / 32 s** — 16× less memory
*and* faster (fewer oversized PNG buffers to parse).

Rule of thumb: never call `convert_from_path()` without `first_page`/`last_page`
on input you don't control. This matters most in CI, where the runner has a
fixed RAM budget you can blow without any Python traceback.
