import { render } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 01 — Hello Svelte', () => {
  it('renders an h1 with "Hello, World!"', () => {
    const { getByRole } = render(App);
    const heading = getByRole('heading', { level: 1 });
    expect(heading).toBeInTheDocument();
    expect(heading.textContent).toBe('Hello, World!');
  });

  it('renders a paragraph with the learning message', () => {
    const { getByText } = render(App);
    expect(getByText('I am learning Svelte.')).toBeInTheDocument();
  });

  it('h1 has rebeccapurple color applied via a style tag', () => {
    const { container } = render(App);
    // Check a <style> tag exists in the component (scoped styles inject into DOM)
    const h1 = container.querySelector('h1');
    expect(h1).toBeInTheDocument();
    // We verify the style rule exists in the document
    const styleSheets = Array.from(document.styleSheets);
    const hasRule = styleSheets.some(sheet => {
      try {
        return Array.from(sheet.cssRules || []).some(rule =>
          rule.cssText && rule.cssText.includes('rebeccapurple')
        );
      } catch { return false; }
    });
    expect(hasRule).toBe(true);
  });
});
