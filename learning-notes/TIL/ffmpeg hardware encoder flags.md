# ffmpeg hardware encoder flags

Date: 2026-08-06 23:36

---

Don't just swap `-c:v libx264` for a hardware codec; each kind needs its own device, filter, and quality flags.

| kind | codec flags | filter | init |
| --- | --- | --- | --- |
| VAAPI | `-c:v h264_vaapi -qp 23 -bf 0` | `format=nv12,hwupload` | `-vaapi_device /dev/dri/renderD128` |
| NVENC | `-c:v h264_nvenc -preset p4 -rc vbr -cq 23` | `format=yuv420p` | none |
| QSV | `-c:v h264_qsv -global_quality 23` | `format=yuv420p` | none |
| CPU | `-c:v libx264 -preset fast -crf 23` | `format=yuv420p` | none |

VAAPI init flags go before the input; the format filter goes in `-vf`. Probe devices by actually encoding a 0.1s test pattern to a temp file, not just by checking `/dev/dri/renderD*`. A good detection order is VAAPI → NVENC → QSV → CPU.

Keep the audio tail (`-c:a aac -b:a 192k`) and `-movflags +faststart` separate from the encoder logic: they don't vary by encoder.
