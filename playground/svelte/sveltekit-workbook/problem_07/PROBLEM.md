# Problem 07 — Named Form Actions

## What you'll learn
- Multiple named actions on a single page: `action="?/create"`, `action="?/delete"`
- How to invoke a specific action with `formaction` attribute
- Loading current data + mutating it via actions (the SvelteKit pattern)

## Context
When a page needs multiple form operations (add, delete, toggle), you define
named actions instead of a single default action.

## What you're building
A todo list where you can:
1. Add todos (action: `create`)
2. Delete todos (action: `delete`)  
3. Toggle todos done/undone (action: `toggle`)

## The data store (`src/lib/todos.ts`) is already written — a simple in-memory array.

## Tasks

### 1. Fix `src/routes/todos/+page.server.ts`
The `load` function is complete. Fill in the three actions:

**`create`**: read `text` from formData, call `todosStore.add(text)`

**`delete`**: read `id` from formData, call `todosStore.remove(id)`

**`toggle`**: read `id` from formData, call `todosStore.toggle(id)`

### 2. Fix `src/routes/todos/+page.svelte`
Three forms already exist but are broken:
- The "add" form needs `action="?/create"` and `use:enhance`
- Each todo needs a delete button with `action="?/delete"` and a hidden `id` input
- Each todo needs a toggle button with `action="?/toggle"` and a hidden `id` input

## Run it
```bash
npm install && npm run dev
```
Add, delete, and toggle todos.

## Key insight
Each form action is a separate POST. The `?/name` syntax routes to the right action.
You can even have a single `<form>` with multiple `<button formaction="?/other">` buttons.
