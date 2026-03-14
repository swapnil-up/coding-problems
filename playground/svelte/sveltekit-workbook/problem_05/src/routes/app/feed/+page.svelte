<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
  // data.user is available here even though this page didn't load it!
  // data.feedItems comes from this page's own load function
</script>

<!-- TODO: h1 saying "Feed — welcome back, {data.user.name}" -->
<!-- TODO: list of feed items -->
