# nepali phonetic typing with xkb

Date: 2026-08-02 01:48

---

Quick phonetic (Roman → Devanagari) typing with no daemon, using XKB layouts
already shipped with X:

```
setxkbmap -layout in -variant hin_kagapa    # phonetic Devanagari (KaGaPa convention)
setxkbmap -layout np                        # traditional Nepali layout
```

- `in` variant `hin_kagapa` is **phonetic** — type `namaste` → नमस्ते. It's the
  Hindi convention but Devanagari is shared, so it works for Nepali.
- `np` is the traditional key→letter (typewriter) layout, not phonetic.

Tip: toggle it from i3 with a `bindsym` running the `setxkbmap` command (global
switch, all apps at once). For proper Nepali transliteration (correct
half-consonants/matras) install `ibus-m17n` and use the `ne-rom-translit` engine
— ibus is usually already running.
