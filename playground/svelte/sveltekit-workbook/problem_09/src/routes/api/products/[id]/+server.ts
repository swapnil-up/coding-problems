import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { products } from '$lib/products';

export const GET: RequestHandler = ({ params }) => {
  // TODO: parse params.id as a number
  // TODO: find the product
  // TODO: return json(product) or 404
};
