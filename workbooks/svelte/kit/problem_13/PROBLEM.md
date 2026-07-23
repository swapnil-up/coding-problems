# Problem 13 — The Handle Hook

## What you'll learn
- `hooks.server.ts` — where server-side hooks live
- The `handle` hook — runs on EVERY request
- `event.locals` — request-scoped data store
- `sequence()` — composing multiple handle hooks

## Context
The `handle` hook is middleware for SvelteKit. It intercepts every request before
any `load` function or action runs. You use it for:
- Logging
- Setting request-scoped data (e.g. current user from a cookie)
- Auth checks
- CORS headers

## Tasks

### 1. Create `src/hooks.server.ts`
Write a `handle` hook that does two things:

**Logging**: Before resolving, `console.log` the method and URL of each request.
After resolving, `console.log` the response status.

**Fake auth**: Check for a cookie named `user`. If it exists, parse it as JSON
and set `event.locals.user = parsedUser`. Otherwise set `event.locals.user = null`.

### 2. Update `src/app.d.ts`
Extend the `App.Locals` interface to include `user: { name: string; role: string } | null`.

### 3. Fix `src/routes/+page.server.ts`
Read `locals.user` and return it as `{ user }`.

### 4. Fix `src/routes/+page.svelte`
Show the user info if logged in, or "Not logged in" if not.
Add buttons to "Set user cookie" and "Clear cookie" that hit the API routes below.

### 5. Fix `src/routes/api/ping/+server.ts`
Just return `json({ message: 'pong', user: event.locals.user })`.

## Run it
```bash
npm install && npm run dev
```
Check the server terminal — you should see log lines for every request.
Use the browser DevTools to manually set a cookie named `user` with value:
`{"name":"Alice","role":"admin"}` — then refresh and see it populate.

## Key insight
`event.locals` is how you pass data from hooks to load functions and actions.
This is the standard pattern for session/auth in SvelteKit.
