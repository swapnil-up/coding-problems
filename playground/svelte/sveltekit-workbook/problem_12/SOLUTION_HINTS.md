## Hints

- `throw redirect(303, '/path')` — must be thrown inside load/actions
- After a POST action, use 303 (not 301/302) to redirect to a GET
- For permanent redirects use 301; for temporary use 302/303
- Don't wrap redirect in try/catch — it throws intentionally
- `url.searchParams.get('from')` reads query params in actions
