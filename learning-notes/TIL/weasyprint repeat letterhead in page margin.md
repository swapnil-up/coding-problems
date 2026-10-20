# weasyprint repeat letterhead in page margin

Date: 2026-06-12 07:14

---

To repeat a letterhead on every printed page without consuming body space, reserve the margin and place a fixed element into it:

```css
@page {
  margin-top: 2.2in;
}

.letterhead {
  position: fixed;
  top: -2.2in;
  left: 0;
  width: 100%;
}
```

`position: fixed` makes WeasyPrint repeat the element on each page. The negative `top` moves it from the content box into the reserved top margin, so body text starts below it on page one and continues normally on later pages.

The image must be sized for the page width, not the content width, or it will be clipped by the margin. Check a multi-page PDF, not just page one: a correctly placed header should appear at the same y-position on every page.
