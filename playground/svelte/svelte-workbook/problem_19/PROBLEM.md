# Problem 19 — Key Blocks

## Learning Objectives
- Use `{#key expr}` to force re-creation of a DOM subtree when a value changes
- Understand the difference between keyed-each (for lists) and key-block (for single elements)
- Common use case: re-triggering a transition when a value changes

## Requirements
Build a "word of the day" component that animates each new word:
1. Declare a `words` array (not state): `['Svelte', 'Reactive', 'Compiled', 'Elegant', 'Fast']`
2. Declare `index` as `$state(0)`
3. Declare `word` as `$derived(words[index])`
4. Render the current word in an `<h2>` wrapped in `{#key word}`
   - Apply `transition:fly={{ y: -30, duration: 400 }}` to the h2
5. Add "Previous" and "Next" buttons that decrement/increment `index`
   - Clamp: index should not go below 0 or above `words.length - 1`
6. Render `<p data-testid="info">{index + 1} / {words.length}</p>`

## Why key blocks?
Without `{#key}`, changing the word just updates the text — no new element is created, so the transition doesn't re-trigger. `{#key word}` tears down and recreates the inner DOM whenever `word` changes.

## Hints
- `{#key expression} ... {/key}` — content is recreated when expression changes
- The transition inside a key block fires every time the key changes
- Import `fly` from `'svelte/transition'`
