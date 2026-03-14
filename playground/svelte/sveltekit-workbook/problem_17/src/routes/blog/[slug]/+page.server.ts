import type { EntryGenerator, PageServerLoad } from './$types';
import { posts } from '$lib/posts';
import { error } from '@sveltejs/kit';

// TODO: export prerender = true

// TODO: export const entries: EntryGenerator = () => { ... }
// This tells SvelteKit which [slug] values to prerender
// return posts.map(p => ({ slug: p.slug }))

export const load: PageServerLoad = async ({ params }) => {
  const post = posts.find((p) => p.slug === params.slug);
  if (!post) throw error(404, 'Post not found');
  return { post };
};
