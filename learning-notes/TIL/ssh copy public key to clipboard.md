# ssh copy public key to clipboard

Date: 2025-12-29 21:45

---

## Insight
Pipe the key into xclip directly.

## Example
xclip -sel clip < ~/.ssh/id_rsa.pub

## Why this matters
Instead of cat, you copy the whole thing as needed.
