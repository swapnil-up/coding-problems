# Problem 04 — Page Load Data

## What you'll learn
- `+page.server.ts` and the `load` function
- Fetching/querying data server-side
- Receiving `data` in the page component via props
- The difference between `+page.server.ts` (server only) and `+page.ts` (universal)

## Context
`src/lib/posts.ts` has a fake data store with posts and a `getPost()` helper.
Your job is to wire up two routes:
1. `/posts` — list all posts
2. `/posts/[slug]` — show a single post

## Tasks

### 1. Posts list (`src/routes/posts/+page.server.ts`)
Write a `load` function that:
- Imports `posts` from `$lib/posts`
- Returns `{ posts }`

### 2. Posts list page (`src/routes/posts/+page.svelte`)
- Receive `data` from props
- Render each post as a link: `<a href="/posts/{post.slug}">{post.title}</a>`
- Show the author and date under each title

### 3. Post detail (`src/routes/posts/[slug]/+page.server.ts`)
Write a `load` function that:
- Gets `params.slug`
- Calls `getPost(params.slug)`
- Returns `{ post }` (handle missing post as `null` for now)

### 4. Post detail page (`src/routes/posts/[slug]/+page.svelte`)
- Display the post title, author, date, and body
- Show "Post not found" if `data.post` is null
- Add a back link to `/posts`

## Run it
```bash
npm install && npm run dev
```
Navigate to /posts and click through to individual posts.

## Key insight
`load` in `+page.server.ts` ONLY runs on the server — never in the browser.
This is where you safely access databases, secrets, and server-only logic.
