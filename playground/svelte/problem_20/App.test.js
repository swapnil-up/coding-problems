import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';
import { tick } from 'svelte'
import { beforeAll } from 'vitest';

beforeAll(() => {
  if (!Element.prototype.animate) {
    Element.prototype.animate = () => ({
      finished: Promise.resolve(),
      cancel: () => { },
      play: () => { },
      pause: () => { },
    });
  }
});

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
    await tick();
    expect(getByTestId('cart-count').textContent).toContain('1');
  });

  it('adding same product again increments qty not count', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    await tick();
    await fireEvent.click(getAllByText(/Add (to Cart|Again)/)[0]);
    await tick();
    // Still 1 unique item
    expect(getByTestId('cart-count').textContent).toContain('1');
  });

  it('product card gets in-cart class after adding', async () => {
    const { getAllByText, container } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    await tick();
    const cards = container.querySelectorAll('.product-card');
    expect(cards[0].classList.contains('in-cart')).toBe(true);
  });

  // --- Cart summary ---
  it('subtotal updates when item is added', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]); // Keyboard $79.99
    await tick();
    expect(getByTestId('subtotal').textContent).toContain('79.99');
  });

  // Instead of querying 'Add to Cart' twice, grab all 4 buttons before any clicks
  it('adding two products updates subtotal', async () => {
    const { getAllByText, getByTestId } = render(App);
    const addButtons = getAllByText('Add to Cart'); // grab all 4 upfront
    await fireEvent.click(addButtons[0]); // Keyboard 79.99
    await tick();
    await fireEvent.click(addButtons[1]); // Mouse 39.99 — same reference, still valid
    await tick();
    expect(getByTestId('subtotal').textContent).toContain('119.98');
  });

  // --- Qty controls ---
  it('+ button increases qty and updates subtotal', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]); // Keyboard 79.99 qty=1
    await tick();
    const plusButtons = getAllByText('+');
    await fireEvent.click(plusButtons[0]); // qty=2 → 159.98
    await tick();
    expect(getByTestId('subtotal').textContent).toContain('159.98');
  });

  it('- button decreases qty, minimum 1', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    await tick();
    const plusButtons = getAllByText('+');
    await fireEvent.click(plusButtons[0]); // qty=2
    await tick();
    const minusButtons = getAllByText('-');
    await fireEvent.click(minusButtons[0]); // qty=1
    await tick();
    await fireEvent.click(minusButtons[0]); // still qty=1 (min)
    await tick();
    expect(getByTestId('subtotal').textContent).toContain('79.99');
  });

  // --- Remove ---
  it('Remove button removes item from cart', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    await tick();
    await fireEvent.click(getAllByText('Remove')[0]);
    await tick();
    expect(getByTestId('cart-count').textContent).toContain('0');
  });

  // --- Coupon ---
  it('coupon input exists', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    await tick();
    expect(getByTestId('coupon-input')).toBeInTheDocument();
  });

  it('SVELTE10 coupon applies 10% discount', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]); // Keyboard 79.99
    await tick();
    const couponInput = getByTestId('coupon-input');
    await fireEvent.input(couponInput, { target: { value: 'SVELTE10' } });
    await tick();
    // discount = 7.999... ≈ 8.00, total = 71.99
    expect(getByTestId('discount')).toBeInTheDocument();
    expect(getByTestId('total').textContent).toContain('71.99');
  });

  it('invalid coupon shows no discount', async () => {
    const { getAllByText, getByTestId, queryByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    await tick();
    const couponInput = getByTestId('coupon-input');
    await fireEvent.input(couponInput, { target: { value: 'INVALID' } });
    await tick();
    expect(queryByTestId('discount')).toBeNull();
  });

  // --- Effect / Log ---
  it('cart log updates when items are added', async () => {
    const { getAllByText, getByTestId } = render(App);
    await fireEvent.click(getAllByText('Add to Cart')[0]);
    await tick();
    const log = getByTestId('cart-log');
    expect(log.textContent).toContain('Cart updated');
  });
});
