import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 15 — Component Events / Callback Props', () => {
  it('renders 5 star buttons', () => {
    const { container } = render(App);
    const stars = container.querySelectorAll('.stars button');
    expect(stars).toHaveLength(5);
  });

  it('shows "No rating yet" initially', () => {
    const { getByTestId } = render(App);
    expect(getByTestId('rating').textContent).toContain('No rating yet');
  });

  it('clicking a star updates the rating display', async () => {
    const { container, getByTestId } = render(App);
    const stars = container.querySelectorAll('.stars button');
    await fireEvent.click(stars[2]); // 3rd star = rating 3
    expect(getByTestId('rating').textContent).toContain('3/5');
  });

  it('clicking star 5 shows 5/5', async () => {
    const { container, getByTestId } = render(App);
    const stars = container.querySelectorAll('.stars button');
    await fireEvent.click(stars[4]);
    expect(getByTestId('rating').textContent).toContain('5/5');
  });

  it('stars up to rating have active class', async () => {
    const { container } = render(App);
    const stars = container.querySelectorAll('.stars button');
    await fireEvent.click(stars[2]); // rating 3
    const activeStars = container.querySelectorAll('.stars button.active');
    expect(activeStars).toHaveLength(3);
  });

  it('can change rating by clicking different star', async () => {
    const { container, getByTestId } = render(App);
    const stars = container.querySelectorAll('.stars button');
    await fireEvent.click(stars[4]); // 5
    await fireEvent.click(stars[1]); // 2
    expect(getByTestId('rating').textContent).toContain('2/5');
  });
});
