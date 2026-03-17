<script lang="ts">
  import { enhance } from '$app/forms';
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<h1>Todos</h1>

<!-- Add todo form -->
<!-- TODO: set action="?/create" and add use:enhance -->
<form method="POST" use:enhance action="?/create">
  <input type="text" name="text" placeholder="New todo..." required />
  <button type="submit">Add</button>
</form>

<!-- Todo list -->
<ul>
  {#each data.todos as todo (todo.id)}
    <li class:done={todo.done}>
      <span>{todo.text}</span>

      <!-- Toggle form -->
      <!-- TODO: set action="?/toggle", add use:enhance, add hidden input name="id" value={todo.id} -->
      <form method="POST" use:enhance action="?/toggle">
        <input type="hidden" name="id" value={todo.id}>
        <button type="submit">{todo.done ? 'Undo' : 'Done'}</button>
      </form>

      <!-- Delete form -->
      <!-- TODO: set action="?/delete", add use:enhance, add hidden input name="id" value={todo.id} -->
      <form method="POST" use:enhance action="?/delete">
      <input type="hidden" name="id" value={todo.id}>
        <button type="submit">Delete</button>
      </form>
    </li>
  {/each}
</ul>

<style>
  ul { list-style: none; padding: 0; max-width: 500px; }
  li { display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem 0; border-bottom: 1px solid #e2e8f0; }
  li span { flex: 1; }
  li.done span { text-decoration: line-through; color: #94a3b8; }
  form { display: contents; }
  input[type="text"] { flex: 1; padding: 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; }
</style>
