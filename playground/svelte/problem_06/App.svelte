<script>
  let todos = $state([]);
  let newTodo = $state("");

  function addTodo() {
    todos.push({ text: newTodo, done: false });
    newTodo = "";
  }

  function removeTodo(index) {
    todos.splice(index, 1);
  }
</script>

<input bind:value={newTodo} placeholder="New todo..." />
<button onclick={addTodo}>Add</button>

<ul>
  {#each todos as todo, i}
    <li>
      <p>{todo.text}</p>
      <button onclick={() => removeTodo(i)}>Remove</button>
    </li>
  {/each}
</ul>
