import type { PageServerLoad } from './$types';
import { posts } from '$lib/posts';

// TODO: export prerender = true

export const load: PageServerLoad = async () => {
  return { posts };
};
