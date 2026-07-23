## Hints

- `request.formData()` returns a `FormData` object — use `.get('fieldname')` to read values
- Cast to string: `data.get('name') as string`
- The `actions` default function must return something or nothing — returning `{ success: true }` makes it available as `form` in the page
- Add `use:enhance` as an attribute: `<form method="POST" use:enhance>`
- `form` prop is `null` on first load, then populated after submission
