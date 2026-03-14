import type { PageServerLoad } from './$types';

const products: Record<string, { name: string; price: number }> = {
  '1': { name: 'Keyboard', price: 79.99 },
  '2': { name: 'Mouse', price: 39.99 },
  '3': { name: 'Monitor', price: 299.99 },
};

export const load: PageServerLoad = async ({ params }) => {
  // TODO: look up products[params.id]
  // TODO: return { product } — for now if not found, return { product: null }
};
