# coop coep service worker for sharedarraybuffer

Date: 2026-05-23 12:59

---

`SharedArrayBuffer` (and therefore Emscripten pthreads / WASM threads) only works when the page is cross-origin isolated. Static hosts that can't set headers can use a service worker that re-serves responses with:

```
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp   (or credentialless)
```

`coi-serviceworker.js` registers itself, reloads the page once, then intercepts fetches and adds those headers. Scope it to the page that needs threads: `require-corp` also applies to fonts, images, and other cross-origin resources, which must send CORP/CORS headers. `credentialless` is looser but still affects some CDNs.
