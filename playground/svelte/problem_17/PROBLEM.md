# Problem 17 — Classes & Styles

## Learning Objectives
- Conditionally apply CSS classes with `class:name={condition}`
- Apply inline styles with `style:property={value}`
- Use component-level CSS with scoped styles

## Requirements
Build a notification card system:
1. Declare `notifications` as `$state` with:
   ```js
   [
     { id: 1, type: 'success', message: 'File saved!', dismissed: false },
     { id: 2, type: 'error', message: 'Upload failed.', dismissed: false },
     { id: 3, type: 'info', message: 'New version available.', dismissed: false },
   ]
   ```
2. Render each as `<div class="notification">` with:
   - `class:success={notification.type === 'success'}`
   - `class:error={notification.type === 'error'}`
   - `class:info={notification.type === 'info'}`
   - `class:dismissed={notification.dismissed}`
   - `style:opacity={notification.dismissed ? '0.4' : '1'}`
3. Each notification has a "Dismiss" button that sets `dismissed: true`
4. Add a "Reset All" button that sets all `dismissed` to false

## Hints
- `class:foo={condition}` adds class "foo" when condition is truthy
- `style:opacity="0.5"` sets the opacity style inline
- Multiple `class:` directives can coexist on the same element
