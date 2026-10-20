# git merge unrelated repos into a monorepo

Date: 2026-06-09 23:09

---

To preserve history when folding standalone repos into one monorepo, rewrite each source repo so its files appear under a subdirectory, then merge the rewritten history:

```bash
cd ~/github/emom
git filter-repo --to-subdirectory-filter app-emom/

cd ~/github/kmp
git merge --allow-unrelated-histories ~/github/emom
```

`filter-repo` rewrites history, so work on a fresh clone or make a backup first. The repos have no common ancestor, hence `--allow-unrelated-histories`.

After the merge, verify that the old commits are still reachable and that every path landed under the intended prefix:

```bash
git log --oneline --graph --all -20
git ls-tree -d --name-only HEAD
```

If two repos contain the same path, resolve the collision in the rewritten source before merging, not after.
