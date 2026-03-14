# Problem 08 — Effects

## Learning Objectives
- Use `$effect()` to run side effects when state changes
- Understand that effects run after the DOM updates
- Return a cleanup function from `$effect` when needed

## Requirements
Build a search component with a "recent searches" log:
1. Declare `query` as `$state('')`
2. Declare `log` as `$state([])` — an array of strings
3. Use `$effect` to watch `query`: whenever `query` changes AND is non-empty, push `"Searched: {query}"` to the log
4. Render an `<input>` bound to `query` with placeholder "Type to search..."
5. Render a `<ul data-testid="log">` showing all log entries

## Important Note
Effects run *after* render, including on first mount. Make sure to guard against the initial empty string.

## Hints
- `$effect(() => { ... })` runs whenever reactive values it reads change
- Effects re-run whenever any `$state` or `$derived` they read updates
- Return a function from `$effect` to clean up (e.g. `return () => clearTimeout(id)`)
- For this problem you don't need cleanup — just guard with `if (query)`
