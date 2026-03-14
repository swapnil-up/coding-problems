import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 17 — Classes & Styles', () => {
  it('renders 3 notifications', () => {
    const { container } = render(App);
    expect(container.querySelectorAll('.notification')).toHaveLength(3);
  });

  it('success notification has success class', () => {
    const { container } = render(App);
    const notifications = container.querySelectorAll('.notification');
    expect(notifications[0].classList.contains('success')).toBe(true);
  });

  it('error notification has error class', () => {
    const { container } = render(App);
    const notifications = container.querySelectorAll('.notification');
    expect(notifications[1].classList.contains('error')).toBe(true);
  });

  it('info notification has info class', () => {
    const { container } = render(App);
    const notifications = container.querySelectorAll('.notification');
    expect(notifications[2].classList.contains('info')).toBe(true);
  });

  it('dismissing a notification adds dismissed class', async () => {
    const { getAllByText, container } = render(App);
    const dismissButtons = getAllByText('Dismiss');
    await fireEvent.click(dismissButtons[0]);
    const notifications = container.querySelectorAll('.notification');
    expect(notifications[0].classList.contains('dismissed')).toBe(true);
  });

  it('dismissed notification has reduced opacity', async () => {
    const { getAllByText, container } = render(App);
    await fireEvent.click(getAllByText('Dismiss')[0]);
    const notification = container.querySelectorAll('.notification')[0];
    expect(notification.style.opacity).toBe('0.4');
  });

  it('Reset All brings dismissed back to false', async () => {
    const { getAllByText, getByText, container } = render(App);
    await fireEvent.click(getAllByText('Dismiss')[0]);
    await fireEvent.click(getAllByText('Dismiss')[1]);
    await fireEvent.click(getByText('Reset All'));
    const dismissed = container.querySelectorAll('.notification.dismissed');
    expect(dismissed).toHaveLength(0);
  });
});
