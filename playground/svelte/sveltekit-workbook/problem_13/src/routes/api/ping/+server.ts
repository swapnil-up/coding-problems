import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

export const GET: RequestHandler = ({ locals }) => {
  // TODO: return json({ message: 'pong', user: locals.user })
  return json({ message: 'pong' });
};
