import { fail, redirect } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';
import { session } from '$lib/session';

export const load: PageServerLoad = async () => {
  // If already logged in, redirect to dashboard
  if (session.isLoggedIn()) throw redirect(303, '/dashboard');
  return {};
};

export const actions: Actions = {
  login: async ({ request, url }) => {
    const data = await request.formData();
    const password = data.get('password') as string;

    // TODO: if password === 'sveltekit', login and redirect to `from` param or /dashboard
    // TODO: else return fail(401, { error: 'Wrong password. Hint: try "sveltekit"' })
  },

  logout: async () => {
    session.logout();
    throw redirect(303, '/login');
  },
};
