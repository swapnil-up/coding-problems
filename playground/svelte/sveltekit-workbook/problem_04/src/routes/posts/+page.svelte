<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<h1>Posts</h1>

<!-- TODO: loop over data.posts and render each as a link with title, author, date -->
