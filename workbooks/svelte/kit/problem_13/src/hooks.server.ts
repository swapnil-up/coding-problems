import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
  // TODO: log the request method and URL
  // console.log(`--> ${event.request.method} ${event.url.pathname}`);

  // TODO: read cookie 'user', parse it, set event.locals.user
  // const userCookie = event.cookies.get('user');
  // event.locals.user = userCookie ? JSON.parse(userCookie) : null;

  const response = await resolve(event);

  // TODO: log the response status
  // console.log(`<-- ${response.status}`);

  return response;
};
