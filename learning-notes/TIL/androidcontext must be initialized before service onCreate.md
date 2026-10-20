# androidcontext must be initialized before service onCreate

Date: 2026-06-18 22:51

---

A global `AndroidContext` singleton that is initialized from `MainActivity` is too late when a service starts first. `Service.onCreate()` can construct database, audio, or haptic drivers before the Activity runs, causing an NPE or an uninitialized `lateinit`.

Initialize it in the service before creating any driver:

```kotlin
override fun onCreate() {
    super.onCreate()
    AndroidContext.init(applicationContext)
    startForeground(...)
}
```

Or initialize in `Application.onCreate()` so every entry point shares one initialization order.

Prefer passing `applicationContext` explicitly into drivers over a mutable global. If a global is unavoidable, make it `lateinit` (so the failure is a clear `UninitializedPropertyAccessException`) and initialize it at the earliest process entry point, not in an Activity.
