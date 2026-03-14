<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();

  async function setUser() {
    await fetch('/api/set-user', { method: 'POST' });
    location.reload();
  }
  async function clearUser() {
    await fetch('/api/clear-user', { method: 'POST' });
    location.reload();
  }
</script>

<!-- TODO: show data.user info if logged in, "Not logged in" otherwise -->

<div style="margin-top:1rem; display:flex; gap:1rem;">
  <button onclick={setUser}>Set user cookie (Alice/admin)</button>
  <button onclick={clearUser}>Clear user cookie</button>
</div>
