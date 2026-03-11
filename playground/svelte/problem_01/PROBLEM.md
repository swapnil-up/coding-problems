# Problem 01 — Hello Svelte

## Learning Objectives
- Understand the three sections of a Svelte component: `<script>`, markup, `<style>`
- Use JavaScript variables in markup with `{}`
- Write scoped CSS styles

## Requirements
The component should:
1. Display an `<h1>` that says "Hello, [name]!" where name comes from a JS variable
2. Display a `<p>` with the text "I am learning Svelte."
3. Style the `<h1>` so it has `color: rebeccapurple`
4. The name variable should be set to `"World"` by default

## Example Output
```
Hello, World!
I am learning Svelte.
```
(with the h1 in rebeccapurple)

## Hints
- A Svelte component file contains `<script>`, HTML markup, and `<style>` — in any order
- Use `{variableName}` in HTML to render a JS value
- Styles in `<style>` are automatically scoped to this component
