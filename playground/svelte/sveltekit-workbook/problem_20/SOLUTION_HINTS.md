## Hints — work through this in order

### 1. Start with auth (hooks + login)
Get the cookie/session flow working first. Everything else depends on it.
Test: visit /admin without logging in → should redirect to /login.

### 2. Then the public blog
Load and display posts — no auth needed. Test the 404 on an invalid slug.

### 3. Then the CMS list
Show all posts in the admin, wire up the delete action.

### 4. Then new post form
Validation + creation + redirect to edit.

### 5. Finally edit post
Pre-fill form with existing data, wire up the update action.

### Common gotchas
- Route groups `(public)` and `(cms)` don't affect URLs — `/admin` not `/(cms)/admin`
- `published` checkbox: `data.get('published') === 'on'` (checkboxes send 'on' or nothing)
- Always `throw redirect(...)`, never `return redirect(...)`
- Layout data merges — `data.user` from the CMS layout is available in all CMS pages
