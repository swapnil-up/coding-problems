# git shallow clone a repo

Date: 2026-04-18 06:14

---

For getting all of a monster project with a really large .git onto your local if you get the error:
```
error: RPC failed; curl 92 HTTP/2 stream 0 was not closed cleanly: INTERNAL_ERROR (err 2) error: 7222 bytes of body are still expected fetch-pack: unexpected disconnect while reading sideband packet fatal: early EOF fatal: fetch-pack: invalid index-pack output
```
Fetch only the latest commits, then unshallow it: 
```
git fetch --depth 1 origin dolphin_deployment
```
