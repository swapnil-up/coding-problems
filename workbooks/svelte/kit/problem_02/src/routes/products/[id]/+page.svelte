<script lang="ts">
  import type { PageData } from './$types';

  const {data}: { data: PageData }=$props();
  // TODO: declare the data prop
  // let { data }: { data: PageData } = $props();
</script>

{#if (data.product)}
  {data.product.name}
  {data.product.price}
{:else}
  <p>Product not found</p>
{/if}

<a href="/products">Go back</a>
<!-- TODO: if data.product exists, show its name and price -->
<!-- TODO: if not, show "Product not found" -->
<!-- TODO: add a back link to /products -->
