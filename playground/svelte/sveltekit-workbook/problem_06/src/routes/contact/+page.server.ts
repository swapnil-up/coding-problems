import type { Actions } from './$types';

export const actions: Actions = {
  default: async ({ request }) => {
    const data = await request.formData();

    // TODO: extract 'name' and 'email' from data
    // const name = data.get('name') as string;
    // const email = ...

    // TODO: return { success: true, name }
  },
};
