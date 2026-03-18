<script lang="ts">
  import type { Product } from '$lib/products';

  let productList = $state<Product[]>([]);
  let selectedProduct = $state<Product | null>(null);
  let category = $state('');
  let loading = $state(false);

  async function fetchProducts() {
    loading = true;
    const url = '/api/products' + (category ? `?category=${category}` : '');
    const response = await fetch(url);
    if(response.ok){
      productList = await response.json();
    }
    // TODO: fetch '/api/products' + (category ? `?category=${category}` : '')
    // set productList to the result
    loading = false;
  }

  async function fetchProduct(id: number) {
    const url = `/api/products/${id}`
    const response = await fetch(url);
    if (response.ok){
      selectedProduct = await response.json()
    }
    // TODO: fetch `/api/products/${id}`
    // set selectedProduct to the result
  }

  // TODO: fetch products on mount using $effect
</script>

<h1>Products API Demo</h1>

<div class="controls">
  <select bind:value={category} onchange={fetchProducts}>
    <option value="">All categories</option>
    <option value="peripherals">Peripherals</option>
    <option value="displays">Displays</option>
    <option value="accessories">Accessories</option>
  </select>
</div>

{#if loading}
  <p>Loading...</p>
{:else}
  <ul>
    {#each productList as product}
      <li>
        {product.name} — ${product.price}
        <button onclick={() => fetchProduct(product.id)}>Details</button>
      </li>
    {/each}
  </ul>
{/if}

{#if selectedProduct}
  <div class="detail">
    <h2>{selectedProduct.name}</h2>
    <p>Price: ${selectedProduct.price}</p>
    <p>Category: {selectedProduct.category}</p>
    <button onclick={() => selectedProduct = null}>Close</button>
  </div>
{/if}
