# html-to-image blank png from off-screen node

Date: 2026-10-10 23:05

---

`html-to-image` clones the target node into an SVG `<foreignObject>` and rasterizes it. If the node is parked off-screen with `position: fixed; left: -10000px`, the clone keeps that position and the exported PNG is blank.

Pass a style override so only the clone is repositioned:

```ts
const dataUrl = await toPng(node, {
  pixelRatio: 3,
  style: {
    position: "static",
    left: "0",
    top: "0",
    margin: "0",
    transform: "none",
    pointerEvents: "auto",
  },
})
```

The real node can stay off-screen, so there is no visible flicker.

Use a solid background and explicit colors if the export must not inherit dark mode. Verify the output by opening the PNG, not just by checking that `toPng` resolved.
