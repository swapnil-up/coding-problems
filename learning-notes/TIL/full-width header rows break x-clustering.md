# full-width header rows break x-clustering

Date: 2026-05-26 21:30

---

When extracting a borderless table by clustering word x-positions, a header row that spans the full page width makes every x-position look like one column. The resulting parse collapses all body rows into a single field.

Filter span rows before computing column boundaries:

```python
page_width = page.width
words = page.extract_words()

header_rows = []
body = []
for row in group_by_y(words, tolerance=5):
    x0 = min(w["x0"] for w in row)
    x1 = max(w["x1"] for w in row)
    if (x1 - x0) > 0.8 * page_width:
        header_rows.append(row)
    else:
        body.append(row)
```

Use the body rows to cluster columns, then apply the resulting boundaries to all rows. Keep the filtered header rows separately if their labels are needed.

Validate the result by checking that each data row has the expected number of cells. A sudden drop to one or two columns on every row usually means a title or spanning header was included in the clustering sample.
