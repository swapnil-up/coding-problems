<script module>
  // TODO: export const ssr = false
  // This disables SSR for this page — safe to use localStorage here
</script>

<script lang="ts">
  let count = $state(0);

  $effect(() => {
    // TODO: read count from localStorage on mount
    // count = parseInt(localStorage.getItem('count') ?? '0');
  });

  function increment() {
    count++;
    // TODO: save count to localStorage
  }
</script>

<h1>Client-only Page (ssr=false)</h1>
<p>This count persists in localStorage:</p>
<p>{count}</p>
<button onclick={increment}>Increment</button>
