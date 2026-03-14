# Svelte Workbook — Basic Svelte Practice

A hands-on workbook covering everything in the **Basic Svelte** tutorial. Each problem has broken/incomplete code for you to fix, plus a test file to verify your solution.

## Prerequisites

- You've read the Basic Svelte tutorial at https://svelte.dev/tutorial
- Node.js 18+ installed

## Setup

```bash
npm install
```

This installs Vitest + @testing-library/svelte used across all problems.

## Running Tests

**Single problem:**
```bash
npm test -- problem_01
```

**All problems:**
```bash
npm test
```

**Watch mode while you work:**
```bash
npm run test:watch -- problem_05
```

## Running server
```bash
npx vite
```
For the specific file change the file path in the main.js

## Problem List

| # | Topic | Concepts |
|---|-------|----------|
| 01 | Hello Svelte | Components, markup, script, style |
| 02 | Dynamic Attributes | `{}` interpolation, dynamic attrs, shorthand |
| 03 | Nested Components | Importing & using child components |
| 04 | HTML Tags | `{@html}` tag |
| 05 | Reactive State | `$state`, updating variables, reactivity |
| 06 | Deep State | `$state` with objects and arrays |
| 07 | Derived State | `$derived` |
| 08 | Effects | `$effect` |
| 09 | Props | `$props()`, passing data down |
| 10 | Prop Defaults & Spread | Default values, spread props |
| 11 | If / Else Blocks | `{#if}`, `{:else}`, `{:else if}` |
| 12 | Each Blocks | `{#each}`, keyed each |
| 13 | Await Blocks | `{#await}` |
| 14 | DOM Events | `onclick`, `oninput`, event handlers |
| 15 | Component Events | Callback props pattern |
| 16 | Bindings | `bind:value`, `bind:checked`, `bind:group` |
| 17 | Classes & Styles | `class:`, `style:`, component styles |
| 18 | Transitions | `transition:`, `in:`, `out:` |
| 19 | Key Blocks | `{#key}` |
| 20 | Final Project | Shopping cart — combines everything |

## How to Work Through Problems

1. Read `PROBLEM.md` in each folder — it explains what to do
2. Edit the `.svelte` file(s) — look for `// TODO` comments
3. Run the tests: `npm test -- problem_XX`
4. Fix until all tests pass
5. Move to the next problem

Good luck!
