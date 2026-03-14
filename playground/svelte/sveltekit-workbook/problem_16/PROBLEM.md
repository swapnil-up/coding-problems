# Problem 16 — invalidate() and Data Freshness

## What you'll learn
- `invalidate(url)` — re-run specific load functions without a full navigation
- `invalidateAll()` — re-run all load functions on the current page
- Custom dependency keys with `depends()`
- When to use invalidate vs full navigation

## Context
After a mutation (form action, API call), you often need to refresh the page data.
`invalidate()` triggers a re-run of any `load` function that `fetch`ed the given URL
or called `depends()` with that key.

## What you're building
A live stats dashboard that:
1. Shows server stats (fake data that changes on each fetch)
2. Has a "Refresh" button that re-fetches without navigation
3. Auto-refreshes every 5 seconds

## Tasks

### 1. Fix `src/routes/api/stats/+server.ts`
Return fake changing stats: `{ timestamp, visitors, revenue, requests }` with slight randomness.

### 2. Fix `src/routes/+page.server.ts`
The load function should:
- Call `depends('app:stats')` — register a custom dependency key
- Fetch `/api/stats` using the SvelteKit `fetch`
- Return the stats data

### 3. Fix `src/routes/+page.svelte`
- Import `invalidate` from `$app/navigation`
- Add a "Refresh" button that calls `invalidate('app:stats')`
- Set up a `$effect` that calls `invalidate('app:stats')` every 5 seconds (clear on cleanup)
- Show the stats and the timestamp so you can see it updating

## Run it
```bash
npm install && npm run dev
```
Watch the timestamp update when you click Refresh or wait 5 seconds.

## Key insight
`invalidate('app:stats')` re-runs ONLY load functions that called `depends('app:stats')`.
This is more surgical than `invalidateAll()` which re-runs everything.
