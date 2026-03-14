<script lang="ts">
  import { page } from '$app/state';

  // TODO: split page.url.pathname by '/' and build breadcrumb segments
  // e.g. '/users/42' → ['', 'users', '42'] → filter empty → ['users', '42']
  // Each segment links to the cumulative path up to that point
  const segments = $derived(
    // TODO: compute array of { label, href } objects
    [] as { label: string; href: string }[]
  );
</script>

<nav class="breadcrumb">
  <a href="/">Home</a>
  <!-- TODO: render each segment with ' / ' separator -->
</nav>

<style>
  .breadcrumb { font-size:0.875rem; color:#64748b; margin-bottom:1rem; }
  .breadcrumb a { color:#3b82f6; text-decoration:none; }
</style>
