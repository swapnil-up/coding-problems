# Problem 03 — Layouts

## What you'll learn
- `+layout.svelte` for shared UI across routes
- Nested layouts — a layout inside a layout
- The `<slot>` / `{@render children()}` pattern

## Context
A `+layout.svelte` file wraps all pages in the same directory (and subdirectories).
The child page renders where you place `{@render children()}` in the layout.

## File structure you're building
```
src/routes/
  +layout.svelte          ← root layout (nav bar for whole site)
  +page.svelte            ← homepage "/"
  dashboard/
    +layout.svelte        ← dashboard layout (sidebar)
    +page.svelte          ← "/dashboard"
    settings/
      +page.svelte        ← "/dashboard/settings"
    profile/
      +page.svelte        ← "/dashboard/profile"
```

## Tasks

### 1. Root layout (`src/routes/+layout.svelte`)
Already has a skeleton — add a `<nav>` with links to `/` and `/dashboard`.
Use `{@render children()}` to render the child page.

### 2. Root page (`src/routes/+page.svelte`)
Simple homepage with an h1 and a "Go to Dashboard" link.

### 3. Dashboard layout (`src/routes/dashboard/+layout.svelte`)
Add a sidebar with links to:
- `/dashboard` → "Overview"  
- `/dashboard/settings` → "Settings"
- `/dashboard/profile` → "Profile"

Use `{@render children()}` for the main content area.

### 4. Fill in the three dashboard pages
Each just needs an `<h1>` with the page name.

## Run it
```bash
npm install && npm run dev
```
Navigate between pages — notice the root nav stays, the sidebar stays within dashboard.

## Key insight
Layouts are **nested**. Dashboard pages get BOTH the root layout AND the dashboard layout wrapping them.
