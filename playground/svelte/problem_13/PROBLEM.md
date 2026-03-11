# Problem 13 — Await Blocks

## Learning Objectives
- Use `{#await}` to handle async Promises in templates
- Show loading, success, and error states
- Handle rejected promises with `{:catch}`

## Requirements
Build a "fetch a joke" component:
1. The file includes a `fetchJoke()` function that returns a Promise (already written)
2. Declare `jokePromise` as `$state(fetchJoke())` — starts fetching immediately
3. Use `{#await jokePromise}` to show:
   - While loading: `<p data-testid="loading">Loading joke...</p>`
   - On success: `<p data-testid="joke">{joke}</p>`
   - On error: `<p data-testid="error">Failed to load joke: {error.message}</p>`
4. Add a "New Joke" button that sets `jokePromise = fetchJoke()`

## Hints
- `{#await promise} loading {:then value} success {:catch error} error {/await}`
- Reassigning the promise variable triggers the await block to re-run
- The mock `fetchJoke` in the starter resolves with a joke string
