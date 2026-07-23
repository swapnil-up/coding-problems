# Problem 02 — Route Parameters

## What you'll learn
- Dynamic route segments with `[param]` folders
- Accessing params inside a `load` function
- Passing data from `load` to the page via the `data` prop

## Context
A folder named `[id]` creates a dynamic route — `/products/42` would set `params.id = '42'`.
You access params inside `+page.server.ts` via the `load` function's `params` argument.

## Tasks

### 1. Create a product list page (`src/routes/products/+page.svelte`)
Show a hardcoded list of product links:
```
/products/1 → "Keyboard"
/products/2 → "Mouse"  
/products/3 → "Monitor"
```

### 2. Fix the product detail page
`src/routes/products/[id]/+page.server.ts` has a broken `load` function — fix it.
`src/routes/products/[id]/+page.svelte` needs to display the loaded data.

The load function should:
- Read `params.id`
- Look up the product from this map:
  ```ts
  const products: Record<string, { name: string; price: number }> = {
    '1': { name: 'Keyboard', price: 79.99 },
    '2': { name: 'Mouse', price: 39.99 },
    '3': { name: 'Monitor', price: 299.99 },
  };
  ```
- Return `{ product }` if found
- For now, return a placeholder if not found (we'll learn `error()` in problem 11)

### 3. Display the product
In `+page.svelte`, use `export let data` to receive the loaded product and display its name and price.

## Run it
```bash
npm install && npm run dev
```
Visit `/products`, click a product, observe the URL and data changing.

## Key insight
`load()` runs on the **server** (because it's in `+page.server.ts`).
The returned object becomes the `data` prop on the page component.
