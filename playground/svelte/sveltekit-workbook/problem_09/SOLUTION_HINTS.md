## Hints

- `json(data)` from `'@sveltejs/kit'` sets Content-Type and serializes the response
- `new Response('Not found', { status: 404 })` for manual responses
- In `RequestHandler`, `url` is a `URL` object with `.searchParams`
- On the client side, `fetch` returns a `Response` — call `.json()` to parse it
- Use `$effect(() => { fetchProducts(); })` for the initial load
