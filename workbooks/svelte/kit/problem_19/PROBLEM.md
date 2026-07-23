# Problem 19 — Streaming Load Data

## What you'll learn
- Returning a Promise from `load` to stream data
- `{#await}` in pages to handle streamed data
- The difference between blocking and non-blocking load data
- Practical use case: fast initial paint with slow data

## Context
If your `load` function fetches data that takes 2+ seconds, users see a blank page.
SvelteKit lets you return Promises from `load` — the page renders immediately with
the fast data, while slow data streams in later.

## What you're building
A reports page that:
- Shows the page header INSTANTLY
- Shows "quick stats" after ~200ms (fast data)
- Shows "full report" after ~2 seconds (slow data) — streamed in

## Tasks

### 1. Fix `src/routes/reports/+page.server.ts`
Return an object where some values are Promises:
```ts
return {
  quickStats: await fetchQuickStats(),  // awaited = blocks, renders fast
  fullReport: fetchFullReport(),         // NOT awaited = streams in
};
```
The `fetchQuickStats` and `fetchFullReport` helpers are already written.

### 2. Fix `src/routes/reports/+page.svelte`
- The `quickStats` is available immediately (it was awaited in load)
- The `fullReport` is a Promise — use `{#await data.fullReport}` to handle it:
  - Pending: show a loading skeleton
  - Resolved: show the report
  - Rejected: show an error

## Run it
```bash
npm install && npm run dev
```
Watch the page — it should appear instantly with quick stats, then the full
report should fade in ~2 seconds later.

## Key insight
This pattern is called "deferred loading" or "streaming".
It's perfect for dashboards where some data is fast (counts) and some is slow (reports).
In production with SSR, this actually streams HTML chunks to the browser.
