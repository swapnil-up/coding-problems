## Hints

- Import syntax: `import { API_KEY } from '$env/static/private'`
- Public vars: `import { PUBLIC_APP_NAME } from '$env/static/public'`
- Private vars CANNOT be imported in:
  - `+page.svelte` / any `.svelte` file
  - `+page.ts` (universal load — runs in browser too)
  - Client-side code
- If you forget `.env`, SvelteKit throws: "API_KEY is not defined in .env"
- `$env/dynamic/private` is for runtime env vars (e.g. set in Docker/Vercel at deploy time)
