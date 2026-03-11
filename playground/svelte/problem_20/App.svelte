<script>
  // TODO: import ProductCard and CartSummary

  const products = [
    { id: 1, name: 'Keyboard', price: 79.99 },
    { id: 2, name: 'Mouse', price: 39.99 },
    { id: 3, name: 'Monitor', price: 299.99 },
    { id: 4, name: 'Webcam', price: 59.99 },
  ];

  // TODO: declare `cart` as $state([])
  // TODO: declare `coupon` as $state('')
  // TODO: declare `cartLog` as $state([])

  // TODO: $derived subtotal
  // TODO: $derived discount (10% if coupon === 'SVELTE10', else 0)
  // TODO: $derived total

  // TODO: $effect to push "Cart updated: N items" to cartLog when cart changes

  function addToCart(product) {
    // TODO: if product already in cart (by id), increase qty
    // else add { ...product, qty: 1 }
  }

  function removeFromCart(id) {
    // TODO: filter cart
  }

  function updateQty(id, qty) {
    // TODO: find item and set qty (minimum 1)
  }
</script>

<main>
  <h1>Tech Shop</h1>

  <!-- TODO: cart count badge <span data-testid="cart-count"> -->

  <section class="products">
    <!-- TODO: {#each products as product}
         <ProductCard
           {...product}
           inCart={cart.some(c => c.id === product.id)}
           onAddToCart={addToCart}
         />
         {/each}
    -->
  </section>

  <!-- TODO: <CartSummary
       {cart} {coupon} {subtotal} {discount} {total}
       onRemove={removeFromCart}
       onUpdateQty={updateQty}
       onCouponChange={(v) => coupon = v}
  /> -->

  <!-- TODO: <ul data-testid="cart-log"> showing each log entry </ul> -->
</main>

<style>
  main { max-width: 900px; margin: 0 auto; padding: 1rem; }
  .products { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 1rem; margin: 1rem 0; }
</style>
