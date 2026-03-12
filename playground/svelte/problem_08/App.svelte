<script>
  let query = $state("");
  let log = $state([]);

  $effect(() => {
    if (query.trim() == "") return;
    if (log[log.length -1] == "Searched: " + query) return;
    log.push("Searched: " + query);
  });
</script>

<input bind:value={query} placeholder="Type to search..." />
<p>Current query: {query}</p>
<ul data-testid="log">
  {#each log as logitem}
    <li>{logitem}</li>
  {/each}
</ul>
