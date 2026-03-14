# Problem 05 — Layout Load Functions

## What you'll learn
- `+layout.server.ts` — running `load` at the layout level
- How layout data flows down to all child pages
- Combining layout data + page data

## Context
Many apps need data that's shared across many pages — think "current user", "unread count", "feature flags".
You don't want to repeat that fetch in every `+page.server.ts`.
Layout load functions solve this.

## What you're building
A simple app shell with:
- A layout that loads the "current user" once
- Multiple child pages that each load their own data
- The user shown in the nav across all pages

## Tasks

### 1. Create `src/routes/app/+layout.server.ts`
Write a `load` function that returns a fake current user:
```ts
return {
  user: { name: 'Alice', email: 'alice@example.com', role: 'admin' }
};
```
(In a real app you'd read this from a session cookie)

### 2. Create `src/routes/app/+layout.svelte`
- Get `data` and `children` from `$props()`
- Show a header with the user's name and email (from `data.user`)
- Render `{@render children()}`

### 3. Fix `src/routes/app/feed/+page.server.ts`
It has a TODO — return some fake feed items.

### 4. Fix `src/routes/app/feed/+page.svelte`
Show the feed items AND confirm the user is available via `data.user`
(hint: layout data merges into page data automatically)

### 5. Fix `src/routes/app/notifications/+page.svelte`
Show a list of fake notifications. Access `data.user.name` to personalize the heading.

## Run it
```bash
npm install && npm run dev
```
Visit /app/feed and /app/notifications — the header shows the same user on both.

## Key insight
Layout `load` data is **merged** into the page's `data` prop automatically.
Child pages get BOTH their own load data AND all parent layout load data.
