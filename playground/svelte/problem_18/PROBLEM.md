# Problem 18 — Transitions

## Learning Objectives
- Add enter/exit transitions with `transition:`, `in:`, and `out:`
- Use built-in transitions: `fade`, `fly`, `slide`, `scale`
- Pass parameters to transitions

## Requirements
Build an animated notification stack:
1. Import `fade`, `fly`, and `slide` from `'svelte/transition'`
2. Declare `messages` as `$state([])` — array of `{ id, text }` objects
3. Declare `nextId` as `$state(1)`
4. Add button "Add Message" that pushes a new message: `{ id: nextId++, text: "Message #${nextId}" }`
5. Render each message in a `<div class="message">` inside `{#each messages as msg (msg.id)}`
   - Apply `transition:fly={{ x: 200, duration: 300 }}` to each message div
6. Each message has a "×" button that removes it from the array
7. Add a separate `<div class="banner">` that shows only when `messages.length === 0`
   - Apply `transition:fade` to the banner
   - Text: "No messages! Add one above."

## Hints
- Import: `import { fade, fly, slide } from 'svelte/transition'`
- Usage: `<div transition:fly={{ x: 200 }}>` or `<div in:fly out:fade>`
- Must use keyed each `(msg.id)` for transitions to work on individual items
- `transition:` handles both in AND out; use `in:` and `out:` for separate
