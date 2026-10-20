# compose bottom bar sinks under navigation bar

Date: 2026-06-08 17:59

---

Applying navigation-bar insets inside a fixed-height row shrinks the content instead of moving the bar:

```kotlin
Row(Modifier.height(64.dp).padding(WindowInsets.navigationBars.asPaddingValues()))
```

Apply the bottom inset to the outer `Surface` (or use `navigationBarsPadding()` there), so the whole bar is lifted above the system bar:

```kotlin
Surface(
    modifier = Modifier
        .fillMaxWidth()
        .padding(bottom = navigationBarBottomDp().dp)
) { Row(Modifier.height(64.dp)) { /* ... */ } }
```

In Compose Multiplatform, `WindowInsets.navigationBars` may report 0 or differ by device. The reliable fix used here was an `expect/actual navigationBarBottomDp()` that reads Android's `navigation_bar_height` resource and returns 0 elsewhere. `Scaffold`'s `innerPadding` is not a substitute for insets on the bottomBar slot.
