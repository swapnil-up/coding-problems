<script>
  let {
    cart,
    coupon,
    subtotal,
    discount,
    total,
    onRemove,
    onUpdateQty,
    onCouponChange,
  } = $props();
</script>

<div class="cart-summary">
  {#if cart.length === 0}
    <p>Your cart is empty</p>
  {:else}
    {#each cart as item (item.id)}
      <div class="cart-item">
        <span>{item.name}</span>
        <button onclick={() => onUpdateQty(item.id, item.qty - 1)}>-</button>
        <span>{item.qty}</span>
        <button onclick={() => onUpdateQty(item.id, item.qty + 1)}>+</button>
        <button onclick={() => onRemove(item.id)}>Remove</button>
      </div>
    {/each}
    <input
      type="text"
      data-testid="coupon-input"
      oninput={(e) => onCouponChange(e.target.value)}
      placeholder="Coupon code"
    />
    <p data-testid="subtotal">Subtotal: ${subtotal.toFixed(2)}</p>
    {#if discount > 0}
      <p data-testid="discount">Discount: ${discount.toFixed(2)}</p>
    {/if}
    <p data-testid="total">Total: ${total.toFixed(2)}</p>
  {/if}
</div>

<style>
  .cart-summary {
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 1rem;
  }
  .cart-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 0;
    border-bottom: 1px solid #f3f4f6;
  }
  .item-name {
    flex: 1;
  }
  .qty-controls {
    display: flex;
    align-items: center;
    gap: 0.25rem;
  }
</style>
