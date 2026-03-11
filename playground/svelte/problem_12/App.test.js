import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 12 — Each Blocks', () => {
  it('renders 4 tasks initially', () => {
    const { container } = render(App);
    expect(container.querySelectorAll('.task')).toHaveLength(4);
  });

  it('each task has a title', () => {
    const { getByText } = render(App);
    expect(getByText('Design mockup')).toBeInTheDocument();
    expect(getByText('Write tests')).toBeInTheDocument();
    expect(getByText('Deploy app')).toBeInTheDocument();
    expect(getByText('Review PR')).toBeInTheDocument();
  });

  it('each task has a priority', () => {
    const { getAllByText } = render(App);
    expect(getAllByText('high').length).toBe(2);
    expect(getAllByText('medium').length).toBe(1);
    expect(getAllByText('low').length).toBe(1);
  });

  it('tasks have 1-based index labels', () => {
    const { container } = render(App);
    const indexes = container.querySelectorAll('.index');
    expect(indexes[0].textContent).toContain('1');
    expect(indexes[3].textContent).toContain('4');
  });

  it('Shuffle button exists', () => {
    const { getByText } = render(App);
    expect(getByText('Shuffle')).toBeInTheDocument();
  });

  it('after shuffle all 4 tasks are still present', async () => {
    const { getByText, container } = render(App);
    await fireEvent.click(getByText('Shuffle'));
    expect(container.querySelectorAll('.task')).toHaveLength(4);
  });
});
