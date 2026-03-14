<script lang="ts">
  import type { PageData } from './$types';
  // TODO: import PUBLIC_FEATURE_FLAG from '$env/static/public'
  let { data }: { data: PageData } = $props();

  let weather = $state<{ temperature: number; condition: string; source: string } | null>(null);

  $effect(() => {
    fetch('/api/weather').then(r => r.json()).then(d => { weather = d; });
  });
</script>

<!-- TODO: show data.appName in h1 -->
<h1>Weather App</h1>

<!-- TODO: show weather data when loaded -->

<!-- TODO: show "Beta Feature" section only if PUBLIC_FEATURE_FLAG === 'true' -->
