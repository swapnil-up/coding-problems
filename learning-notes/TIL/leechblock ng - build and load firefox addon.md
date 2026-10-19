# leechblock ng - build and load firefox addon

Date: 2026-07-17 11:44

---

`LeechBlockNG/` — a Firefox **WebExtension (Manifest V3)**.

Missing dependency: jQuery UI. Install it into `jquery-ui/` (already
gitignored, along with `*.xpi`).

**Load it temporarily in Firefox:**

1. Go to `about:debugging#/runtime/this-firefox`
2. **Load Temporary Add-on…**
3. Select `manifest.json` in the repo
4. It appears in the toolbar (gone on restart)

**Make it permanent:** sign it via Mozilla's Add-on Developer hub, **or** set
`xpinstall.signatures.required = false` in `about:config` and package it as an
XPI.
