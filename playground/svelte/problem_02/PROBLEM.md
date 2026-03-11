# Problem 02 — Dynamic Attributes

## Learning Objectives
- Set HTML attributes dynamically using `{}`
- Use the shorthand `{src}` instead of `src={src}` when name matches
- Understand accessibility attributes

## Requirements
The component should:
1. Declare a variable `src` set to `"https://picsum.photos/200"`
2. Declare a variable `name` set to `"A random photo"`
3. Render an `<img>` tag that uses `src` for its `src` attribute and `name` for its `alt` attribute
4. Use the **shorthand** syntax for `src` (just `{src}`, not `src={src}`)
5. Display a caption `<p>` below the image showing the name

## Example Output
An image loaded from picsum with alt text "A random photo" and a caption below.

## Hints
- `<img src={src}>` can be shortened to `<img {src}>` when the attribute name matches the variable name
- You cannot use shorthand for `alt` here since the variable is called `name`, not `alt`
- Dynamic attributes use the same `{}` syntax as text interpolation
