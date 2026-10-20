# copying a firefox profile does not bypass cloudflare

Date: 2026-07-21 13:15

---

A Playwright crawler that copies the real Firefox profile still gets the Cloudflare challenge:

```
[Cloudflare] Challenge detected, waiting...
[Cloudflare] Challenge did not pass in time.
```

Profile cookies are not enough when the challenge is bound to IP/browser fingerprint or detects headless mode. Steps that help:

1. Visit the site in real Firefox and solve the challenge once so the trusted cookie exists.
2. Use a headed browser (`headless=False`) for the challenge.
3. If it still fails, the site is fingerprinting Playwright; profile copying won't fix it. Consider `playwright-stealth`, a real browser via CDP, or a different source.

Don't retry the same challenge in a loop; it burns time and can worsen the block.
