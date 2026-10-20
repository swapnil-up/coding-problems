# android foreground service for a reliable timer

Date: 2026-06-03 20:39

---

A timer that must survive screen-off needs more than a coroutine: Doze can delay ticks and the process can be killed.

- `TimerService`: foreground service with a persistent notification, `START_STICKY`, and a `PARTIAL_WAKE_LOCK` around the active timer.
- Create the notification channel on Android 8+; use `Notification.Builder(this, CHANNEL_ID)` on O+ and suppress the deprecated constructor on older APIs.
- Manifest: `FOREGROUND_SERVICE`, `FOREGROUND_SERVICE_DATA_SYNC`, `WAKE_LOCK`, `POST_NOTIFICATIONS`.
- Request `POST_NOTIFICATIONS` at runtime on Android 13+.
- Keep shared code platform-agnostic with a delegate singleton; `MainActivity` supplies the start/stop lambdas.
- Hold `FLAG_KEEP_SCREEN_ON` separately if the screen should stay awake while running.

Release the wake lock in `onDestroy`/when the timer stops; a leaked `PARTIAL_WAKE_LOCK` drains the battery.
