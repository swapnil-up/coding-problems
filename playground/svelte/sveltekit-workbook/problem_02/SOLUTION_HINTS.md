## Hints

- `load` receives `{ params }` — access the param with `params.id`
- Return a plain object from `load`: `return { product: products[params.id] ?? null }`
- In the Svelte component: `let { data }: { data: PageData } = $props();`
- Then use `data.product` in the template
- `PageServerLoad` and `PageData` are auto-generated types from `./$types`
