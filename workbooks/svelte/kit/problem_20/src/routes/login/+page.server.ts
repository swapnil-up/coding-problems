import { fail, redirect } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
  // TODO: if already logged in, redirect to /admin
  return {};
};

export const actions: Actions = {
  login: async ({ request, cookies, url }) => {
    const data = await request.formData();
    const password = data.get('password') as string;
    // TODO: check password === 'cms-password'
    // TODO: on success: set 'session' cookie with { name: 'Admin' }, redirect to from ?? /admin
    // TODO: on failure: return fail(401, { error: 'Wrong password' })
  },

  logout: async ({ cookies }) => {
    // TODO: delete session cookie, redirect to /login
  },
};
