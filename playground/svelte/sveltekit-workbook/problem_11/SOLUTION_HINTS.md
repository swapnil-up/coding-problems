## Hints

- Import: `import { error } from '@sveltejs/kit'`
- Usage: `throw error(404, 'Not found')` — must be thrown, not returned
- In `+error.svelte`: `import { page } from '$app/state'`
- Access: `page.status`, `page.error?.message`
- The closest `+error.svelte` up the directory tree handles the error
