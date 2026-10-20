# pdftoppm tesseract python-docx for editable scans

Date: 2026-06-10 22:35

---

For a short scanned PDF that needs editing, rasterize, OCR, then rebuild a DOCX:

```bash
pdftoppm -png -r 300 input.pdf page
for f in page-*.png; do
  tesseract "$f" "${f%.png}" -l eng
done
```

Then assemble the text with `python-docx`:

```python
from docx import Document

doc = Document()
for path in sorted(Path(".").glob("page-*.txt")):
    for line in path.read_text().splitlines():
        if line.strip():
            doc.add_paragraph(line)
doc.save("edited.docx")
```

300 DPI is a good default for body text. Check `pdftoppm -v` and `tesseract --list-langs` first; missing language data silently produces poor OCR.

OCR is not a layout-preserving conversion. For tables or forms, extract coordinates or rebuild the structure manually. Always proofread names, numbers, and dates against the original scan.
