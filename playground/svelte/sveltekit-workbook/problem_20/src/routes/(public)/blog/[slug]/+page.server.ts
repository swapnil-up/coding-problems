import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { postStore } from '$lib/server/posts';

export const load: PageServerLoad = async ({ params }) => {
  // TODO: get post by slug, throw error(404) if not found or not published
  // return { post }
  return { post: null };
};
