import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

export const GET: RequestHandler = () => {
  // TODO: return json with { timestamp, visitors, revenue, requests }
  // Add Math.random() to make values change each request so you can see updates
  return json({
    timestamp: new Date().toISOString(),
    // TODO: add visitors, revenue, requests with slight randomness
  });
};
