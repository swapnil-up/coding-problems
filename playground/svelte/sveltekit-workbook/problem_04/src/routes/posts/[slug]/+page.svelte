<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<!-- TODO: if data.post, show title/author/date/body -->
<!-- TODO: if not, show "Post not found" -->
<!-- TODO: back link to /posts -->
