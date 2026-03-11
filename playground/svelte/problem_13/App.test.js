import { render, fireEvent, waitFor } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 13 — Await Blocks', () => {
  it('shows loading state initially', () => {
    const { getByTestId } = render(App);
    expect(getByTestId('loading')).toBeInTheDocument();
    expect(getByTestId('loading').textContent).toContain('Loading joke');
  });

  it('shows joke after promise resolves', async () => {
    const { getByTestId } = render(App);
    await waitFor(() => {
      expect(getByTestId('joke')).toBeInTheDocument();
    }, { timeout: 2000 });
  });

  it('joke text is non-empty', async () => {
    const { getByTestId } = render(App);
    await waitFor(() => {
      const joke = getByTestId('joke');
      expect(joke.textContent.trim().length).toBeGreaterThan(5);
    }, { timeout: 2000 });
  });

  it('loading indicator is gone after resolve', async () => {
    const { getByTestId, queryByTestId } = render(App);
    await waitFor(() => {
      expect(queryByTestId('loading')).toBeNull();
      expect(getByTestId('joke')).toBeInTheDocument();
    }, { timeout: 2000 });
  });

  it('New Joke button exists', async () => {
    const { getByText } = render(App);
    await waitFor(() => {
      expect(getByText('New Joke')).toBeInTheDocument();
    }, { timeout: 2000 });
  });

  it('clicking New Joke shows loading again', async () => {
    const { getByTestId, getByText } = render(App);
    await waitFor(() => getByTestId('joke'), { timeout: 2000 });
    await fireEvent.click(getByText('New Joke'));
    // Should show loading immediately after click
    expect(getByTestId('loading')).toBeInTheDocument();
  });
});
