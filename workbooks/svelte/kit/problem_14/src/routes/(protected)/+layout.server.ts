import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals, url }) => {
  // TODO: if !locals.user, redirect to /login with ?from= current path
  // TODO: return { user: locals.user }
};
