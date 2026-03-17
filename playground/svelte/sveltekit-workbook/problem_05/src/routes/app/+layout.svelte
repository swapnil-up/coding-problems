<script lang="ts">
  import type { LayoutData } from './$types';
  // TODO: get data and children from $props()
  // let { data, children }: { data: LayoutData; children: any } = $props();
  let {data, children}: {data: LayoutData; children: any}= $props();
</script>
<header>
  {data.user.name}
  {data.user.email}
</header>
{@render children()}
<!-- TODO: header showing data.user.name and data.user.email -->
<!-- TODO: nav links to /app/feed and /app/notifications -->
<!-- TODO: {@render children()} -->

<style>
  header { background: #0f172a; color: white; padding: 1rem 2rem; display: flex; justify-content: space-between; }
  nav { display: flex; gap: 1rem; padding: 1rem 2rem; border-bottom: 1px solid #e2e8f0; }
  nav a { color: #475569; text-decoration: none; }
  main { padding: 2rem; }
</style>
