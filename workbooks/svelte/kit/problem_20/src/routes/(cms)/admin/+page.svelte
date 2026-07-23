<script lang="ts">
  import { enhance } from '$app/forms';
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<h1>All Posts</h1>
<a href="/admin/posts/new">+ New Post</a>

<!-- TODO: table/list of all posts (including drafts) with:
     - title, published status, date
     - Edit link to /admin/posts/{id}/edit
     - Delete form with action="?/delete" and use:enhance
-->
