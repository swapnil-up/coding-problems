import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { products } from '$lib/products';

export const GET: RequestHandler = ({ url }) => {
  let productList = products
  const category = url.searchParams.get('category')
  if (category) {
    productList = products.filter(items=>items.category==category)}  
    return json(productList)
  // TODO: filter products if category is provided
  // TODO: return json(result)
};
