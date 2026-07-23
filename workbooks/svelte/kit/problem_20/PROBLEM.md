# Problem 20 — Final Project: Mini Blog CMS

## What you'll learn
This problem combines EVERYTHING:
- Route groups `(public)` and `(cms)`
- Layouts (public site layout vs CMS layout)
- Server load functions
- Form actions with validation
- API routes
- Auth via hooks + cookies
- Error pages
- `$page` state for active links
- `invalidate()` for data freshness
- Redirects and `error()`

## What you're building
A mini blog CMS with:
- **Public side** (`/blog`, `/blog/[slug]`) — anyone can read
- **CMS side** (`/admin`) — password-protected, manage posts
- **Login page** (`/login`) — auth gate for CMS

## File structure
```
src/
  hooks.server.ts          ← reads session cookie → locals.user
  app.d.ts                 ← Locals type
  lib/
    server/
      posts.ts             ← in-memory post store (already written)
  routes/
    login/                 ← login/logout
    (public)/
      +layout.svelte       ← public nav
      blog/
        +page.server.ts    ← load all posts
        +page.svelte
        [slug]/
          +page.server.ts  ← load single post
          +page.svelte
    (cms)/
      +layout.server.ts    ← auth guard
      +layout.svelte       ← CMS nav with user info
      admin/
        +page.server.ts    ← load posts for management
        +page.svelte       ← post list with delete
        posts/
          new/
            +page.server.ts  ← create action
            +page.svelte
          [id]/edit/
            +page.server.ts  ← load post + update/delete actions
            +page.svelte
    api/
      posts/
        +server.ts         ← GET all posts (public JSON API)
```

## The post store is already written in `src/lib/server/posts.ts`.

## Your tasks (in order of difficulty)

1. **`src/app.d.ts`** — add `Locals.user` type
2. **`src/hooks.server.ts`** — read session cookie, set locals.user
3. **`src/routes/login/+page.server.ts`** — login/logout actions
4. **`src/routes/(cms)/+layout.server.ts`** — auth guard
5. **`src/routes/(public)/blog/+page.server.ts`** — load posts
6. **`src/routes/(public)/blog/[slug]/+page.server.ts`** — load single post
7. **`src/routes/(cms)/admin/+page.server.ts`** — load posts + delete action
8. **`src/routes/(cms)/admin/posts/new/+page.server.ts`** — create action with validation
9. **`src/routes/(cms)/admin/posts/[id]/edit/+page.server.ts`** — load + update action
10. **`src/routes/api/posts/+server.ts`** — public JSON API
11. **All the `.svelte` files** — wire up the UI

## Login password: `cms-password`

## Run it
```bash
npm install && npm run dev
```

Start at `/blog` (public), then try `/admin` (should redirect to login),
then log in and manage posts.

## What "done" looks like
- [ ] Unauthenticated visit to `/admin` redirects to `/login?from=/admin`
- [ ] Login with wrong password shows error
- [ ] Login with correct password goes to `/admin`
- [ ] `/admin` shows post list with delete buttons
- [ ] New post form validates (title + body required)
- [ ] New post appears on `/blog` after creation
- [ ] Edit post loads existing data
- [ ] `/blog/[slug]` shows correct post or 404
- [ ] `GET /api/posts` returns JSON
- [ ] Logout returns to `/login`
