<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<a href="/blog">← Blog</a>
<h1>{data.post.title}</h1>
<p><small>{data.post.date}</small></p>
<p>{data.post.body}</p>
