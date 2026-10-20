# git list subtrees

Date: 2026-05-21 07:18

---

`git subtree` records the imported directory and commit in each split/merge commit body. There is no `git subtree list`, so grep the bodies:

```bash
git log --all --format="%b" | grep "^git-subtree-dir:" | sort -u
```

Output lines look like `git-subtree-dir: miniprojects/bookmarks-sorter`. `--all` is required if the subtree commits are not on the current branch.

To see the commits that introduced them:

```bash
git log --all --grep="git-subtree-dir" --pretty=format:"%h %s"
```
