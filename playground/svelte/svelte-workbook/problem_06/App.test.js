import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 06 — Deep State', () => {
  it('renders an input and Add button', () => {
    const { getByPlaceholderText, getByText } = render(App);
    expect(getByPlaceholderText('New todo...')).toBeInTheDocument();
    expect(getByText('Add')).toBeInTheDocument();
  });

  it('starts with an empty list', () => {
    const { container } = render(App);
    const items = container.querySelectorAll('li');
    expect(items).toHaveLength(0);
  });

  it('adds a todo when clicking Add', async () => {
    const { getByPlaceholderText, getByText, container } = render(App);
    const input = getByPlaceholderText('New todo...');
    await fireEvent.input(input, { target: { value: 'Buy milk' } });
    await fireEvent.click(getByText('Add'));
    const items = container.querySelectorAll('li');
    expect(items).toHaveLength(1);
    expect(items[0].textContent).toContain('Buy milk');
  });

  it('clears the input after adding', async () => {
    const { getByPlaceholderText, getByText } = render(App);
    const input = getByPlaceholderText('New todo...');
    await fireEvent.input(input, { target: { value: 'Buy milk' } });
    await fireEvent.click(getByText('Add'));
    expect(input.value).toBe('');
  });

  it('can add multiple todos', async () => {
    const { getByPlaceholderText, getByText, container } = render(App);
    const input = getByPlaceholderText('New todo...');
    await fireEvent.input(input, { target: { value: 'Task 1' } });
    await fireEvent.click(getByText('Add'));
    await fireEvent.input(input, { target: { value: 'Task 2' } });
    await fireEvent.click(getByText('Add'));
    expect(container.querySelectorAll('li')).toHaveLength(2);
  });

  it('remove button deletes the correct todo', async () => {
    const { getByPlaceholderText, getByText, getAllByText, container } = render(App);
    const input = getByPlaceholderText('New todo...');
    await fireEvent.input(input, { target: { value: 'Keep me' } });
    await fireEvent.click(getByText('Add'));
    await fireEvent.input(input, { target: { value: 'Delete me' } });
    await fireEvent.click(getByText('Add'));

    const removeButtons = getAllByText('Remove');
    await fireEvent.click(removeButtons[1]); // remove "Delete me"

    const items = container.querySelectorAll('li');
    expect(items).toHaveLength(1);
    expect(items[0].textContent).toContain('Keep me');
  });
});
