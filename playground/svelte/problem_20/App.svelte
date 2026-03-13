<script>
  import { untrack } from "svelte";
  import CartSummary from "./CartSummary.svelte";
  import ProductCard from "./ProductCard.svelte";

  const products = [
    { id: 1, name: "Keyboard", price: 79.99 },
    { id: 2, name: "Mouse", price: 39.99 },
    { id: 3, name: "Monitor", price: 299.99 },
    { id: 4, name: "Webcam", price: 59.99 },
  ];

  let cart = $state([]);
  let coupon = $state("");
  let cartLog = $state([]);

  let subtotal = $derived(
    cart.reduce((sum, item) => sum + item.qty * item.price, 0),
  );
  let discount = $derived(coupon === "SVELTE10" ? subtotal * 0.1 : 0);
  let total = $derived(subtotal - discount);
  $effect(() => {
    const count = cart.length;
    if (count>0){
      untrack(() => {
        cartLog = [...cartLog, `Cart updated: ${count} items`];
      });
    }
  });

  function addToCart(item) {
    const index = cart.findIndex((product) => product.id === item.id);
    if (index !== -1) {
      cart[index].qty += 1;
      cart = [...cart];
    } else {
      cart = [...cart, { ...item, qty: 1 }];
    }
  }

  function removeFromCart(id) {
    cart = cart.filter((cartItem) => cartItem.id !== id);
  }

  function updateQty(id, qty) {
    if (qty < 1) return;
    const index = cart.findIndex((p) => p.id === id);
    if (index !== -1) {
      cart[index].qty = qty;
      cart = [...cart];
    }
  }
</script>

<main>
  <h1>Tech Shop</h1>

  <span data-testid="cart-count">Show total item count: {cart.length}</span>

  <section class="products">
    {#each products as product}
      <ProductCard
        {...product}
        inCart={cart.some((c) => c.id === product.id)}
        onAddToCart={addToCart}
      />
    {/each}
  </section>

  <CartSummary
    {cart}
    {coupon}
    {subtotal}
    {discount}
    {total}
    onRemove={removeFromCart}
    onUpdateQty={updateQty}
    onCouponChange={(v) => (coupon = v)}
  />

  <ul data-testid="cart-log">
    {#each cartLog as entry}
      <li>{entry}</li>
    {/each}
  </ul>
</main>

<style>
  main {
    max-width: 900px;
    margin: 0 auto;
    padding: 1rem;
  }
  .products {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
  }
</style>
