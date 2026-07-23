import type { Actions, PageServerLoad } from './$types';
import { postStore } from '$lib/server/posts';

export const load: PageServerLoad = async () => {
  // TODO: return { posts: postStore.all() }
  return { posts: [] };
};

export const actions: Actions = {
  delete: async ({ request }) => {
    const data = await request.formData();
    const id = data.get('id') as string;
    // TODO: call postStore.delete(id)
  },
};
