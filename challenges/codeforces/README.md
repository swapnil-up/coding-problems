# Codeforces — local workflow

Solve and test everything on your laptop; submit only when you choose.

## Layout

```
codeforces/
  new.sh        # pull a problem + samples into contest/letter/
  t.sh          # run your solution against the samples
  template.py   # fast-I/O starting point
  0004/
    A/
      main.py   # your solution
      test/     # sample-*.in / sample-*.out (gitignored)
```

## Daily loop

From `codeforces/`:

```bash
./new.sh https://codeforces.com/problemset/problem/4/A
cd 0004/A
# edit main.py
../../t.sh
```

`t.sh` runs `oj t -c "python3 main.py"` and prints AC/WA per sample, with timing and memory.

## Submitting (optional, one-time login)

```bash
oj login https://codeforces.com
oj s main.py
```

`oj` infers the language from the file. To submit as PyPy (recommended for speed):

```bash
oj languages            # find the exact name, e.g. "PyPy 3-64"
oj s --language "PyPy 3-64" main.py
```

## Writing solutions

Start from the template:

```python
import sys


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    sys.stdout.write(str(sum(a)))


if __name__ == "__main__":
    solve()
```

- Read all input once with `sys.stdin.buffer.read().split()`.
- Write a single string to stdout; avoid per-line `print` in hot loops.
- Deep recursion: raise the limit or use an iterative DFS.

## Where to start

Fundamentals order and resources are in `../../resources/competitive-programming.md`. First reps: Codeforces rating 800–1000, or CSES *Introductory Problems* if the CF style feels unfamiliar.
