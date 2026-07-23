import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals, url }) => {
  // TODO: if !locals.user, redirect to /login?from={url.pathname}
  // TODO: return { user: locals.user }
};
