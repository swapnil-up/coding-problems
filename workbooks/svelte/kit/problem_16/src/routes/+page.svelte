<script lang="ts">
  import { invalidate } from '$app/navigation';
  import type { PageData } from './$types';

  let { data }: { data: PageData } = $props();

  // TODO: $effect to set up a 5-second interval calling invalidate('app:stats')
  // Return a cleanup function to clear the interval
</script>

<h1>Live Stats Dashboard</h1>

<!-- TODO: refresh button -->
<button onclick={() => invalidate('app:stats')}>Refresh</button>

<!-- TODO: show data.timestamp, data.visitors, data.revenue, data.requests -->
