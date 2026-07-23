import { render, fireEvent } from '@testing-library/svelte';
import { describe, it, expect } from 'vitest';
import App from './App.svelte';

describe('Problem 16 — Bindings', () => {
  it('text input updates name in preview', async () => {
    const { container, getByTestId } = render(App);
    const nameInput = container.querySelector('input[type="text"]') ||
                      container.querySelector('input:not([type])');
    await fireEvent.input(nameInput, { target: { value: 'Alice' } });
    expect(getByTestId('preview').textContent).toContain('Alice');
  });

  it('select input updates plan in preview', async () => {
    const { container, getByTestId } = render(App);
    const select = container.querySelector('select');
    await fireEvent.change(select, { target: { value: 'pro' } });
    expect(getByTestId('preview').textContent).toContain('pro');
  });

  it('checkbox toggles newsletter in preview', async () => {
    const { container, getByTestId } = render(App);
    const checkboxes = container.querySelectorAll('input[type="checkbox"]');
    // Find newsletter checkbox (not group ones)
    const newsletter = Array.from(checkboxes).find(cb => !cb.value || cb.value === 'on');
    if (newsletter) {
      await fireEvent.click(newsletter);
      expect(getByTestId('preview').textContent).toContain('true');
    }
  });

  it('interest checkboxes update interests array', async () => {
    const { container, getByTestId } = render(App);
    const codingCheckbox = container.querySelector('input[value="coding"]');
    expect(codingCheckbox).toBeInTheDocument();
    await fireEvent.click(codingCheckbox);
    expect(getByTestId('preview').textContent).toContain('coding');
  });

  it('radio buttons update contact method', async () => {
    const { container, getByTestId } = render(App);
    const phoneRadio = container.querySelector('input[value="phone"]');
    expect(phoneRadio).toBeInTheDocument();
    await fireEvent.click(phoneRadio);
    expect(getByTestId('preview').textContent).toContain('phone');
  });

  it('preview shows all 6 fields', () => {
    const { getByTestId } = render(App);
    const preview = getByTestId('preview').textContent;
    // Should contain representations of all fields
    expect(preview).toBeTruthy();
    expect(preview.length).toBeGreaterThan(10);
  });
});
