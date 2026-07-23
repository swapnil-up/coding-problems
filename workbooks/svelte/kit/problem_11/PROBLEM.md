# Problem 11 — Error Pages

## What you'll learn
- `error(status, message)` from `@sveltejs/kit`
- `+error.svelte` — custom error UI
- Route-level vs root-level error pages
- The `$page.error` object

## Context
When something goes wrong in a `load` function or action, you throw an error.
SvelteKit catches it and renders the nearest `+error.svelte` file.

## Tasks

### 1. Fix `src/routes/products/[id]/+page.server.ts`
Currently returns null for missing products. Change it to:
- `throw error(404, 'Product not found')` if the product doesn't exist
- `throw error(400, 'Invalid product ID')` if the ID isn't a valid number

### 2. Create `src/routes/+error.svelte`
This is the **root** error page — shown when no closer error page exists.
- Import `page` from `$app/state`
- Show `page.error.message` and `page.status`
- Add a link back to `/`

### 3. Create `src/routes/products/+error.svelte`
This is a **route-level** error page — only shown for `/products/*` errors.
- Show a products-specific message: "Oops! Product issue: {page.error.message}"
- Add a link back to `/products`

### 4. Create `src/routes/products/+page.svelte`
Simple list of product links (like problem 02).

## Run it
```bash
npm install && npm run dev
```
Try `/products/999` — you should see the product-specific error page.
Try adding a route that throws a 500 to test the root error page.

## Key insight
Error pages are scoped — a `+error.svelte` in `/products/` only handles errors from product routes.
The root `src/routes/+error.svelte` is the final fallback.
