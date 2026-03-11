import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 20 — Shopping Cart (Final Project)', () => {
  // --- Product Cards ---
  it('renders 4 product cards', () => {
    const { container } = render(App);
    expect(container.querySelectorAll('.product-card')).toHaveLength(4);
  });

  it('shows all product names', () => {
    const { getByText } = render(App);
    expect(getByText('Keyboard')).toBeInTheDocument();
    expect(getByText('Mouse')).toBeInTheDocument();
    expect(getByText('Monitor')).toBeInTheDocument();
    expect(getByText('Webcam')).toBeInTheDocument();
  });

  it('initially cart count is 0', () => {
    const { getByTestId } = render(App);
    expect(getByTestId('cart-count').textContent).toContain('0');
  });

  // --- Adding to cart ---
  it('clicking Add to Cart adds item', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    expect(getByTestId('cart-count').textContent).toContain('1');
  });

  it('adding same product again increments qty not count', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    await fireEvent.click(getAllByText(/Add (to Cart|Again)/)[0]);
    // Still 1 unique item
    expect(getByTestId('cart-count').textContent).toContain('1');
  });

  it('product card gets in-cart class after adding', async () => {
    const { getAllByText, container } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    const cards = container.querySelectorAll('.product-card');
    expect(cards[0].classList.contains('in-cart')).toBe(true);
  });

  // --- Cart summary ---
  it('subtotal updates when item is added', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]); // Keyboard $79.99
    expect(getByTestId('subtotal').textContent).toContain('79.99');
  });

  it('adding two products updates subtotal', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]); // Keyboard 79.99
    await fireEvent.click(getAllByText('Add to Cart')[1]); // Mouse 39.99
    // 79.99 + 39.99 = 119.98
    expect(getByTestId('subtotal').textContent).toContain('119.98');
  });

  // --- Qty controls ---
  it('+ button increases qty and updates subtotal', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]); // Keyboard 79.99 qty=1
    const plusButtons = getAllByText('+');
    await fireEvent.click(plusButtons[0]); // qty=2 → 159.98
    expect(getByTestId('subtotal').textContent).toContain('159.98');
  });

  it('- button decreases qty, minimum 1', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    const plusButtons = getAllByText('+');
    await fireEvent.click(plusButtons[0]); // qty=2
    const minusButtons = getAllByText('-');
    await fireEvent.click(minusButtons[0]); // qty=1
    await fireEvent.click(minusButtons[0]); // still qty=1 (min)
    expect(getByTestId('subtotal').textContent).toContain('79.99');
  });

  // --- Remove ---
  it('Remove button removes item from cart', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    await fireEvent.click(getAllByText('Remove')[0]);
    expect(getByTestId('cart-count').textContent).toContain('0');
  });

  // --- Coupon ---
  it('coupon input exists', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    expect(getByTestId('coupon-input')).toBeInTheDocument();
  });

  it('SVELTE10 coupon applies 10% discount', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]); // Keyboard 79.99
    const couponInput = getByTestId('coupon-input');
    await fireEvent.input(couponInput, { target: { value: 'SVELTE10' } });
    // discount = 7.999... ≈ 8.00, total = 71.99
    expect(getByTestId('discount')).toBeInTheDocument();
    expect(getByTestId('total').textContent).toContain('71.99');
  });

  it('invalid coupon shows no discount', async () => {
    const { getAllByText, getByTestId, queryByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    const couponInput = getByTestId('coupon-input');
    await fireEvent.input(couponInput, { target: { value: 'INVALID' } });
    expect(queryByTestId('discount')).toBeNull();
  });

  // --- Effect / Log ---
  it('cart log updates when items are added', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    const log = getByTestId('cart-log');
    expect(log.textContent).toContain('Cart updated');
  });
});
