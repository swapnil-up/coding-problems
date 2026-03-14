## Hints

- In Svelte 5 / SvelteKit, layouts use `{@render children()}` not `<slot />`
- Get `children` from `$props()`: `let { children } = $props();`
- Layouts wrap children automatically — no config needed, just the file placement
- Root layout wraps EVERY page. Dashboard layout wraps only dashboard/* pages.
