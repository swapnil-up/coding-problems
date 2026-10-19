# translation overlay - per line ocr colors

Date: 2026-06-28 11:04

---

`translation/` OCR pipeline — `pdf_to_text.py` renders per-line translated blocks
over the scanned page. Default colours (cyan `.np` / gold `.en` on
`rgba(0,0,0,0.5)`) had poor contrast on white PDFs.

Final scheme (apply in **both** copies of `pdf_to_text.py`):

| Element | Colour |
|---------|--------|
| `.np` (Devanagari) | `#00eeff` — brighter neon cyan |
| `.en` (translation) | `#88ddff` — light blue, complements the neon |
| block background | `rgba(0,0,0,0.7)` — more opaque so the neon pops on white |

Remember the same styling lives in the backend copy of the script — grep for the
hex values, don't assume one file.
