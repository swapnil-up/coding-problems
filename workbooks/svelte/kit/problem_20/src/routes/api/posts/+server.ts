import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { postStore } from '$lib/server/posts';

export const GET: RequestHandler = () => {
  // TODO: return json of all published posts
  return json([]);
};
