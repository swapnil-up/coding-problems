# Problem 07 — Derived State

## Learning Objectives
- Use `$derived()` to compute values that automatically update when their dependencies change
- Understand the difference between `$state` (mutable) and `$derived` (read-only computed)

## Requirements
Build a cart summary:
1. Declare `items` as `$state` with these initial values:
   ```js
   [
     { name: 'Apple', price: 1.5, qty: 2 },
     { name: 'Bread', price: 2.5, qty: 1 },
     { name: 'Milk', price: 1.0, qty: 3 }
   ]
   ```
2. Use `$derived` to compute `total` — the sum of `price * qty` for all items
3. Use `$derived` to compute `itemCount` — the sum of all `qty` values
4. Render a table showing each item's name, price, qty, and subtotal (price*qty)
5. Render `<p data-testid="total">` showing the total
6. Render `<p data-testid="item-count">` showing the item count
7. Add a button per row to increase that item's qty by 1 — watch derived values update!

## Hints
- `let total = $derived(items.reduce(...))` 
- `$derived` recalculates whenever its referenced `$state` changes
- You can't assign to a `$derived` variable directly
