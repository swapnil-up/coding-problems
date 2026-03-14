## Hints

- Parse JSON body: `const { title, content } = await request.json()`
- Set status on json: `json(data, { status: 201 })`
- Bad request: `new Response('Title required', { status: 400 })`
- No-content response: `new Response(null, { status: 204 })`
- Client-side POST with JSON:
  ```js
  fetch('/api/notes', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, content })
  })
  ```
