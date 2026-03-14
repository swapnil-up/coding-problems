import { fail, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions: Actions = {
  login: async ({ request, cookies, url }) => {
    const data = await request.formData();
    const password = data.get('password') as string;

    if (password !== 'admin123') {
      return fail(401, { error: 'Wrong password. Hint: admin123' });
    }

    // TODO: set 'session' cookie with JSON { name: 'Admin', role: 'admin' }
    // cookies.set('session', JSON.stringify({ name: 'Admin', role: 'admin' }), { path: '/' })

    const from = url.searchParams.get('from') ?? '/dashboard';
    throw redirect(303, from);
  },

  logout: async ({ cookies }) => {
    // TODO: delete 'session' cookie
    throw redirect(303, '/login');
  },
};
