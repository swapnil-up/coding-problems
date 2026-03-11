# Problem 20 — Final Project: Shopping Cart

## Learning Objectives
This problem combines everything you've learned:
- Components & props
- Reactive state (`$state`, `$derived`)
- Effects
- Each blocks (keyed)
- If/else blocks
- Bindings
- Events & callbacks
- Classes & styles
- Transitions

## Requirements

### App.svelte (orchestrator)
1. Declare `cart` as `$state([])` — array of `{ id, name, price, qty }`
2. Declare `coupon` as `$state('')`
3. `$derived`: `subtotal` = sum of price*qty
4. `$derived`: `discount` = if coupon === 'SVELTE10', subtotal * 0.1, else 0
5. `$derived`: `total` = subtotal - discount
6. `$effect`: when `cart` changes, log `"Cart updated: {cart.length} items"` to a `cartLog` state array
7. Import and use `ProductCard` and `CartSummary` components

### ProductCard.svelte
- Props: `id`, `name`, `price`, `onAddToCart`
- Renders a card with name, price, and "Add to Cart" button
- The button calls `onAddToCart({ id, name, price })`
- Has class `in-cart` when the product is already in cart (prop: `inCart` boolean)

### CartSummary.svelte
- Props: `cart`, `coupon`, `subtotal`, `discount`, `total`, `onRemove`, `onUpdateQty`, `onCouponChange`
- Renders the cart items with qty controls (+ / - buttons)
- Renders coupon input bound via `onCouponChange` callback
- Renders subtotal, discount (only if > 0), and total
- Each item has a "Remove" button

### Products data (in App.svelte)
```js
const products = [
  { id: 1, name: 'Keyboard', price: 79.99 },
  { id: 2, name: 'Mouse', price: 39.99 },
  { id: 3, name: 'Monitor', price: 299.99 },
  { id: 4, name: 'Webcam', price: 59.99 },
];
```

### Add to Cart logic
- If product already in cart, increase qty by 1
- If not, add with qty: 1

### Remove from cart: filter by id

### Update qty: find item by id and set qty (minimum 1)

## Test IDs needed
- `data-testid="subtotal"` — in CartSummary
- `data-testid="total"` — in CartSummary
- `data-testid="discount"` — in CartSummary (only render when discount > 0)
- `data-testid="cart-count"` — in App (shows number of unique items)
- `data-testid="coupon-input"` — the coupon input
- `data-testid="cart-log"` — in App, showing cart change log entries

## Hints
- Keep App.svelte as the source of truth; pass everything down as props
- Break the problem into small pieces: get ProductCard working first, then CartSummary
- The coupon input in CartSummary uses `oninput={(e) => onCouponChange(e.target.value)}`
- Add transitions to cart items for a polished feel
