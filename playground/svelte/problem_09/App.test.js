import { render } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 09 — Props', () => {
  it('renders two user cards', () => {
    const { container } = render(App);
    expect(container.querySelectorAll('.user-card')).toHaveLength(2);
  });

  it('renders Alice card with correct data', () => {
    const { getByText } = render(App);
    expect(getByText('Alice')).toBeInTheDocument();
    expect(getByText('Engineer')).toBeInTheDocument();
  });

  it('renders Bob card with correct data', () => {
    const { getByText } = render(App);
    expect(getByText('Bob')).toBeInTheDocument();
    expect(getByText('Designer')).toBeInTheDocument();
  });

  it('each card has an img with correct alt', () => {
    const { container } = render(App);
    const imgs = container.querySelectorAll('img');
    expect(imgs).toHaveLength(2);
    const alts = Array.from(imgs).map(img => img.getAttribute('alt'));
    expect(alts).toContain('Alice');
    expect(alts).toContain('Bob');
  });

  it('imgs have correct src attributes', () => {
    const { container } = render(App);
    const imgs = container.querySelectorAll('img');
    const srcs = Array.from(imgs).map(img => img.getAttribute('src'));
    expect(srcs.some(s => s.includes('alice'))).toBe(true);
    expect(srcs.some(s => s.includes('bob'))).toBe(true);
  });
});
