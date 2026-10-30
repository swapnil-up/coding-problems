import sys


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    w = int(data[0])
    sys.stdout.write("YES\n" if w % 2 == 0 and w > 2 else "NO\n")


if __name__ == "__main__":
    solve()
