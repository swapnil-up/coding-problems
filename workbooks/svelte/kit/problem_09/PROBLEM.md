# Problem 09 — API Routes (GET)

## What you'll learn
- `+server.ts` for building API endpoints
- The `GET` handler and returning `json()`
- URL search params for filtering
- Dynamic API routes

## Context
SvelteKit's `+server.ts` files export HTTP verb handlers: `GET`, `POST`, `PUT`, `DELETE`.
They're perfect for building JSON APIs, webhooks, or any custom server endpoint.

## What you're building
Two API endpoints:
- `GET /api/products` — list all products, with optional `?category=` filter
- `GET /api/products/[id]` — get a single product by ID

And a frontend page that uses `fetch` to call these endpoints.

## Tasks

### 1. Fix `src/routes/api/products/+server.ts`
Export a `GET` handler that:
- Reads `url.searchParams.get('category')`  
- Filters products by category if provided
- Returns `json(filteredProducts)`

### 2. Fix `src/routes/api/products/[id]/+server.ts`
Export a `GET` handler that:
- Parses `params.id` as a number
- Finds the matching product
- Returns `json(product)` if found
- Returns `new Response('Not found', { status: 404 })` if not

### 3. Fix `src/routes/+page.svelte`
The page already has the UI skeleton. Wire up:
- On mount, fetch `/api/products` and show results
- When the category select changes, re-fetch with `?category=value`
- Add a button "View Details" per product that fetches `/api/products/{id}` and shows details

## Run it
```bash
npm install && npm run dev
```
Open the Network tab and watch the API requests.

## Key insight
API routes co-exist with page routes. Use them for:
- Fetching data from client-side JS
- Webhooks (POST from external services)
- File downloads
- Anything that needs raw HTTP control
