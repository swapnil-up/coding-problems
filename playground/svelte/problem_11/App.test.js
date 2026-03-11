import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 11 — If/Else Blocks', () => {
  it('starts with red signal', () => {
    const { getByTestId } = render(App);
    expect(getByTestId('signal').textContent).toContain('red');
    expect(getByTestId('message').textContent).toBe('Stop!');
  });

  it('clicking Yellow shows slow down message', async () => {
    const { getByText, getByTestId } = render(App);
    await fireEvent.click(getByText('Yellow'));
    expect(getByTestId('signal').textContent).toContain('yellow');
    expect(getByTestId('message').textContent).toBe('Slow down!');
  });

  it('clicking Green shows go message', async () => {
    const { getByText, getByTestId } = render(App);
    await fireEvent.click(getByText('Green'));
    expect(getByTestId('message').textContent).toBe('Go!');
  });

  it('clicking Red after Green goes back to stop', async () => {
    const { getByText, getByTestId } = render(App);
    await fireEvent.click(getByText('Green'));
    await fireEvent.click(getByText('Red'));
    expect(getByTestId('message').textContent).toBe('Stop!');
  });

  it('renders all three buttons', () => {
    const { getByText } = render(App);
    expect(getByText('Red')).toBeInTheDocument();
    expect(getByText('Yellow')).toBeInTheDocument();
    expect(getByText('Green')).toBeInTheDocument();
  });
});
