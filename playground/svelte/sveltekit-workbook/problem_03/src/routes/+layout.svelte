<script lang="ts">
  let { children } = $props();
</script>

<nav>
  <a href="/">Home</a>
  <a href="/dashboard">Dashboard</a>
</nav>
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
