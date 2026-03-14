<script lang="ts">
  import { enhance } from '$app/forms';
  import type { ActionData } from './$types';
  let { form }: { form: ActionData } = $props();
</script>

<h1>New Post</h1>

<form method="POST" use:enhance>
  <!-- TODO: title input (show error if form?.errors?.title) -->
  <!-- TODO: body textarea (show error if form?.errors?.body) -->
  <!-- TODO: published checkbox -->
  <!-- TODO: submit button "Create Post" -->
</form>

<a href="/admin">← Cancel</a>
