import { render } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 04 — HTML Tags', () => {
  it('renders .content div with parsed HTML', () => {
    const { container } = render(App);
    const content = container.querySelector('.content');
    expect(content).toBeInTheDocument();
    expect(content.querySelector('strong')).toBeInTheDocument();
    expect(content.querySelector('em')).toBeInTheDocument();
  });

  it('.content strong element says "bold"', () => {
    const { container } = render(App);
    const strong = container.querySelector('.content strong');
    expect(strong.textContent).toBe('bold');
  });

  it('.content em element says "italic"', () => {
    const { container } = render(App);
    const em = container.querySelector('.content em');
    expect(em.textContent).toBe('italic');
  });

  it('renders .raw div with escaped text (no parsed elements)', () => {
    const { container } = render(App);
    const raw = container.querySelector('.raw');
    expect(raw).toBeInTheDocument();
    // Should not contain actual strong/em elements
    expect(raw.querySelector('strong')).toBeNull();
    expect(raw.querySelector('em')).toBeNull();
    // Should contain the literal tag text
    expect(raw.textContent).toContain('<strong>');
  });
});
