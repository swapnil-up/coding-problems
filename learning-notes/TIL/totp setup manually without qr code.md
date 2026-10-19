# totp setup manually without qr code

Date: 2026-08-05 12:39

---

If the 2FA QR code won't scan, you don't need it — the **secret** is enough.

**Option 1 — manual entry in the authenticator app**

1. Tap **+** → "Enter a setup key" (or "Manual entry").
2. Account name: anything (e.g. your email).
3. Paste the **secret** shown under the QR.
4. Save — the app starts generating 6-digit codes.

**Option 2 — skip the app**

The secret alone generates TOTP codes (`otpauth://` URI also works). Handy for a
one-off login.

The code rotates every **30 seconds** and is time-based, so the device clock
must be accurate.
