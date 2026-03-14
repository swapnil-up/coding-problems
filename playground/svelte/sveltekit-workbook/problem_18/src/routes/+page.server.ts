import type { PageServerLoad } from './$types';
// TODO: import PUBLIC_APP_NAME from '$env/static/public'

export const load: PageServerLoad = async () => {
  // TODO: return { appName: PUBLIC_APP_NAME }
  return { appName: 'App' };
};
