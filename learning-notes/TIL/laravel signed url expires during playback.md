# laravel signed url expires during playback

Date: 2026-04-29 06:07

---

A short-lived signed URL can expire before a video finishes streaming. The player fetches the URL, starts playback, and later requests byte ranges; once the expiry passes, those requests return `403 Forbidden`.

Typical causes:

- `temporarySignedRoute(..., now()->addMinute())` is too short for buffering and seeking.
- The URL is generated once and reused for the whole session.
- A proxy or different host/port changes the URL signature validation.

Fix by using a TTL that covers the expected watch time, or refresh the URL before expiry:

```php
$url = URL::temporarySignedRoute(
    'video.stream',
    now()->addHours(2),
    ['video' => $video->id]
);
```

If the frontend handles heartbeats, return a fresh signed URL from the heartbeat endpoint and swap it into the player before the old one expires. Also ensure `APP_KEY` is identical across app instances; a mismatched key produces `Invalid signature` rather than an expiry error.
