# Problem 08 — Form Validation & fail()

## What you'll learn
- `fail(status, data)` to return validation errors from an action
- Showing field-level errors in the form
- Preserving form values on failed submission (repopulating fields)
- The `form` prop type — `ActionData`

## Context
`fail()` is SvelteKit's way to return a non-2xx response from a form action
while still sending data back to the page. The page re-renders with `form`
populated with your error data.

## Tasks

### 1. Fix `src/routes/register/+page.server.ts`
The action reads the form data but returns nothing. Add validation:

- `username`: required, min 3 chars, max 20 chars
- `email`: required, must contain `@`
- `password`: required, min 8 chars
- `confirmPassword`: must match `password`

On failure: `return fail(422, { errors, values })` where:
- `errors` is an object with field names as keys and error messages as values
- `values` is the submitted form data (so we can repopulate the form)

On success: `return { success: true, username }`

### 2. Fix `src/routes/register/+page.svelte`
- Show inline error messages under each field using `form?.errors?.fieldName`
- Repopulate field values using `form?.values?.fieldName ?? ''`
- Show a success banner when `form?.success`
- Add `use:enhance` to the form

## Run it
```bash
npm install && npm run dev
```
Try submitting with bad data — errors should appear inline without a page reload.

## Key insight
`fail(422, data)` sends a 422 status but the page still renders normally.
The `data` you pass becomes the `form` prop on the page.
This is how you do server-side validation in SvelteKit.
