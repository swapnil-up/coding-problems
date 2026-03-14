## Hints

- `LayoutServerLoad` is the type for `+layout.server.ts` load functions
- Layout data merges with page data — `data.user` just works in child pages
- In `+layout.svelte`, get `children` from props: `let { data, children } = $props()`
- Use `{@render children()}` inside the layout template (not `<slot />`)
