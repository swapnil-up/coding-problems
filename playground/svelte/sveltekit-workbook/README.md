# SvelteKit Workbook

20 hands-on problems covering SvelteKit from basics to prod-ready patterns.
Each problem is a **self-contained SvelteKit app** — run it, break it, fix it.

## Prerequisites
- Completed Basic Svelte (you have)
- Node.js 18+

## Structure

Each problem folder is a standalone SvelteKit project:
```
problem_01/
  src/
    routes/
      +page.svelte        ← edit this
      +page.server.ts     ← and/or this
  PROBLEM.md              ← read this first
  SOLUTION_HINTS.md       ← peek if stuck
```

## How to run a problem

```bash
cd problem_05
npm install   # first time only
npm run dev   # visit http://localhost:5173
```

## How to check your work

Most problems have a checklist in PROBLEM.md.
Some have a `npm run check` script for type checking.
The real test: does it work in the browser as described?

---

## Problem List

| # | Topic | Key concepts |
|---|-------|-------------|
| 01 | Your first page | `+page.svelte`, file-based routing |
| 02 | Route params | `[slug]`, `params` in load |
| 03 | Layouts | `+layout.svelte`, shared UI |
| 04 | Page load data | `+page.server.ts` `load()`, `data` prop |
| 05 | Layout load | `+layout.server.ts`, inherited data |
| 06 | Default form action | `<form>`, `actions`, `use:enhance` |
| 07 | Named form actions | Multiple actions on one page |
| 08 | Form validation & fail | `fail()`, `form` prop, error display |
| 09 | API route GET | `+server.ts`, `json()` |
| 10 | API route POST | Request body, returning responses |
| 11 | Error pages | `error()`, `+error.svelte` |
| 12 | Redirects | `redirect()` in load and actions |
| 13 | The handle hook | `hooks.server.ts`, `event.locals` |
| 14 | Auth pattern | Protecting routes via `locals` + hook |
| 15 | $page state | `$app/state`, current URL, params |
| 16 | invalidate() | Client-side data refresh without reload |
| 17 | Page options | `prerender`, `ssr`, `csr` |
| 18 | Environment vars | `$env/static/private`, `$env/dynamic/public` |
| 19 | Streaming with await | `defer`, streaming `load()` data |
| 20 | Final: Mini blog | Routing + load + forms + hooks + API |

---

## Tips

- Each problem has **broken or incomplete code** — your job is to fill the TODOs
- Read `PROBLEM.md` fully before touching code
- SvelteKit reloads on save — keep `npm run dev` running in a terminal
- TypeScript errors are hints — fix them, don't suppress them
- Check the Network tab in DevTools to see server requests / form POSTs
