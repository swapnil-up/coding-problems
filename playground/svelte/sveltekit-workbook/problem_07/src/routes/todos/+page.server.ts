import type { Actions, PageServerLoad } from './$types';
import { todosStore } from '$lib/todos';

export const load: PageServerLoad = async () => {
  return { todos: todosStore.all() };
};

export const actions: Actions = {
  create: async ({ request }) => {
    const data = await request.formData();
    // TODO: get 'text' from data and call todosStore.add(text)
  },

  delete: async ({ request }) => {
    const data = await request.formData();
    // TODO: get 'id' from data and call todosStore.remove(id)
  },

  toggle: async ({ request }) => {
    const data = await request.formData();
    // TODO: get 'id' from data and call todosStore.toggle(id)
  },
};
