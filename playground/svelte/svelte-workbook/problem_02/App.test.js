import { render } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';
import path from 'path';
import { fileURLToPath } from 'url';

describe('Problem 02 — Dynamic Attributes', () => {
  it('renders an img with the correct src', () => {
    const { container } = render(App);
    const img = container.querySelector('img');
    expect(img).toBeInTheDocument();
    expect(img.getAttribute('src')).toBe('https://picsum.photos/200');
  });

  it('img has alt attribute set to the name variable', () => {
    const { container } = render(App);
    const img = container.querySelector('img');
    expect(img.getAttribute('alt')).toBe('A random photo');
  });

  it('renders a caption paragraph with the name', () => {
    const { getByText } = render(App);
    expect(getByText('A random photo')).toBeInTheDocument();
  });

  it('component source uses shorthand {src} syntax', async () => {
    // Read the source file to verify shorthand usage
    const fs = await import('fs');

    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    const source = fs.readFileSync(path.resolve(__dirname, './App.svelte'), 'utf-8');
    // Should contain {src} shorthand, not src={src}
    expect(source).toMatch(/\{src\}/);
  });
});
