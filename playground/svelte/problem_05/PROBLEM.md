# Problem 05 — Reactive State

## Learning Objectives
- Declare reactive state with `$state()`
- Update state in response to events
- Understand that Svelte re-renders when state changes

## Requirements
Build a simple counter:
1. Declare a reactive variable `count` using `$state(0)`
2. Render the current count in a `<p data-testid="count">`  like: "Count: 0"
3. Add a button "Increment" that increases `count` by 1 on click
4. Add a button "Decrement" that decreases `count` by 1 on click
5. Add a button "Reset" that sets `count` back to 0

## Example Output
```
Count: 0
[Increment] [Decrement] [Reset]
```
After clicking Increment twice: "Count: 2"

## Hints
- `let count = $state(0)` makes `count` reactive
- Attach click handlers with `onclick={handler}`
- Inline arrow: `onclick={() => count += 1}`
