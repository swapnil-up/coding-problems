# android haptics need vibratormanager fallback

Date: 2026-05-30 22:25

---

A hard cast to `VibratorManager` can crash on devices or OEM builds where the service is missing or not exposed:

```kotlin
// fragile
val manager = context.getSystemService(VibratorManager::class.java)
val vibrator = manager.defaultVibrator
```

Use the API-level split and a fallback:

```kotlin
val vibrator = if (Build.VERSION.SDK_INT >= 31) {
    context.getSystemService(VibratorManager::class.java)?.defaultVibrator
} else {
    @Suppress("DEPRECATION")
    context.getSystemService(Context.VIBRATOR_SERVICE) as? Vibrator
}

if (vibrator?.hasVibrator() == true) {
    vibrator.vibrate(VibrationEffect.createOneShot(300, VibrationEffect.DEFAULT_AMPLITUDE))
}
```

Declare `android.permission.VIBRATE`. Compose's `LocalHapticFeedback` may be silent on some Xiaomi devices, so a platform `VibrationEffect` with a null-safe fallback is more reliable. OEMs may also ignore custom amplitudes; default amplitude is the safer choice.
