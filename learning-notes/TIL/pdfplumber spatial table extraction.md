# pdfplumber spatial table extraction

Date: 2026-09-30 17:11

---

For tables with no ruling lines (or legacy PDFs where cells collapse), don't split text by whitespace. Extract words with coordinates and assign columns by x-position:

```python
import pdfplumber

with pdfplumber.open(path) as pdf:
    words = pdf.pages[0].extract_words(
        use_text_flow=False,
        keep_blank_chars=False,
    )
```

- Cluster column boundaries from a fully populated row or the header's x positions; numbers are often right-aligned, so cluster by `x1` (right edge), not `x0`.
- Fill missing cells with `0`; PDFs often omit zero cells, so a row with 38 expected columns may yield 7 words.
- Use `y_tolerance` around 5 to merge a name line with the number line when they are vertically offset.
- Devanagari digits work with `int()`; strip commas first. Values like `२०७१/७२` are not numbers (`str.isdigit()` is false) and must not be treated as counts.
- Overlapping text layers on some pages produce merged words; flag those pages instead of trusting the parse.

Validate with row invariants (e.g. male + female = total) before exporting.
