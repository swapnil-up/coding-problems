# service worker breaks large firefox streams

Date: 2026-05-23 20:44

---

A COI service worker that wraps every response in `new Response(response.body, ...)` to add COOP/COEP headers broke a 31 MB Hugging Face model download in Firefox:

```
NS_BINDING_FAILED
TypeError: Error in input stream
```

The body is a stream; re-wrapping it for a large cross-origin binary made Firefox fail. Fix: skip requests that don't need isolation:

```js
self.addEventListener('fetch', (event) => {
  if (new URL(event.request.url).hostname === 'huggingface.co') return
  event.respondWith(addCoiHeaders(event.request))
})
```

Only intercept same-origin documents/WASM that actually need `SharedArrayBuffer`. Alternatively pass `event.request` through untouched and only add headers to the document response.
