## Hints

- The key difference: `await fetchFn()` vs `fetchFn()` (no await)
- Awaited values are available immediately in the template
- Non-awaited Promises appear as Promise objects in `data` — use `{#await}` to render them
- The TypeScript type of `data.fullReport` will be `Promise<...>` — `{#await}` handles this correctly
- In production, SvelteKit streams the resolved value to the browser as a `<script>` tag injected into the HTML stream
