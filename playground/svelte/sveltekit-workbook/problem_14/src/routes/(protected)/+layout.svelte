<script lang="ts">
  import type { LayoutData } from './$types';
  let { data, children }: { data: LayoutData; children: any } = $props();
</script>

<!-- TODO: header with data.user.name and a logout form -->
<!-- Logout: <form method="POST" action="/login?/logout"> <button>Logout</button> </form> -->

{@render children()}
