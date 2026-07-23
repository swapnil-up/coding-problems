<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<h1>Welcome to the dashboard, {data.username}!</h1>
<p>You are logged in.</p>
<form method="POST" action="/login?/logout">
  <button type="submit">Logout</button>
</form>
