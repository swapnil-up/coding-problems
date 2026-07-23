import type { PageServerLoad } from './$types';
import { posts } from '$lib/posts';

export const load: PageServerLoad = async () => {
  return {posts}
  // TODO: import posts from $lib/posts and return them
};
