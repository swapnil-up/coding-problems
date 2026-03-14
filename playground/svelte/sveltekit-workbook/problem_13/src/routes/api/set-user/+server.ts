import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

export const POST: RequestHandler = ({ cookies }) => {
  cookies.set('user', JSON.stringify({ name: 'Alice', role: 'admin' }), {
    path: '/',
    httpOnly: false, // allowing JS read for demo
  });
  return json({ ok: true });
};
