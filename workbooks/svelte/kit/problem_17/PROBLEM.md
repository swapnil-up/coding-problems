# Problem 17 — Page Options (prerender, ssr, csr)

## What you'll learn
- `export const prerender = true` — generate static HTML at build time
- `export const ssr = false` — disable server-side rendering for a page
- `export const csr = false` — disable client-side JavaScript for a page
- When to use each option and why

## Context
SvelteKit is flexible: pages can be server-rendered, statically pre-generated,
or client-side only. You control this per-page or per-layout.

## Tasks

### 1. Prerendered blog (`src/routes/blog/`)
Blog posts are static content — prerender them.

In `src/routes/blog/+page.server.ts`:
- Export `prerender = true`
- Return the posts list

In `src/routes/blog/[slug]/+page.server.ts`:
- Export `prerender = true`
- Export `entries` function that returns all slugs (required for dynamic prerendered routes)
- Return the matching post

### 2. SSR-disabled page (`src/routes/client-only/+page.svelte`)
This page uses browser-only APIs (like `localStorage`).
- Export `ssr = false` from a `<script module>`
- The page shows a counter stored in `localStorage`
- Reads/writes `localStorage` freely since SSR is disabled

### 3. Dashboard (`src/routes/dashboard/+page.server.ts`)
Default behavior (ssr: true, csr: true) — no special options.
Show a note in the UI explaining what the default behavior means.

## Run it
```bash
npm install && npm run dev
```
Note: prerender only fully applies at build time. In dev, all pages are SSR'd.
To see prerender: `npm run build && npm run preview`

## Key insight
- `prerender = true`: HTML generated at build time, served as static files (fastest!)
- `ssr = false`: page only renders in the browser (for browser-API-heavy pages)
- `csr = false`: no JS sent to client (pure HTML, no hydration — for very simple pages)
