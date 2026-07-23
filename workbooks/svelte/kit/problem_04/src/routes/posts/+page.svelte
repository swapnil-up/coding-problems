<script lang="ts">
  import { posts } from '$lib/posts';
import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<h1>Posts</h1>

{#each data.posts as post}
  <a href="/posts/{post.slug}">{post.title}</a>
  <p>{post.author}</p>
  <p>{post.date}</p>
{/each}
<!-- TODO: loop over data.posts and render each as a link with title, author, date -->
