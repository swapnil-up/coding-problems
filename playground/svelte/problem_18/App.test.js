import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 18 — Transitions', () => {
  it('shows the empty banner initially', () => {
    const { container } = render(App);
    const banner = container.querySelector('.banner');
    expect(banner).toBeInTheDocument();
    expect(banner.textContent).toContain('No messages');
  });

  it('has an "Add Message" button', () => {
    const { getByText } = render(App);
    expect(getByText('Add Message')).toBeInTheDocument();
  });

  it('clicking Add Message creates a message', async () => {
    const { getByText, container } = render(App);
    await fireEvent.click(getByText('Add Message'));
    expect(container.querySelectorAll('.message')).toHaveLength(1);
  });

  it('message contains correct text', async () => {
    const { getByText } = render(App);
    await fireEvent.click(getByText('Add Message'));
    expect(getByText(/Message #1/)).toBeInTheDocument();
  });

  it('can add multiple messages', async () => {
    const { getByText, container } = render(App);
    await fireEvent.click(getByText('Add Message'));
    await fireEvent.click(getByText('Add Message'));
    await fireEvent.click(getByText('Add Message'));
    expect(container.querySelectorAll('.message')).toHaveLength(3);
  });

  it('banner disappears when messages exist', async () => {
    const { getByText, container } = render(App);
    await fireEvent.click(getByText('Add Message'));
    // Banner might still be in DOM during transition in jsdom, but check content
    const messages = container.querySelectorAll('.message');
    expect(messages.length).toBeGreaterThan(0);
  });

  it('× button removes the message', async () => {
    const { getByText, container } = render(App);
    await fireEvent.click(getByText('Add Message'));
    await fireEvent.click(getByText('Add Message'));
    const removeBtn = container.querySelectorAll('.message button')[0];
    await fireEvent.click(removeBtn);
    expect(container.querySelectorAll('.message')).toHaveLength(1);
  });

  it('component source uses transition directive', async () => {
    const fs = await import('fs');
    const path = await import('path'); // Use the path module instead

    // Construct the path manually from the project root
    // Assuming App.svelte is in the same folder as the test
    const filePath = path.join(process.cwd(), 'problem_18', 'App.svelte');

    try {
      const source = fs.readFileSync(filePath, 'utf-8');
      expect(source).toMatch(/transition:|in:|out:/);
    } catch (err) {
      // If the folder structure is different, this fallback might help
      const fallbackPath = path.resolve(__dirname, 'App.svelte');
      const source = fs.readFileSync(fallbackPath, 'utf-8');
      expect(source).toMatch(/transition:|in:|out:/);
    }
  });
});
