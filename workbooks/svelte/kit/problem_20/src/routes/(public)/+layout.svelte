<script lang="ts">
  import { page } from '$app/state';
  let { children } = $props();
</script>

<header>
  <nav>
    <a href="/blog" class:active={page.url.pathname === '/blog'}>Blog</a>
    <a href="/admin" style="margin-left:auto">Admin →</a>
  </nav>
</header>

{@render children()}

<style>
  header { background:#0f172a; padding:1rem 2rem; }
  nav { display:flex; gap:1.5rem; align-items:center; }
  nav a { color:#94a3b8; text-decoration:none; }
  nav a.active, nav a:hover { color:white; }
  main { max-width:720px; margin:2rem auto; padding:0 1rem; }
</style>
