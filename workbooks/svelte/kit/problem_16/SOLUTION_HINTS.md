## Hints

- `depends('app:stats')` marks this load as depending on the key `'app:stats'`
- `invalidate('app:stats')` triggers a re-run of all loads with that dependency
- For intervals in effects:
  ```js
  $effect(() => {
    const id = setInterval(() => invalidate('app:stats'), 5000);
    return () => clearInterval(id); // cleanup when component unmounts
  });
  ```
- `invalidateAll()` is the nuclear option — re-runs every load on the page
- The `fetch` inside `load` is SvelteKit's enhanced fetch — use it, not the global one
