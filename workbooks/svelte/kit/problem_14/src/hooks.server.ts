import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
  // TODO: read 'session' cookie
  // TODO: parse it as { name, role } and set event.locals.user
  // TODO: wrap in try/catch, default to null

  event.locals.user = null; // remove this line when done

  return resolve(event);
};
