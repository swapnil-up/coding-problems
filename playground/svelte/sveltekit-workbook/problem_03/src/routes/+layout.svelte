<script lang="ts">
  let { children } = $props();
</script>

<!-- TODO: add a <nav> with links to "/" (Home) and "/dashboard" (Dashboard) -->
<!-- Style it simply — just display:flex and a bit of padding is fine -->

<!-- TODO: render the child page here -->
{@render children()}

<style>
  nav {
    background: #1e293b;
    padding: 1rem 2rem;
    display: flex;
    gap: 1.5rem;
  }
  nav a { color: white; text-decoration: none; }
  nav a:hover { text-decoration: underline; }
</style>
