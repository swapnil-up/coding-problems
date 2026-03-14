<script lang="ts">
  import { enhance } from '$app/forms';
  import { page } from '$app/state';
  import type { ActionData } from './$types';
  let { form }: { form: ActionData } = $props();

  const from = $derived(page.url.searchParams.get('from'));
</script>

<!-- TODO: if `from` exists, show "You need to log in to access {from}" -->

<!-- TODO: if form?.error, show the error message -->

<!-- TODO: add use:enhance, set action="?/login" -->
<form method="POST">
  <label>
    Password
    <input type="password" name="password" placeholder="try: sveltekit" />
  </label>
  <button type="submit">Login</button>
</form>
