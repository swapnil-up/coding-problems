#!/usr/bin/env bash
set -euo pipefail

solution="${1:-main.py}"
oj t -c "python3 ${solution}"
