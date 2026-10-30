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
