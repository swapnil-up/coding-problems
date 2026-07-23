export type Post = {
  id: string;
  slug: string;
  title: string;
  body: string;
  author: string;
  publishedAt: string;
  published: boolean;
};

let posts: Post[] = [
  {
    id: '1',
    slug: 'welcome',
    title: 'Welcome to the Blog',
    body: 'This is the first post. SvelteKit makes building full-stack apps a joy.',
    author: 'Admin',
    publishedAt: '2025-01-01',
    published: true,
  },
  {
    id: '2',
    slug: 'sveltekit-forms',
    title: 'SvelteKit Form Actions',
    body: 'Form actions are one of the killer features of SvelteKit. No API routes needed for mutations.',
    author: 'Admin',
    publishedAt: '2025-01-15',
    published: true,
  },
  {
    id: '3',
    slug: 'draft-post',
    title: 'Draft: Upcoming Features',
    body: 'This post is not published yet.',
    author: 'Admin',
    publishedAt: '2025-02-01',
    published: false,
  },
];

function slugify(title: string): string {
  return title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}

export const postStore = {
  all: () => posts,
  published: () => posts.filter((p) => p.published),
  get: (id: string) => posts.find((p) => p.id === id),
  getBySlug: (slug: string) => posts.find((p) => p.slug === slug),
  create: (data: { title: string; body: string; published: boolean }) => {
    const post: Post = {
      id: Date.now().toString(),
      slug: slugify(data.title),
      title: data.title,
      body: data.body,
      author: 'Admin',
      publishedAt: new Date().toISOString().slice(0, 10),
      published: data.published,
    };
    posts = [...posts, post];
    return post;
  },
  update: (id: string, data: Partial<Omit<Post, 'id' | 'slug' | 'author'>>) => {
    posts = posts.map((p) => (p.id === id ? { ...p, ...data } : p));
    return posts.find((p) => p.id === id)!;
  },
  delete: (id: string) => {
    posts = posts.filter((p) => p.id !== id);
  },
};
