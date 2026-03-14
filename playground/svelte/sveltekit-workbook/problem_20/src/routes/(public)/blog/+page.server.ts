import type { PageServerLoad } from './$types';
import { postStore } from '$lib/server/posts';

export const load: PageServerLoad = async () => {
  // TODO: return { posts: postStore.published() }
  return { posts: [] };
};
