<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<h1>Dashboard</h1>
<p>Logged in as: {data.user?.name} ({data.user?.role})</p>
<a href="/settings">Go to Settings</a>
