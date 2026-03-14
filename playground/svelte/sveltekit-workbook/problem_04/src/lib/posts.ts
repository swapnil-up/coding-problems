// Simulated data store — in real life this would be a DB query
export type Post = {
  slug: string;
  title: string;
  author: string;
  date: string;
  body: string;
};

export const posts: Post[] = [
  {
    slug: 'hello-sveltekit',
    title: 'Hello SvelteKit',
    author: 'Alice',
    date: '2025-01-10',
    body: 'SvelteKit is an opinionated framework built on top of Svelte...',
  },
  {
    slug: 'load-functions',
    title: 'Understanding Load Functions',
    author: 'Bob',
    date: '2025-01-15',
    body: 'Load functions run on the server and pass data to pages...',
  },
  {
    slug: 'form-actions',
    title: 'Form Actions in Practice',
    author: 'Alice',
    date: '2025-01-20',
    body: 'Form actions let you handle form submissions without an API route...',
  },
];

export function getPost(slug: string): Post | undefined {
  return posts.find((p) => p.slug === slug);
}
