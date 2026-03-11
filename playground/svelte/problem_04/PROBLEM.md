# Problem 04 — HTML Tags

## Learning Objectives
- Render raw HTML strings safely with `{@html}`
- Understand when (and why) to use it vs plain text interpolation

## Requirements
The component should:
1. Declare a variable `description` containing this HTML string:
   `"This is <strong>bold</strong> and this is <em>italic</em>."`
2. Render the HTML using `{@html description}` inside a `<div class="content">`
3. Also render the same variable with plain `{description}` in a `<div class="raw">` so you can see the difference

## Expected Output
- `.content` shows: "This is **bold** and this is *italic*." (styled)
- `.raw` shows the literal string with `<strong>` visible as text

## Hints
- `{@html someString}` renders the string as actual HTML
- `{someString}` escapes special characters — `<` becomes `&lt;`
- Only use `{@html}` with content you trust! It bypasses XSS protections.
