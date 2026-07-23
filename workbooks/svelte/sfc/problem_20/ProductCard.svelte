<script>
  let { id, name, price, inCart, onAddToCart } = $props();
</script>

<div class="product-card" class:in-cart={inCart}>
  <h3>{name}</h3>
  <p class="price">${price}</p>
  <button onclick={() => onAddToCart({ id, name, price })}>
    {#if inCart}
      Add Again
    {:else}
      Add to Cart
    {/if}
  </button>
</div>

<style>
  .product-card {
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
    /* transition: border-color 0.2s; */
  }
  .product-card.in-cart {
    border-color: #10b981;
  }
  .price {
    color: #6b7280;
    font-size: 1.1rem;
  }
  button {
    margin-top: 0.5rem;
    padding: 0.5rem 1rem;
    cursor: pointer;
  }
</style>
