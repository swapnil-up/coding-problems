# audacity mashup editing basics

Date: 2026-09-16 19:28

---

Quick workflow for making a dance mashup in Audacity on Ubuntu.

- Import each track with **File → Import → Audio**.
- Match tempo: select a clip, **Effect → Change Tempo** to the target BPM.
- Move clips with the **Time Shift** tool (or drag the clip).
- Trim: select the excess and press Delete; or select the keeper part and press
  `Ctrl+T` (Trim Audio).
- Crossfade: overlap the two clips on separate tracks, select the overlap,
  **Effect → Crossfade Tracks**. If only Fade In/Fade Out are installed, apply
  those manually to the overlapping ends.
- Level match: select the quieter track and use **Effect → Amplify** or
  **Normalize Loudness**, or adjust its Gain slider.
- Export: **File → Export Audio** as WAV/MP3.

Useful selection shortcuts: `Ctrl+A` all, `Ctrl+Shift+A` none,
`Shift+Left/Right` extend, `[` / `]` set selection boundaries, `Shift+J` /
`Shift+K` select to track start/end.
