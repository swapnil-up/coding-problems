export type Product = { id: number; name: string; price: number; category: string };

export const products: Product[] = [
  { id: 1, name: 'Keyboard', price: 79.99, category: 'peripherals' },
  { id: 2, name: 'Mouse', price: 39.99, category: 'peripherals' },
  { id: 3, name: 'Monitor', price: 299.99, category: 'displays' },
  { id: 4, name: 'Webcam', price: 59.99, category: 'peripherals' },
  { id: 5, name: 'Desk Lamp', price: 29.99, category: 'accessories' },
];
