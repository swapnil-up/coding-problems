# preeti reverse encoder pitfalls

Date: 2026-05-25 20:23

---

Converting Unicode Devanagari back to Preeti keystrokes is lossy and rule-order-sensitive.

- A post-rule case can add the `l` matra and then the general matra branch adds it again, producing `ll` (e.g. `प्रतिक्रिया`). Use a flag to skip the general branch when the special case already emitted it.
- Compound vowels may need decomposition: `ो` → `ा` + `े` before lookup; otherwise the independent-vowel branch misses.
- Preeti uses `f` as a halanta terminator. The converter's `्ा` → empty rule is intentional but lossy: `0ff` cannot round-trip to `णा`, because the first `f` strips the halanta. Don't "fix" this without accepting the encoding's limits.
- Test with round-trip cases (Unicode → Preeti → Unicode) rather than only one direction.
