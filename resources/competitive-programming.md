# Competitive Programming — Resources

Python track, Codeforces for reps. Fundamentals first.

## The two books

- **LeetCode 101: A Grinding Guide** — Chang Gao
  - GitHub: https://github.com/changgyhub/leetcode_101
  - Read online (2nd ed.): https://noworneverev.github.io/leetcode_101/en
  - Techniques/pattern recognition for interview problems. C++ & Python.
- **Competitive Programming 4** — Steven & Felix Halim, Suhendry Effendy
  - https://cpbook.net — contains the formal "Methods to Solve" (MtS) framework.
  - Paid. Free stand-in below covers the fundamentals better as a starting point.
- **Competitive Programmer's Handbook** — Antti Laaksonen (free)
  - https://cses.fi/book/book.pdf — the canonical beginner text. Start here.

## Fundamentals track

Work a topic at a time: read the chapter, then do the matching CSES section, then 3–5 Codeforces problems of the same tag.

| # | Topic | Read | Practice |
|---|-------|------|----------|
| 1 | Complexity, I/O, stdin/stdout | CPHB ch. 1–2 | CSES *Introductory Problems* |
| 2 | Sorting & searching | CPHB ch. 3 | CSES *Sorting and Searching* |
| 3 | Stacks, queues, sets, maps, prefix sums | CPHB ch. 4 | CSES *Data Structures* |
| 4 | Recursion & backtracking (complete search) | CPHB ch. 5 | CSES *Introductory Problems* (harder half) |
| 5 | Dynamic programming | CPHB ch. 6 | CSES *Dynamic Programming* |
| 6 | Graphs: BFS/DFS, shortest paths | CPHB ch. 7–8 | CSES *Graph Algorithms* |
| 7 | Number theory & math | CPHB ch. 9–10 | CSES *Mathematics* |

## Reference (lookup, not cover-to-cover)

- cp-algorithms — https://cp-algorithms.com — every technique, with code.
- USACO Guide — https://usaco.guide — topic tracks linking problems across judges.
- Princeton CP resources — https://competitive-programming.cs.princeton.edu/resources

## Practice

- **CSES Problem Set** — https://cses.fi/problemset — ~300 problems ordered by topic. Best fundamentals drill.
- **Codeforces problemset** — https://codeforces.com/problemset — filter by rating + tag.
  - 800–1000: warm-up, get used to stdin/stdout.
  - 1000–1200: fundamentals reps.
  - 1200–1400: solid early-medium; where real thinking starts.
- **Codeforces EDU / ITMO courses** — structured topic walk-throughs.

## Python on Codeforces

- Read all input at once, fast:
  `data = sys.stdin.buffer.read().split()`
- Submit as **PyPy3** — substantially faster than CPython in tight loops.
- Practical ceiling is roughly **1300–1400**; past that Python TLE becomes the bottleneck before your algorithm does. Then micro-optimize or switch to C++.
- Expect full stdin/stdout programs, not LeetCode's `class Solution` signature.
- Deep recursion: `sys.setrecursionlimit(...)`; prefer iterative DFS on large inputs.

## How to use these together

- CPHB + CSES = learn the technique and get the reps.
- LeetCode 101 = pattern recognition and interview framing.
- Don't read cover-to-cover. One chapter → that CSES section → a few CF problems.

## Habits that close the gap you already have

- After a solution works, ask: "is there a cleaner O(n)?" Refactor toward it (hash map / two pointers) instead of shipping the brute force.
- Re-implement each solved problem from scratch the next day (spaced repetition).
- Before coding, write the approach and its time/space complexity in one line.
