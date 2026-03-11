# Problem 10 — Prop Defaults & Spread Props

## Learning Objectives
- Set default values for props
- Use spread syntax to pass many props at once
- Understand `$$props` / rest props pattern

## Requirements
1. `Badge.svelte` accepts props: `label` (required), `color` (default: `"gray"`), `size` (default: `"medium"`)
2. It renders a `<span class="badge">` showing the label, with `data-color` and `data-size` attributes set
3. In `App.svelte`, create an array of badge data objects and render them using spread props
4. The array should have at least 3 badges:
   - `{ label: "New", color: "green" }` (size defaults to "medium")
   - `{ label: "Hot", color: "red", size: "large" }`
   - `{ label: "Draft" }` (both color and size should use defaults)

## Hints
- Default props: `let { label, color = 'gray', size = 'medium' } = $props();`
- Spread an object as props: `<Badge {...badgeData} />`
- This is the same as writing each prop out manually
