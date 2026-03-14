import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch, depends }) => {
  // TODO: call depends('app:stats') to register this load as depending on that key
  // TODO: fetch '/api/stats' and return the data
  return {};
};
