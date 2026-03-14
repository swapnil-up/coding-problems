# Problem 14 — Auth Pattern (Route Groups + Hooks)

## What you'll learn
- Route groups `(name)` — organize routes without affecting URLs
- The canonical auth pattern: hook sets locals, layout guards the group
- Cookies for session storage
- Protecting multiple routes at once via a layout load

## Context
This is the real auth pattern used in production SvelteKit apps.
Instead of checking auth in every `+page.server.ts`, you:
1. Set `locals.user` in the handle hook (from a session cookie)
2. Create a `(protected)` route group with a layout that redirects if no user

## File structure
```
src/
  hooks.server.ts               ← sets locals.user from cookie
  routes/
    login/
      +page.svelte
      +page.server.ts           ← login/logout actions
    (protected)/                ← route group (no URL prefix)
      +layout.server.ts         ← auth guard — redirect if no user
      +layout.svelte            ← shared header for authed pages
      dashboard/
        +page.svelte
      settings/
        +page.svelte
```

## Tasks

### 1. `src/hooks.server.ts`
Read a cookie `session` (JSON: `{ name, role }`), set `event.locals.user`.

### 2. `src/routes/(protected)/+layout.server.ts`
If `!locals.user`, redirect to `/login?from={event.url.pathname}`.
Return `{ user: locals.user }`.

### 3. `src/routes/(protected)/+layout.svelte`
Show the user's name and a logout button in a header.

### 4. `src/routes/login/+page.server.ts`
Two actions:
- `login`: check password === 'admin123', set session cookie, redirect to `from` or `/dashboard`
- `logout`: delete session cookie, redirect to `/login`

### 5. Dashboard and Settings pages
Simple pages — they get user data from the layout automatically.

## Run it
```bash
npm install && npm run dev
```
Visit `/dashboard` without logging in — should redirect to `/login?from=/dashboard`.

## Key insight
Route groups `(name)` affect file organization but NOT the URL.
`/dashboard` still maps to `src/routes/(protected)/dashboard/+page.svelte`.
