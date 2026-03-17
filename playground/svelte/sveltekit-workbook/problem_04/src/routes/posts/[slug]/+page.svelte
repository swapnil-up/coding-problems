<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

{#if data.post}
<p>{data.post.title}</p>
<p>{data.post.author}</p>
<p>{data.post.date}</p>
<p>{data.post.body}</p>
{:else}
<p>Post not found</p>
{/if}

<a href="/posts">Posts</a>
<!-- TODO: if data.post, show title/author/date/body -->
<!-- TODO: if not, show "Post not found" -->
<!-- TODO: back link to /posts -->
