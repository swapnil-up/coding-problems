<script lang="ts">
  let { children } = $props();
</script>

<div class="layout">
  <aside>
    <!-- TODO: add nav links for Overview, Settings, Profile -->
     <nav>
      <a href='/dashboard'>Dashboard</a>
      <a href='/dashboard/settings'>Settings</a>
      <a href='/dashboard/profile'>Profile</a>
     </nav>
  </aside>

  <main>
  {@render children()}
    <!-- TODO: render children here -->
  </main>
</div>

<style>
  .layout { display: flex; min-height: calc(100vh - 52px); }
  aside { width: 200px; background: #f1f5f9; padding: 1rem; }
  aside a { display: block; padding: 0.5rem; color: #334155; text-decoration: none; }
  aside a:hover { background: #e2e8f0; border-radius: 4px; }
  main { flex: 1; padding: 2rem; }
</style>
