# Problem 12 — Each Blocks

## Learning Objectives
- Use `{#each}` to render lists
- Use keyed each `{#each items as item (item.id)}` for efficient DOM updates
- Access loop index with `{#each items as item, i}`

## Requirements
Build a task board:
1. Declare `tasks` as `$state` with these items:
   ```js
   [
     { id: 1, title: 'Design mockup', priority: 'high' },
     { id: 2, title: 'Write tests', priority: 'medium' },
     { id: 3, title: 'Deploy app', priority: 'low' },
     { id: 4, title: 'Review PR', priority: 'high' },
   ]
   ```
2. Render each task as a `<div class="task">` containing:
   - `<span class="title">` with the title
   - `<span class="priority">` with the priority
   - `<span class="index">` showing its 1-based position (e.g. "#1")
3. Use a **keyed** each block: `{#each tasks as task (task.id)}`
4. Add a "Shuffle" button that randomly reorders the tasks array
5. After shuffling, the `#1, #2...` indexes should update to reflect new positions

## Hints
- Keyed each: `{#each items as item (item.id)}`
- Loop index: `{#each items as item, i (item.id)}` — i is 0-based
- Shuffle: `tasks = [...tasks].sort(() => Math.random() - 0.5)`
