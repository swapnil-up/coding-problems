# typst slash star starts a comment

Date: 2026-05-15 08:09

---

Typst treats `/*` as the start of a block comment, even when it appears in ordinary prose. Writing `Svelte/*FastAPI` can silently comment out the rest of the document.

Escape the asterisk or put spacing around the slash:

```typst
Svelte/\*FastAPI
Svelte / FastAPI
```

Use raw text or a code span when the literal characters matter:

```typst
`Svelte/*FastAPI`
```

If a generated PDF suddenly loses a section, search the source for an unescaped `/*` before debugging layout or pagination.
