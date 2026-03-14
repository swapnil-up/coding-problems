import { render } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 10 — Prop Defaults & Spread', () => {
  it('renders at least 3 badges', () => {
    const { container } = render(App);
    expect(container.querySelectorAll('.badge').length).toBeGreaterThanOrEqual(3);
  });

  it('renders "New" badge with color green', () => {
    const { container } = render(App);
    const badges = Array.from(container.querySelectorAll('.badge'));
    const newBadge = badges.find(b => b.textContent.trim() === 'New');
    expect(newBadge).toBeDefined();
    expect(newBadge.getAttribute('data-color')).toBe('green');
  });

  it('"New" badge uses default size "medium"', () => {
    const { container } = render(App);
    const badges = Array.from(container.querySelectorAll('.badge'));
    const newBadge = badges.find(b => b.textContent.trim() === 'New');
    expect(newBadge.getAttribute('data-size')).toBe('medium');
  });

  it('"Hot" badge has color red and size large', () => {
    const { container } = render(App);
    const badges = Array.from(container.querySelectorAll('.badge'));
    const hotBadge = badges.find(b => b.textContent.trim() === 'Hot');
    expect(hotBadge).toBeDefined();
    expect(hotBadge.getAttribute('data-color')).toBe('red');
    expect(hotBadge.getAttribute('data-size')).toBe('large');
  });

  it('"Draft" badge uses default color "gray" and size "medium"', () => {
    const { container } = render(App);
    const badges = Array.from(container.querySelectorAll('.badge'));
    const draftBadge = badges.find(b => b.textContent.trim() === 'Draft');
    expect(draftBadge).toBeDefined();
    expect(draftBadge.getAttribute('data-color')).toBe('gray');
    expect(draftBadge.getAttribute('data-size')).toBe('medium');
  });
});
