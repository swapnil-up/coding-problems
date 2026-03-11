import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 07 — Derived State', () => {
  it('renders initial total correctly (1.5*2 + 2.5*1 + 1.0*3 = 8.5)', () => {
    const { getByTestId } = render(App);
    expect(getByTestId('total').textContent).toContain('8.50');
  });

  it('renders initial item count correctly (2+1+3 = 6)', () => {
    const { getByTestId } = render(App);
    expect(getByTestId('item-count').textContent).toContain('6');
  });

  it('renders all three items in the table', () => {
    const { getByText } = render(App);
    expect(getByText('Apple')).toBeInTheDocument();
    expect(getByText('Bread')).toBeInTheDocument();
    expect(getByText('Milk')).toBeInTheDocument();
  });

  it('clicking add on Apple row updates total', async () => {
    const { getAllByText, getByTestId } = render(App);
    // Click the first "Add" button (Apple row)
    const addButtons = getAllByText(/add/i);
    await fireEvent.click(addButtons[0]);
    // Apple qty goes from 2 to 3, so total becomes 1.5*3 + 2.5*1 + 1.0*3 = 10.0
    expect(getByTestId('total').textContent).toContain('10.00');
  });

  it('clicking add updates item count', async () => {
    const { getAllByText, getByTestId } = render(App);
    const addButtons = getAllByText(/add/i);
    await fireEvent.click(addButtons[0]);
    // 3+1+3 = 7
    expect(getByTestId('item-count').textContent).toContain('7');
  });
});
