# Problem 10 — API Routes (POST, DELETE)

## What you'll learn
- `POST` and `DELETE` handlers in `+server.ts`
- Parsing JSON request bodies
- RESTful API patterns in SvelteKit
- Calling your own API from a `+page.svelte` client

## What you're building
A notes CRUD API:
- `GET /api/notes` — list all notes
- `POST /api/notes` — create a note (JSON body: `{ title, content }`)
- `DELETE /api/notes/[id]` — delete a note

And a frontend page that uses this API.

## Tasks

### 1. Fix `src/routes/api/notes/+server.ts`
Export two handlers:

**`GET`**: return `json(notesStore.all())`

**`POST`**: 
- Parse JSON body: `const body = await request.json()`
- Validate that `title` and `content` exist
- Call `notesStore.create(title, content)`
- Return `json(newNote, { status: 201 })`
- Return a 400 error if validation fails

### 2. Fix `src/routes/api/notes/[id]/+server.ts`
Export a `DELETE` handler:
- Check the note exists, 404 if not
- Call `notesStore.delete(params.id)`
- Return `new Response(null, { status: 204 })`

### 3. Fix `src/routes/+page.svelte`
Wire up the create form and delete buttons to call the API using `fetch`.

## Run it
```bash
npm install && npm run dev
```

## Key insight
`+server.ts` endpoints are your escape hatch for full HTTP control.
They're also useful for webhooks, file uploads, and anything that doesn't fit the form-action pattern.
