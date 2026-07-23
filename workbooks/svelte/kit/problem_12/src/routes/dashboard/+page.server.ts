import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { session } from '$lib/session';

export const load: PageServerLoad = async () => {
  // TODO: if not logged in, redirect to /login?from=/dashboard
  // if (!session.isLoggedIn()) throw redirect(303, '/login?from=/dashboard')

  return { username: 'Alice' };
};
