# Problem 14 — DOM Events

## Learning Objectives
- Attach event handlers with `onclick`, `oninput`, `onkeydown`, etc.
- Use inline vs named handlers
- Work with the event object (e.g. `e.key`, `e.target.value`)

## Requirements
Build a color picker / keyboard demo:
1. Declare `color` as `$state('#3b82f6')`
2. Declare `keyLog` as `$state([])`
3. Render a color swatch: `<div class="swatch" style="background: {color};">`
4. Render a color input `<input type="color">` with an `oninput` handler that updates `color` from `event.target.value`
5. Render a text input with:
   - placeholder "Press keys here..."
   - `onkeydown` handler that pushes `e.key` to `keyLog` (except if `keyLog` already has 5 entries, reset it to `[e.key]`)
6. Render a `<ul data-testid="key-log">` showing each logged key as an `<li>`

## Hints
- Inline handlers: `oninput={(e) => color = e.target.value}`
- Event objects in Svelte 5 are standard DOM events — no magic wrappers
- `onkeydown` fires before the character appears in the input
