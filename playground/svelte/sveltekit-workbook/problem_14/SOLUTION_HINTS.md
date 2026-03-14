## Hints

- Route group `(protected)` is a folder name — it does NOT appear in URLs
- Layout `load` in a route group applies to all pages in that group
- `cookies.set(name, value, { path: '/' })` — `path` is required
- `cookies.delete(name, { path: '/' })` — `path` must match what was set
- `locals.user` flows from hook → layout load → page load → page component
