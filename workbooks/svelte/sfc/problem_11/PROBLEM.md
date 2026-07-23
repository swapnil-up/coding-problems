# Problem 11 — If / Else Blocks

## Learning Objectives
- Use `{#if}`, `{:else}`, and `{:else if}` to conditionally render content
- Toggle UI elements based on state

## Requirements
Build a simple traffic light component:
1. Declare `signal` as `$state("red")` — possible values: "red", "yellow", "green"
2. Render a `<div class="light">` that shows different content based on `signal`:
   - red → `<p data-testid="message">Stop!</p>` with red background indicator
   - yellow → `<p data-testid="message">Slow down!</p>`
   - green → `<p data-testid="message">Go!</p>`
   - anything else → `<p data-testid="message">Unknown signal</p>`
3. Add three buttons "Red", "Yellow", "Green" to change the signal
4. Add a `<span data-testid="signal">` showing the current signal value

## Hints
- `{#if signal === 'red'} ... {:else if signal === 'yellow'} ... {:else} ... {/if}`
- Use `onclick={() => signal = 'red'}` etc. on the buttons
