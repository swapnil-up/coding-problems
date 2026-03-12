<script>
  let items = $state([
    { name: "Apple", price: 1.5, qty: 2 },
    { name: "Bread", price: 2.5, qty: 1 },
    { name: "Milk", price: 1.0, qty: 3 },
  ]);

  let total = $derived(
    items.reduce((sum, item) => sum + item.price * item.qty, 0),
  );
  let itemCount = $derived(items.reduce((sum, item) => sum + item.qty, 0));
</script>

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Price</th>
      <th>Qty</th>
      <th>Subtotal</th>
      <th>Action</th>
    </tr>
  </thead>

  <tbody>
    {#each items as item}
      <tr>
        <td>{item.name}</td>
        <td>${item.price.toFixed(2)}</td>
        <td>{item.qty}</td>
        <td>${(item.price * item.qty).toFixed(2)}</td>
        <td>
          <button onclick={() => (item.qty += 1)}>Add</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>

<p data-testid="total">Total: ${total.toFixed(2)}</p>
<p data-testid="item-count">Items: {itemCount}</p>
