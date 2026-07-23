# Problem 15 — Component Events (Callback Props)

## Learning Objectives
- Pass callback functions as props from parent to child
- Child calls the callback to communicate back to parent
- Svelte 5's approach: event-like communication via props (no createEventDispatcher)

## Requirements
1. `RatingStars.svelte` shows 5 star buttons (★) and accepts an `onRate` callback prop
2. When a star is clicked, it calls `onRate(starNumber)` where starNumber is 1-5
3. It also accepts a `value` prop (current rating 0-5) and highlights stars up to and including `value`
4. In `App.svelte`:
   - Declare `rating` as `$state(0)`
   - Render `<RatingStars value={rating} onRate={(r) => rating = r} />`
   - Render a `<p data-testid="rating">` showing "Rating: {rating}/5" or "No rating yet" if 0

## Hints
- Callback prop pattern: `let { onRate, value } = $props();`
- Call it: `onclick={() => onRate(i)}`
- To highlight: `class:active={i <= value}` or use a conditional style
