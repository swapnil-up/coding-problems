# cid font unicode comes from per page tounicode maps

Date: 2026-06-02 08:06

---

For a Type0/CIDFontType2 PDF, glyph identity is CID, not Unicode. The embedded TTF's `cmap` can parse but contain no Devanagari mappings; the PDF's `ToUnicode` CMap is the only reliable CID→Unicode source.

- Each font instance on each page has its own ToUnicode stream.
- Those CMaps are subsets: they only map CIDs that appear on that page, so the same CID can map differently or be missing elsewhere.
- Extract every ToUnicode CMap across pages, merge them, and handle conflicts; then decode CIDs.
- Unmapped CIDs become control characters (`\x04`, `\x0e`) in extracted text. Treat them as unknown, not as text.

With PyMuPDF (`fitz`), walk `page.get_fonts(full=True)` → xref → `doc.xref_stream(xref)` for the ToUnicode stream. Don't rely on the embedded TTF cmap.
