# Problem 03 — Nested Components

## Learning Objectives
- Import and use a child Svelte component
- Understand that component names should be capitalized
- Compose UIs from multiple components

## Requirements
1. `Card.svelte` is provided and renders a styled card box — do not change it
2. In `App.svelte`:
   - Import `Card` from `./Card.svelte`
   - Render **three** `<Card />` elements
   - Each card should be wrapped in a `<div class="grid">` container
3. The grid div should contain exactly 3 Card elements

## Hints
- Import syntax: `import Card from './Card.svelte'`
- Use the component like an HTML tag: `<Card />`
- Components must start with a capital letter to distinguish them from HTML elements
