# PyMuPDF's "table version" message is its own one-time ad

Date: 2026-10-28

---

If you see a notification saying the PyMuPDF **table version** produces much
better results, it is **not an error** and not from your code. PyMuPDF prints it
once, on the first `page.find_tables()` call, when the optional
`pymupdf_layout` package isn't installed — `pymupdf/__init__.py:_warn_layout_once`.

It looks like a repo notification because it shows up at runtime, but it's
PyMuPDF advertising its own optional layout analyzer.

Two environments here behaved differently:

- The project **venv** had `pymupdf 2.0` + `pymupdf-layout 2.0`, so `find_tables()`
  already used the improved path (hence no message).
- **System Python** had `pymupdf 1.27.2.3` without `pymupdf.layout`, so scripts run
  outside the venv still saw the message.

Silence it any of these ways:

```bash
export PYMUPDF_SUGGEST_LAYOUT_ANALYZER=0     # env var
```

```python
import pymupdf
pymupdf.no_recommend_layout()                # or just run inside .venv
```

If table extraction quality actually matters, install the analyzer:
`pip install pymupdf-layout`.
