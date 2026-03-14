<script lang="ts">
  import { page, navigating } from '$app/state';
  let { children } = $props();
</script>

<nav>
  <!-- TODO: links to /, /users/1, /users/2, /users/3 -->
  <!-- TODO: add class:active based on page.url.pathname matching -->
  <a href="/">Home</a>
  <a href="/users/1">User 1</a>
  <a href="/users/2">User 2</a>
</nav>

<!-- TODO: show "Navigating..." if navigating is truthy -->

{@render children()}

<style>
  nav { display:flex; gap:1rem; padding:1rem; background:#1e293b; }
  nav a { color:#94a3b8; text-decoration:none; }
  nav a.active { color:white; font-weight:bold; }
  .spinner { padding:0.5rem 1rem; background:#fef3c7; text-align:center; }
</style>
