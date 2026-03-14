## Hints

- Import from `$lib` alias: `import { posts, getPost } from '$lib/posts'`
- `load` must return a plain serializable object (no classes, functions, etc.)
- TypeScript: the return type of your load function determines `PageData` automatically
- `data.posts` in the page has the exact shape you returned from `load`
