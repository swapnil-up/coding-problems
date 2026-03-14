import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { products } from '$lib/products';

export const GET: RequestHandler = ({ url }) => {
  // TODO: read url.searchParams.get('category')
  // TODO: filter products if category is provided
  // TODO: return json(result)
};
