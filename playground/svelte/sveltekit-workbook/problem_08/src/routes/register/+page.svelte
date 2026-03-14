<script lang="ts">
  import { enhance } from '$app/forms';
  import type { ActionData } from './$types';
  let { form }: { form: ActionData } = $props();
</script>

<h1>Create Account</h1>

<!-- TODO: show success message when form?.success is true -->

<!-- TODO: add use:enhance to this form -->
<form method="POST">
  <div class="field">
    <label for="username">Username</label>
    <!-- TODO: add value={form?.values?.username ?? ''} to repopulate -->
    <input type="text" id="username" name="username" />
    <!-- TODO: show form?.errors?.username if it exists -->
  </div>

  <div class="field">
    <label for="email">Email</label>
    <!-- TODO: repopulate and show error -->
    <input type="email" id="email" name="email" />
  </div>

  <div class="field">
    <label for="password">Password</label>
    <input type="password" id="password" name="password" />
    <!-- TODO: show error -->
  </div>

  <div class="field">
    <label for="confirmPassword">Confirm Password</label>
    <input type="password" id="confirmPassword" name="confirmPassword" />
    <!-- TODO: show error -->
  </div>

  <button type="submit">Register</button>
</form>

<style>
  form { display: flex; flex-direction: column; gap: 1rem; max-width: 400px; }
  .field { display: flex; flex-direction: column; gap: 0.25rem; }
  label { font-weight: 500; }
  input { padding: 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; }
  .error { color: #ef4444; font-size: 0.85rem; }
  button { padding: 0.75rem; background: #3b82f6; color: white; border: none; border-radius: 4px; cursor: pointer; }
  .success { background: #d1fae5; border: 1px solid #10b981; padding: 1rem; border-radius: 6px; }
</style>
