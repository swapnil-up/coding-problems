# Problem 18 — Environment Variables

## What you'll learn
- `$env/static/private` — server-only env vars, inlined at build time
- `$env/dynamic/private` — server-only env vars, read at runtime
- `$env/static/public` — public env vars (VITE_ or PUBLIC_ prefixed)
- `$env/dynamic/public` — public env vars, runtime

## Context
SvelteKit has four env modules. Choosing the right one matters:
- **private**: Never exposed to the browser (API keys, DB passwords)
- **public**: Safe for the browser
- **static**: Inlined at build time (can be tree-shaken)
- **dynamic**: Read at runtime (needed for containerized deployments)

## Setup
Create a `.env` file in `problem_18/`:
```
API_KEY=my-secret-key-12345
API_BASE_URL=https://api.example.com
PUBLIC_APP_NAME=Weather App
PUBLIC_FEATURE_FLAG=true
```

## Tasks

### 1. Fix `src/routes/api/weather/+server.ts`
- Import `API_KEY` from `$env/static/private`
- Import `API_BASE_URL` from `$env/static/private`
- The handler should return a fake weather response, but log that it's "using key: {API_KEY.slice(0,4)}..."
- Return `json({ temperature: 22, condition: 'Sunny', source: API_BASE_URL })`

### 2. Fix `src/routes/+page.server.ts`
- Import `PUBLIC_APP_NAME` from `$env/static/public`
- Return `{ appName: PUBLIC_APP_NAME }` so the page can show it

### 3. Fix `src/routes/+page.svelte`
- Import `PUBLIC_FEATURE_FLAG` from `$env/static/public`
- Show a "Beta Feature" section only if `PUBLIC_FEATURE_FLAG === 'true'`
- Show `data.appName` in the heading
- Fetch `/api/weather` and show the result

## Run it
```bash
npm install && npm run dev
```

## Key insight
NEVER import from `$env/*/private` in a `.svelte` file or `+page.ts` (universal load).
Private env only works in `+page.server.ts`, `+layout.server.ts`, `+server.ts`, and `hooks.server.ts`.
SvelteKit will throw a build error if you try.
