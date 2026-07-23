import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async () => {
  return { user: { name: 'Alice', email: 'alice@example.com', role: 'admin' } }
};