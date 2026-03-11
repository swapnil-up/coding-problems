<script>
  let items = $state([
    { name: 'Apple', price: 1.5, qty: 2 },
    { name: 'Bread', price: 2.5, qty: 1 },
    { name: 'Milk', price: 1.0, qty: 3 }
  ]);

  // TODO: declare `total` using $derived — sum of price * qty for each item
  // let total = $derived(...)

  // TODO: declare `itemCount` using $derived — sum of all qty values
  // let itemCount = $derived(...)
</script>

<!-- TODO: render a table with columns: Name, Price, Qty, Subtotal, and an Add button -->
<!-- Each row should show item data and a button to increase qty by 1 -->

<!-- TODO: <p data-testid="total">Total: ${total.toFixed(2)}</p> -->
<!-- TODO: <p data-testid="item-count">Items: {itemCount}</p> -->
