<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<h1>{data.product.name}</h1>
<p>Price: ${data.product.price}</p>
<a href="/products">← Back to products</a>
