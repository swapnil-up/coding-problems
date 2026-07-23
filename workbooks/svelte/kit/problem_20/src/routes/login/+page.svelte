<script lang="ts">
  import { enhance } from '$app/forms';
  import { page } from '$app/state';
  import type { ActionData } from './$types';
  let { form }: { form: ActionData } = $props();
  const from = $derived(page.url.searchParams.get('from'));
</script>

<div class="login-page">
  <h1>CMS Login</h1>
  {#if from}<p>Login required to access <code>{from}</code></p>{/if}
  {#if form?.error}<p class="error">{form.error}</p>{/if}

  <form method="POST" action="?/login" use:enhance>
    <input type="password" name="password" placeholder="Password (hint: cms-password)" required />
    <button type="submit">Login</button>
  </form>

  <p><a href="/blog">← View public blog</a></p>
</div>

<style>
  .login-page { max-width:360px; margin:4rem auto; padding:2rem; border:1px solid #e2e8f0; border-radius:8px; }
  form { display:flex; flex-direction:column; gap:0.75rem; margin:1rem 0; }
  input { padding:0.5rem; border:1px solid #cbd5e1; border-radius:4px; }
  button { padding:0.75rem; background:#3b82f6; color:white; border:none; border-radius:4px; cursor:pointer; }
  .error { color:#ef4444; }
</style>
