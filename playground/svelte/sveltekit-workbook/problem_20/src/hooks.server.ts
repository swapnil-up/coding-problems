import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
  // TODO: read 'session' cookie, parse JSON, set event.locals.user
  // Default to null if no cookie or parse error
  event.locals.user = null;
  return resolve(event);
};
