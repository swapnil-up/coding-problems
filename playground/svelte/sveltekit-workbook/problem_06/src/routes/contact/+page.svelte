<script lang="ts">
  import { enhance } from '$app/forms';
  import type { ActionData } from './$types';

  let { form }: { form: ActionData } = $props();
</script>

<h1>Contact Us</h1>

<!-- TODO: show success message if form?.success is true -->
<!-- "Thanks, {form.name}! We'll be in touch." -->

<!-- 
  TODO: add use:enhance to the form below
  The action="?" means "POST to this page's default action"
-->
<form method="POST">
  <label>
    Name
    <input type="text" name="name" required />
  </label>

  <label>
    Email
    <input type="email" name="email" required />
  </label>

  <button type="submit">Send Message</button>
</form>

<style>
  form { display: flex; flex-direction: column; gap: 1rem; max-width: 400px; }
  label { display: flex; flex-direction: column; gap: 0.25rem; font-weight: 500; }
  input { padding: 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; }
  button { padding: 0.75rem; background: #3b82f6; color: white; border: none; border-radius: 4px; cursor: pointer; }
  .success { background: #d1fae5; border: 1px solid #10b981; padding: 1rem; border-radius: 6px; }
</style>
