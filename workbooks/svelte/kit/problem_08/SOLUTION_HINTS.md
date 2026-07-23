## Hints

- Import `fail` from `'@sveltejs/kit'`
- `return fail(422, { errors, values })` — the second arg becomes the `form` prop
- `fail` must be returned, not thrown
- In the template: `{#if form?.errors?.username}<span class="error">{form.errors.username}</span>{/if}`
- Repopulate: `value={form?.values?.username ?? ''}`
- TypeScript narrows `ActionData` — you may need to cast or check nullability
