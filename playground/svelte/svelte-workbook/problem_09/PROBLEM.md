# Problem 09 — Props

## Learning Objectives
- Declare component props using `$props()`
- Pass data from parent to child
- Access individual props by destructuring

## Requirements
1. `UserCard.svelte` should accept props: `name`, `role`, and `avatarUrl`
2. It renders a card showing all three values
3. `App.svelte` should render two `<UserCard>` instances with different data:
   - `{ name: "Alice", role: "Engineer", avatarUrl: "https://i.pravatar.cc/50?u=alice" }`
   - `{ name: "Bob", role: "Designer", avatarUrl: "https://i.pravatar.cc/50?u=bob" }`

## Hints
- In Svelte 5: `let { name, role, avatarUrl } = $props();`
- Pass props like HTML attributes: `<UserCard name="Alice" role="Engineer" avatarUrl="..." />`
- Props flow one way: parent → child
