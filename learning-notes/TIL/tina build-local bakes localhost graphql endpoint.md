# TinaCMS build-local bakes a localhost:4001 GraphQL endpoint

Date: 2026-11-07

---

A TinaCMS site built with `pnpm build-local` (no Tina Cloud credentials) renders
the shell fine but **fails to fetch content**. The reason: the generated client
points at the local Tina server, which only runs under `pnpm dev`.

Check the generated client:

```bash
grep -nE "localhost|4001|isLocal|VITE_TINA|fetch" tina/__generated__/client.ts
```

It resolves to `http://localhost:4001/graphql`, i.e. the Tina local content
server that `tinacms dev` starts. `vite preview` serves the static build but
**not** that GraphQL endpoint, so any real render/verification pass against a
`build-local` artifact must run against the **dev server**, not `preview`.

Practical consequences:

- `pnpm build-local` is fine for typechecking and compiling the SPA.
- To actually verify content-driven rendering, run `tinacms dev -c "vite"` and
  point the browser at the dev URL.
- For real deploys you need either Tina Cloud credentials or to run the local
  server at build time; a plain static `preview` of a local build won't show
  content.
