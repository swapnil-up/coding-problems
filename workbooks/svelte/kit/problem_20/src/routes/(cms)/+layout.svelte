<script lang="ts">
  import { page } from '$app/state';
  import type { LayoutData } from './$types';
  let { data, children }: { data: LayoutData; children: any } = $props();
</script>

<div class="cms">
  <aside>
    <div class="user-info">
      <!-- TODO: show data.user.name -->
    </div>
    <nav>
      <a href="/admin" class:active={page.url.pathname === '/admin'}>All Posts</a>
      <a href="/admin/posts/new" class:active={page.url.pathname === '/admin/posts/new'}>+ New Post</a>
    </nav>
    <form method="POST" action="/login?/logout" style="margin-top:auto">
      <button type="submit" class="logout">Logout</button>
    </form>
  </aside>
  <main>
    {@render children()}
  </main>
</div>

<style>
  .cms { display:flex; min-height:100vh; }
  aside { width:220px; background:#1e293b; color:white; padding:1.5rem; display:flex; flex-direction:column; gap:0.5rem; }
  aside nav { display:flex; flex-direction:column; gap:0.25rem; }
  aside a { color:#94a3b8; text-decoration:none; padding:0.5rem 0.75rem; border-radius:4px; }
  aside a.active, aside a:hover { color:white; background:#334155; }
  main { flex:1; padding:2rem; }
  .user-info { color:#cbd5e1; font-size:0.875rem; padding:0.5rem 0 1rem; border-bottom:1px solid #334155; margin-bottom:0.5rem; }
  .logout { background:none; border:1px solid #475569; color:#94a3b8; padding:0.5rem 1rem; border-radius:4px; cursor:pointer; width:100%; }
</style>
