import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 14 — DOM Events', () => {
  it('renders a color swatch with initial blue', () => {
    const { container } = render(App);
    const swatch = container.querySelector('.swatch');
    expect(swatch).toBeInTheDocument();
    expect(swatch.style.background).toContain('#3b82f6');
  });

  it('color input updates the swatch', async () => {
    const { container } = render(App);
    const colorInput = container.querySelector('input[type="color"]');
    await fireEvent.input(colorInput, { target: { value: '#ff0000' } });
    const swatch = container.querySelector('.swatch');
    expect(swatch.style.background).toContain('#ff0000');
  });

  it('renders key log list initially empty', () => {
    const { getByTestId } = render(App);
    expect(getByTestId('key-log').querySelectorAll('li')).toHaveLength(0);
  });

  it('pressing a key adds it to the log', async () => {
    const { getByPlaceholderText, getByTestId } = render(App);
    const input = getByPlaceholderText('Press keys here...');
    await fireEvent.keyDown(input, { key: 'a' });
    const items = getByTestId('key-log').querySelectorAll('li');
    expect(items.length).toBeGreaterThan(0);
    expect(items[0].textContent).toBe('a');
  });

  it('pressing multiple keys logs them all', async () => {
    const { getByPlaceholderText, getByTestId } = render(App);
    const input = getByPlaceholderText('Press keys here...');
    await fireEvent.keyDown(input, { key: 'h' });
    await fireEvent.keyDown(input, { key: 'i' });
    const items = getByTestId('key-log').querySelectorAll('li');
    expect(items.length).toBe(2);
  });

  it('log resets after 5 keys and starts fresh', async () => {
    const { getByPlaceholderText, getByTestId } = render(App);
    const input = getByPlaceholderText('Press keys here...');
    for (const k of ['a','b','c','d','e']) {
      await fireEvent.keyDown(input, { key: k });
    }
    expect(getByTestId('key-log').querySelectorAll('li')).toHaveLength(5);
    await fireEvent.keyDown(input, { key: 'f' });
    // After 6th key, should reset to just [f]
    const items = getByTestId('key-log').querySelectorAll('li');
    expect(items).toHaveLength(1);
    expect(items[0].textContent).toBe('f');
  });
});
