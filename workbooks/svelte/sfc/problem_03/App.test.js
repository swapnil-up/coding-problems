import { render } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 03 — Nested Components', () => {
  it('renders a .grid container', () => {
    const { container } = render(App);
    const grid = container.querySelector('.grid');
    expect(grid).toBeInTheDocument();
  });

  it('renders exactly 3 card elements', () => {
    const { container } = render(App);
    const cards = container.querySelectorAll('.card');
    expect(cards).toHaveLength(3);
  });

  it('each card contains the expected text', () => {
    const { getAllByText } = render(App);
    const texts = getAllByText('I am a Card component!');
    expect(texts).toHaveLength(3);
  });

  it('cards are inside the grid container', () => {
    const { container } = render(App);
    const grid = container.querySelector('.grid');
    const cards = grid.querySelectorAll('.card');
    expect(cards).toHaveLength(3);
  });
});
