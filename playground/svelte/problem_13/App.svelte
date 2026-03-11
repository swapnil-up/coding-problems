<script>
  // This function simulates an API call — already complete, don't change it
  async function fetchJoke() {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 100));
    const jokes = [
      "Why do programmers prefer dark mode? Because light attracts bugs!",
      "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
      "Why did the developer go broke? Because they used up all their cache!",
    ];
    return jokes[Math.floor(Math.random() * jokes.length)];
  }

  // TODO: declare `jokePromise` as $state(fetchJoke())
</script>

<!-- TODO: use {#await jokePromise} to show:
     - loading state: <p data-testid="loading">Loading joke...</p>
     - success state: <p data-testid="joke">{joke}</p>
     - error state: <p data-testid="error">Failed to load joke: {error.message}</p>
-->

<!-- TODO: add a "New Joke" button that sets jokePromise = fetchJoke() -->
