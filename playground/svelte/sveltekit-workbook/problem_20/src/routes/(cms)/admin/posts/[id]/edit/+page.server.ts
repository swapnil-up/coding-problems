import { error, fail } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';
import { postStore } from '$lib/server/posts';

export const load: PageServerLoad = async ({ params }) => {
  const post = postStore.get(params.id);
  if (!post) throw error(404, 'Post not found');
  return { post };
};

export const actions: Actions = {
  update: async ({ request, params }) => {
    const data = await request.formData();
    const title = data.get('title') as string;
    const body = data.get('body') as string;
    const published = data.get('published') === 'on';

    // TODO: validate, call postStore.update, return { success: true }
  },
};
