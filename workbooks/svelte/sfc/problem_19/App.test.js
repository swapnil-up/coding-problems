import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';
import { tick } from 'svelte';

describe('Problem 19 — Key Blocks', () => {
  it('shows the first word "Svelte" initially', () => {
    const { getByText } = render(App);
    expect(getByText('Svelte')).toBeInTheDocument();
  });

  it('shows "1 / 5" info initially', () => {
    const { getByTestId } = render(App);
    expect(getByTestId('info').textContent).toContain('1 / 5');
  });

  it('Next button advances to second word', async () => {
    const { getByText, getByTestId } = render(App);
    await fireEvent.click(getByText('Next'));
    await tick();
    expect(getByTestId('info').textContent).toContain('2 / 5');
    expect(getByText('Reactive')).toBeInTheDocument();
  });

  it('Previous button goes back', async () => {
    const { getByText } = render(App);
    await fireEvent.click(getByText('Next'));
    await fireEvent.click(getByText('Previous'));
    await tick();
    expect(getByText('Svelte')).toBeInTheDocument();
  });

  it('Previous does not go below index 0', async () => {
    const { getByText, getByTestId } = render(App);
    await fireEvent.click(getByText('Previous'));
    await fireEvent.click(getByText('Previous'));
    expect(getByTestId('info').textContent).toContain('1 / 5');
  });

  it('Next does not go above last index', async () => {
    const { getByText, getByTestId } = render(App);
    for (let i = 0; i < 10; i++) await fireEvent.click(getByText('Next'));
    expect(getByTestId('info').textContent).toContain('5 / 5');
    expect(getByText('Fast')).toBeInTheDocument();
  });

  it('uses {#key} block in source', async () => {
    const fs = await import('fs');
    const path = await import('path');

    // Use a string path to avoid the URL object error
    const filePath = path.join(process.cwd(), 'problem_19', 'App.svelte');
    const source = fs.readFileSync(filePath, 'utf-8');

    expect(source).toMatch(/#key/);
  });
});
