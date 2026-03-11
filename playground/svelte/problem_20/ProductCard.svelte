<script>
  // TODO: destructure props: id, name, price, inCart, onAddToCart
  // let { id, name, price, inCart, onAddToCart } = $props();
</script>

<!-- TODO: render a div.product-card with:
     - class:in-cart={inCart}
     - <h3> with name
     - <p class="price"> with formatted price e.g. "$79.99"
     - <button> "Add to Cart" that calls onAddToCart({ id, name, price })
       - Change button text to "Add Again" if inCart
-->

<style>
  .product-card {
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
    transition: border-color 0.2s;
  }
  .product-card.in-cart {
    border-color: #10b981;
  }
  .price { color: #6b7280; font-size: 1.1rem; }
  button { margin-top: 0.5rem; padding: 0.5rem 1rem; cursor: pointer; }
</style>
