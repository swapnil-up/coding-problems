<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<h1>Blog (prerendered)</h1>
<ul>
  {#each data.posts as post}
    <li><a href="/blog/{post.slug}">{post.title}</a></li>
  {/each}
</ul>
