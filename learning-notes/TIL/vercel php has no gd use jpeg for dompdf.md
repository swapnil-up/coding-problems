# vercel php has no gd use jpeg for dompdf

Date: 2026-06-14 09:17

---

`vercel-php` doesn't ship the GD extension (`PHP_EXTENSIONS=gd` in `vercel.json` is ineffective). Dompdf needs GD to decode PNGs, so image-bearing PDFs return 500.

Options:

- Convert uploads to JPEG client-side (Canvas API) before sending; Dompdf embeds raw JPEG without GD.
- Use a PDF renderer that doesn't need GD.

Check `php -m | grep -i gd` on the deployed function; don't trust the dashboard setting.
