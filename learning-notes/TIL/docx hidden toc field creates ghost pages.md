# docx hidden toc field creates ghost pages

Date: 2026-09-18 10:41

---

A Word document can contain an automatic table-of-contents field that is hidden in the editor but still renders during PDF export. It may add blank or duplicate “Contents” pages and shift every page number after it.

Check the DOCX XML for a TOC field:

```bash
unzip -p document.docx word/document.xml | grep -o 'TOC [^<]*'
```

Look for `w:fldChar`/`w:instrText` pairs containing `TOC \o` or `TOC \h`. Remove the field and its result, then rebuild the table of contents as normal paragraphs with explicit page numbers.

After removal:

1. Re-export the PDF.
2. Confirm the certificate/declaration page moved back to the intended page.
3. Re-sync all TOC page numbers to the new pagination.

A hidden field can survive editing because it is not visible in the normal view; inspect the XML when PDF pagination does not match the DOCX editor.
