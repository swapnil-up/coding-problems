## Hints

- `import { page, navigating } from '$app/state'`
- `page.url.pathname` is the current path string
- `page.params` is an object of dynamic route params
- `navigating` is null when not navigating, has `from`/`to` when in progress
- Active link: `class:active={page.url.pathname === '/users/1'}`
- Breadcrumb path building:
  ```js
  const parts = page.url.pathname.split('/').filter(Boolean);
  const segments = parts.map((label, i) => ({
    label,
    href: '/' + parts.slice(0, i + 1).join('/')
  }));
  ```
