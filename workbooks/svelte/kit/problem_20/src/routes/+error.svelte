<script lang="ts">
  import { page } from '$app/state';
</script>

<div class="error-page">
  <h1>{page.status}</h1>
  <p>{page.error?.message ?? 'Something went wrong'}</p>
  <a href="/">← Go home</a>
</div>

<style>
  .error-page { text-align:center; padding:4rem; }
  h1 { font-size:5rem; color:#ef4444; margin-bottom:0.5rem; }
</style>
