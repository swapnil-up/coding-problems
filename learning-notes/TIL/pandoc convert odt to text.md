# pandoc convert odt to text

Date: 2026-05-27 19:37

---

`odt2txt` is often not installed, but pandoc and LibreOffice usually are.

```bash
pandoc "notes.odt" -t plain --wrap=none
pandoc "notes.odt" -t markdown --wrap=none -o notes.md
```

`--wrap=none` keeps long paragraphs on one line, which is better for grepping. The same commands work for `.docx`.
