import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions: Actions = {
  default: async ({ request }) => {
    const data = await request.formData();
    const username = data.get('username') as string;
    const email = data.get('email') as string;
    const password = data.get('password') as string;
    const confirmPassword = data.get('confirmPassword') as string;

    const errors: Record<string, string> = {};
    const values = { username, email }; // don't send passwords back

    // TODO: validate username (required, 3-20 chars)
    // if (!username || username.length < 3) errors.username = '...'

    // TODO: validate email (required, must contain @)

    // TODO: validate password (required, min 8 chars)

    // TODO: validate confirmPassword matches password

    // TODO: if errors exist, return fail(422, { errors, values })

    // TODO: on success, return { success: true, username }
  },
};
