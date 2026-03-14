# Problem 16 — Bindings

## Learning Objectives
- Use `bind:value` for text, number, and select inputs
- Use `bind:checked` for checkboxes
- Use `bind:group` for radio buttons and checkbox groups
- See how bindings create two-way data flow

## Requirements
Build a user profile form:
1. `name` ($state ''): bound to a text input
2. `age` ($state 0): bound to a number input (shows NaN protection)
3. `plan` ($state 'free'): bound to a `<select>` with options: free, pro, enterprise
4. `newsletter` ($state false): bound to a checkbox
5. `interests` ($state []): bound to a group of checkboxes with values: "coding", "design", "writing"
6. `contactMethod` ($state 'email'): bound to radio buttons with values: email, phone, none
7. Render a `<div data-testid="preview">` that shows all current values as a summary

## Hints
- `<input bind:value={name}>` — text
- `<input type="number" bind:value={age}>` — number (auto-coerces to number)
- `<select bind:value={plan}>` with `<option value="x">X</option>`
- `<input type="checkbox" bind:checked={newsletter}>`
- `<input type="checkbox" bind:group={interests} value="coding">` — adds/removes from array
- `<input type="radio" bind:group={contactMethod} value="email">` — sets to scalar
