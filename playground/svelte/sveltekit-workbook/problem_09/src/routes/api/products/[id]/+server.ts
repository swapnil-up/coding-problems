import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { products } from '$lib/products';

export const GET: RequestHandler = ({ params }) => {
  // TODO: parse params.id as a number
  // TODO: find the product
  // TODO: return json(product) or 404
  let id = Number(params.id)
  const product = products.find(item => item.id == id)
  if (product) return json(product)
  else return new Response('Not found', {status:404})
};
