# Problem 06 — Deep State

## Learning Objectives
- Use `$state` with objects and arrays
- Mutate nested state (Svelte 5 tracks deep mutations with Proxy)
- Understand that you can push/splice arrays directly with `$state`

## Requirements
Build a simple todo list:
1. Declare `todos` as `$state([])` — an empty array
2. Declare `newTodo` as `$state('')`
3. Add an `<input bind:value={newTodo} placeholder="New todo...">` 
4. Add an "Add" button that pushes `{ text: newTodo, done: false }` to `todos` and clears `newTodo`
5. Render each todo in a `<ul>` as `<li>` items showing the todo text
6. Each `<li>` should have a "Remove" button that removes that item from the array

## Hints
- With Svelte 5's `$state`, you can mutate arrays directly: `todos.push(item)`, `todos.splice(i, 1)`
- An alternative is reassignment: `todos = [...todos, item]` — both work
- Use `{#each todos as todo, i}` to loop with an index
