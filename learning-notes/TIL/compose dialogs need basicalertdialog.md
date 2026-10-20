# compose dialogs need basicalertdialog

Date: 2026-06-02 07:06

---

A hand-rolled overlay (`Box` + `Surface` + `Column(verticalScroll)`) can render with unbounded constraints, so `verticalScroll` doesn't scroll and the dialog can be clipped. It also sits in normal z-order, so it may appear under other content.

Use the Material3 dialog primitive and put dialog conditionals after the main content:

```kotlin
BasicAlertDialog(onDismissRequest = onDismiss) {
    Surface(Modifier.fillMaxWidth()) {
        Column(
            Modifier
                .verticalScroll(rememberScrollState())
                .padding(24.dp)
        ) { /* ... */ }
    }
}
```

`BasicAlertDialog` uses `Dialog` from `compose.ui.window`, which creates a separate window layer with bounded constraints. Don't put `heightIn` on the scrolling column; constrain the Surface instead.
