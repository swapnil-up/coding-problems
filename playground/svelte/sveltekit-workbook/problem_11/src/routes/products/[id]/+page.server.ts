import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { products } from '$lib/products';

export const load: PageServerLoad = async ({ params }) => {
  const id = parseInt(params.id);

  // TODO: if isNaN(id), throw error(400, 'Invalid product ID')
  
  const product = products.find((p) => p.id === id);

  // TODO: if !product, throw error(404, 'Product not found')

  return { product };
};
