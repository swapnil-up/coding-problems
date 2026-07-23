import { fail, redirect } from '@sveltejs/kit';
import type { Actions } from './$types';
import { postStore } from '$lib/server/posts';

export const actions: Actions = {
  default: async ({ request }) => {
    const data = await request.formData();
    const title = data.get('title') as string;
    const body = data.get('body') as string;
    const published = data.get('published') === 'on';

    const errors: Record<string, string> = {};
    // TODO: validate title (required, min 3 chars)
    // TODO: validate body (required, min 10 chars)
    // TODO: if errors, return fail(422, { errors, values: { title, body } })

    const post = postStore.create({ title, body, published });
    throw redirect(303, `/admin/posts/${post.id}/edit`);
  },
};
