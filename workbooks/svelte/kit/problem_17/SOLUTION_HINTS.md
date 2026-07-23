## Hints

- `export const prerender = true` goes at the module level (top of `<script module>` or a `+page.server.ts`)
- `entries` function for dynamic prerendered routes:
  ```ts
  export const entries: EntryGenerator = () => posts.map(p => ({ slug: p.slug }));
  ```
- `export const ssr = false` must be in `<script module>` (not `<script>`) in `.svelte` files
- In `.server.ts` files, just `export const ssr = false` at the top level
- `localStorage` access in `$effect` is safe even with `ssr=false` because effects only run client-side
