import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 08 — Effects', () => {
  it('renders the input', () => {
    const { getByPlaceholderText } = render(App);
    expect(getByPlaceholderText('Type to search...')).toBeInTheDocument();
  });

  it('log is empty initially', () => {
    const { getByTestId } = render(App);
    expect(getByTestId('log').querySelectorAll('li')).toHaveLength(0);
  });

  it('typing into input adds to log', async () => {
    const { getByPlaceholderText, getByTestId } = render(App);
    const input = getByPlaceholderText('Type to search...');
    await fireEvent.input(input, { target: { value: 'svelte' } });
    const items = getByTestId('log').querySelectorAll('li');
    expect(items.length).toBeGreaterThan(0);
    expect(items[0].textContent).toContain('svelte');
  });

  it('changing input multiple times adds multiple log entries', async () => {
    const { getByPlaceholderText, getByTestId } = render(App);
    const input = getByPlaceholderText('Type to search...');
    await fireEvent.input(input, { target: { value: 'hello' } });
    await fireEvent.input(input, { target: { value: 'world' } });
    const items = getByTestId('log').querySelectorAll('li');
    expect(items.length).toBeGreaterThanOrEqual(2);
  });

  it('log entries contain "Searched:" prefix', async () => {
    const { getByPlaceholderText, getByTestId } = render(App);
    const input = getByPlaceholderText('Type to search...');
    await fireEvent.input(input, { target: { value: 'test' } });
    const items = getByTestId('log').querySelectorAll('li');
    expect(items[0].textContent).toContain('Searched:');
  });
});
