## Hints

- The `handle` hook signature: `async ({ event, resolve }) => { ... return resolve(event); }`
- Always call and return `resolve(event)` — otherwise the request hangs
- `event.cookies.get('name')` reads a cookie
- `event.locals` is typed by `App.Locals` in `app.d.ts`
- Wrap JSON.parse in try/catch in case the cookie value is malformed
