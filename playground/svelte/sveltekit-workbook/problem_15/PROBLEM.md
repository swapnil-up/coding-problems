# Problem 15 — $app/state: page, navigating

## What you'll learn
- `page` from `$app/state` — reactive current page info
- `page.url`, `page.params`, `page.data`, `page.status`
- `navigating` — detecting in-progress navigation
- Building active nav links

## Context
`$app/state` exposes reactive state about the current navigation.
`page` is updated on every client-side navigation automatically.

## Tasks

### 1. Fix `src/routes/+layout.svelte`
Build a nav that highlights the active link:
- Import `page` from `$app/state`
- Use `class:active={page.url.pathname === '/'}` on each link
- Show a "Loading..." spinner using `navigating` from `$app/state`

### 2. Fix `src/routes/+page.svelte`
Show a debug panel:
- Current path: `page.url.pathname`
- Current params: `JSON.stringify(page.params)`
- Page status: `page.status`

### 3. Fix `src/routes/users/[id]/+page.server.ts`
Return `{ user: { id: params.id, name: 'User ' + params.id } }`

### 4. Fix `src/routes/users/[id]/+page.svelte`
Show the user data AND demonstrate that `page.params.id` equals `data.user.id`.

### 5. Add a breadcrumb component `src/lib/Breadcrumb.svelte`
Split `page.url.pathname` by `/` and render breadcrumb links.
e.g. `/users/42` → `Home / users / 42`

## Run it
```bash
npm install && npm run dev
```
Navigate between pages and watch the active link and debug panel update reactively.

## Key insight
`page` from `$app/state` is reactive Svelte 5 state — it updates automatically
on every navigation without any subscriptions or stores needed.
