<script>
  // TODO: destructure props:
  // cart, coupon, subtotal, discount, total, onRemove, onUpdateQty, onCouponChange
</script>

<!-- TODO: render a div.cart-summary -->
<!-- If cart is empty, show <p>Your cart is empty</p> -->
<!-- Otherwise show: -->
<!--   - keyed each over cart items with qty controls (- qty + and Remove button) -->
<!--   - coupon input with data-testid="coupon-input" -->
<!--   - <p data-testid="subtotal">Subtotal: ${subtotal.toFixed(2)}</p> -->
<!--   - {#if discount > 0} <p data-testid="discount">Discount: -${discount.toFixed(2)}</p> {/if} -->
<!--   - <p data-testid="total">Total: ${total.toFixed(2)}</p> -->

<style>
  .cart-summary { border: 1px solid #e5e7eb; border-radius: 8px; padding: 1rem; }
  .cart-item { display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem 0; border-bottom: 1px solid #f3f4f6; }
  .item-name { flex: 1; }
  .qty-controls { display: flex; align-items: center; gap: 0.25rem; }
</style>
