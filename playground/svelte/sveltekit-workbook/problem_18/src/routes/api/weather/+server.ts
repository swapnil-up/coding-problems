import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
// TODO: import API_KEY and API_BASE_URL from '$env/static/private'

export const GET: RequestHandler = () => {
  // TODO: console.log that you're using the API key (first 4 chars only, for security)
  // TODO: return json with temperature, condition, source (use API_BASE_URL as source)
  return json({ temperature: 0, condition: 'Unknown' });
};
