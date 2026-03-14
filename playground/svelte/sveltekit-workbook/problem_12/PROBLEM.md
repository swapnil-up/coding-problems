# Problem 12 — Redirects

## What you'll learn
- `redirect(status, location)` from `@sveltejs/kit`
- Redirecting in `load` functions (protect routes)
- Redirecting after form actions
- `redirect` vs `error` — when to use each

## Context
`redirect()` is thrown (like `error()`) and tells SvelteKit to send the browser elsewhere.
Common uses: auth guards, post-submission redirects, legacy URL migrations.

## Tasks

### 1. Protect `/dashboard` (`src/routes/dashboard/+page.server.ts`)
- Check `session.isLoggedIn()`
- If NOT logged in: `throw redirect(303, '/login?from=/dashboard')`
- If logged in: return `{ username: 'Alice' }`

### 2. Fix login page action (`src/routes/login/+page.server.ts`)
The action reads `password` from the form. Complete it:
- If password is `'sveltekit'`, call `session.login()` and redirect to `url.searchParams.get('from') ?? '/dashboard'`
- If wrong password, return `fail(401, { error: 'Wrong password' })`

### 3. Fix the login page (`src/routes/login/+page.svelte`)
- Show the redirect source if `page.url.searchParams.get('from')` exists: "You need to log in to access {from}"
- Show error message if `form?.error` exists
- Add `use:enhance` to the form

### 4. Fix legacy redirect (`src/routes/old-page/+page.server.ts`)
This old URL should permanently redirect to `/dashboard`.
Use a 301 redirect.

## Run it
```bash
npm install && npm run dev
```
Try visiting /dashboard directly — should redirect to login.
Login with password "sveltekit" — should redirect back to /dashboard.

## Key insight
303 = "See Other" — used after POST actions to redirect to a GET page.
301 = Permanent redirect — for legacy URLs/SEO.
