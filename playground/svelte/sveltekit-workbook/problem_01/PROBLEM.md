# Problem 01 — Your First Page

## What you'll learn
- How SvelteKit uses the filesystem as a router
- The `+page.svelte` file convention
- Basic page structure and the `<svelte:head>` tag

## Context
In SvelteKit, every route is a folder inside `src/routes/`.
A `+page.svelte` file renders the page UI for that route.

## Tasks

### 1. Fix the homepage (`src/routes/+page.svelte`)
The page is mostly empty. Make it:
- Show an `<h1>` with the text "Welcome to my SvelteKit app"
- Show a `<p>` with any description
- Use `<svelte:head>` to set the page `<title>` to "Home"

### 2. Create an About page
Create the file `src/routes/about/+page.svelte` with:
- An `<h1>` saying "About"
- A back link: `<a href="/">← Home</a>`
- Page title set to "About"

### 3. Add nav to both pages
On the homepage, add a link: `<a href="/about">About</a>`

## Run it
```bash
npm install && npm run dev
```
Visit http://localhost:5173 and http://localhost:5173/about

## What to observe
- No router config needed — the file structure IS the router
- Clicking the links does client-side navigation (no full reload)
- Each page has its own `<title>` in the browser tab
