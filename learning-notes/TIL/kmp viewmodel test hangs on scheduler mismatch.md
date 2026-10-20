# kmp viewmodel test hangs on scheduler mismatch

Date: 2026-06-05 21:44

---

`viewModelScope` uses `Dispatchers.Main`. In a test, `Dispatchers.setMain(StandardTestDispatcher())` creates a dispatcher with its own `TestCoroutineScheduler`; `runTest` creates another. The two schedulers do not advance each other, so `advanceUntilIdle()` never runs the ViewModel's coroutines and the test hangs.

Share the scheduler:

```kotlin
@Test
fun testThing() = runTest {
    Dispatchers.setMain(StandardTestDispatcher(testScheduler))
    // ...
}

@AfterTest
fun tearDown() {
    Dispatchers.resetMain()
}
```

Alternatives:

- `UnconfinedTestDispatcher()` for eager execution in simple tests.
- Inject the dispatcher into the ViewModel instead of hardcoding `Dispatchers.Main`.

A `viewModelScope` that collects a never-ending `StateFlow` can also hang `runTest`; use `backgroundScope` for those collectors or add a test timeout.
