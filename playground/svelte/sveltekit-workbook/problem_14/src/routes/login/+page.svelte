<script lang="ts">
  import { enhance } from '$app/forms';
  import { page } from '$app/state';
  import type { ActionData } from './$types';
  let { form }: { form: ActionData } = $props();
  const from = $derived(page.url.searchParams.get('from'));
</script>

<h1>Login</h1>
{#if from}<p>Login required to access <code>{from}</code></p>{/if}
{#if form?.error}<p class="error">{form.error}</p>{/if}

<form method="POST" action="?/login" use:enhance>
  <input type="password" name="password" placeholder="password (hint: admin123)" />
  <button type="submit">Login</button>
</form>

<style>
  form { display:flex; gap:0.5rem; margin-top:1rem; }
  input { padding: 0.5rem; border: 1px solid #cbd5e1; border-radius:4px; flex:1; }
  button { padding: 0.5rem 1rem; background:#3b82f6; color:white; border:none; border-radius:4px; cursor:pointer; }
  .error { color:#ef4444; }
</style>
