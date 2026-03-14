# Problem 06 — Default Form Action

## What you'll learn
- `actions` export in `+page.server.ts`
- The default form action pattern
- `use:enhance` for progressive enhancement (no full-page reload)
- Reading `request.formData()` on the server
- `form` prop — how the server sends data back to the page

## Context
SvelteKit form actions let you handle form submissions entirely on the server,
with no manual API route needed. They work without JavaScript (true progressive enhancement),
and with `use:enhance` they feel like a SPA.

## Tasks

### 1. Fix `src/routes/contact/+page.server.ts`
It exports a broken `actions` object. Complete the `default` action:
- Parse `name` and `email` from the form data
- Return `{ success: true, name }` on success

### 2. Fix `src/routes/contact/+page.svelte`
- Add `use:enhance` to the form (already imported, just add it)
- Show a success message when `form?.success` is true
- Show the submitted name back: "Thanks, {form.name}!"

## The form has these fields (already in the template):
- `name` (text input)
- `email` (email input)
- A submit button

## Run it
```bash
npm install && npm run dev
```
Submit the form with and without JS (disable JS in DevTools to test the progressive enhancement).

## Key insight
`use:enhance` intercepts the form submit and uses `fetch` instead of a full reload.
Without it (or without JS), the form still works — it just does a full page reload.
This is progressive enhancement in action.
