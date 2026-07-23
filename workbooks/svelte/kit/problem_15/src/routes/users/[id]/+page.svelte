<script lang="ts">
  import { page } from '$app/state';
  import type { PageData } from './$types';
  import Breadcrumb from '$lib/Breadcrumb.svelte';

  let { data }: { data: PageData } = $props();
</script>

<Breadcrumb />

<h1>{data.user.name}</h1>
<!-- TODO: show that page.params.id === data.user.id -->
<p>URL param: {page.params.id}</p>
