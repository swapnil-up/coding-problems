# compose textfield cursor jumps with async state

Date: 2026-06-12 20:41

---

Binding a `TextField` directly to ViewModel state that round-trips asynchronously can reset the cursor on every keystroke. The field emits a new value, the ViewModel saves and re-emits state, and Compose receives a value that no longer matches its internal edit buffer.

Keep the immediate value local and debounce the write:

```kotlin
var localValue by remember(value) { mutableStateOf(value) }
var job by remember { mutableStateOf<Job?>(null) }

TextField(
    value = localValue,
    onValueChange = {
        localValue = it
        job?.cancel()
        job = scope.launch {
            delay(400)
            onValueChange(it)
        }
    },
)
```

Sync from the ViewModel only when the field is not being edited (for example on focus loss), or key `remember` on a stable field identity rather than the changing value. Without local state, every async round-trip fights the cursor.

Test by typing quickly, then pausing, then typing again; cursor jumps often only appear after the first debounce completes.
