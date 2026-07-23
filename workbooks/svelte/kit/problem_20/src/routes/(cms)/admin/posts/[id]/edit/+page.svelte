<script lang="ts">
  import { enhance } from '$app/forms';
  import type { ActionData, PageData } from './$types';
  let { data, form }: { data: PageData; form: ActionData } = $props();
</script>

<h1>Edit: {data.post.title}</h1>
{#if form?.success}<p class="success">Saved!</p>{/if}

<form method="POST" action="?/update" use:enhance>
  <!-- TODO: same fields as new post form, pre-filled with data.post values -->
  <!-- title, body, published checkbox, submit button "Save Changes" -->
</form>

<div style="margin-top:1rem; display:flex; gap:1rem;">
  <a href="/admin">← All Posts</a>
  <a href="/blog/{data.post.slug}" target="_blank">View on blog ↗</a>
</div>
