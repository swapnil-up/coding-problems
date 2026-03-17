import type { PageServerLoad } from './$types';
import { getPost } from '$lib/posts';

export const load: PageServerLoad = async ({ params }) => {
  const post = getPost(params.slug) ?? null
  return {post}
  // TODO: import getPost from $lib/posts
  // TODO: look up the post by params.slug
  // TODO: return { post }
};
