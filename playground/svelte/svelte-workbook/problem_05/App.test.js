import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 05 — Reactive State', () => {
  it('renders initial count of 0', () => {
    const { getByTestId } = render(App);
    expect(getByTestId('count').textContent).toContain('0');
  });

  it('increment button increases count by 1', async () => {
    const { getByText, getByTestId } = render(App);
    await fireEvent.click(getByText('Increment'));
    expect(getByTestId('count').textContent).toContain('1');
  });

  it('clicking increment multiple times accumulates', async () => {
    const { getByText, getByTestId } = render(App);
    await fireEvent.click(getByText('Increment'));
    await fireEvent.click(getByText('Increment'));
    await fireEvent.click(getByText('Increment'));
    expect(getByTestId('count').textContent).toContain('3');
  });

  it('decrement button decreases count by 1', async () => {
    const { getByText, getByTestId } = render(App);
    await fireEvent.click(getByText('Increment'));
    await fireEvent.click(getByText('Increment'));
    await fireEvent.click(getByText('Decrement'));
    expect(getByTestId('count').textContent).toContain('1');
  });

  it('reset button sets count back to 0', async () => {
    const { getByText, getByTestId } = render(App);
    await fireEvent.click(getByText('Increment'));
    await fireEvent.click(getByText('Increment'));
    await fireEvent.click(getByText('Reset'));
    expect(getByTestId('count').textContent).toContain('0');
  });
});
