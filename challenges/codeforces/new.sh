#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ $# -ne 1 ]; then
    echo "usage: new.sh <problem-url>" >&2
    echo "  e.g. new.sh https://codeforces.com/problemset/problem/4/A" >&2
    echo "       new.sh https://codeforces.com/contest/4/problem/A" >&2
    exit 1
fi

url="$1"

if [[ "$url" =~ /problemset/problem/([0-9]+)/([A-Za-z0-9]+) ]]; then
    contest="${BASH_REMATCH[1]}"
    prob="${BASH_REMATCH[2]}"
elif [[ "$url" =~ /contest/([0-9]+)/problem/([A-Za-z0-9]+) ]]; then
    contest="${BASH_REMATCH[1]}"
    prob="${BASH_REMATCH[2]}"
else
    echo "could not parse contest/problem from URL: $url" >&2
    exit 1
fi

dir="$SCRIPT_DIR/$(printf '%04d' "$contest")/${prob}"
mkdir -p "$dir"

oj d --directory "$dir/test" "$url"

if [ ! -f "$dir/main.py" ]; then
    cp "$SCRIPT_DIR/template.py" "$dir/main.py"
    echo "[ok] created $dir/main.py from template"
fi

echo "[ok] cd $dir && ../../t.sh"
