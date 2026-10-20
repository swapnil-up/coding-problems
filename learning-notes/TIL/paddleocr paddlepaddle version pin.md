# paddleocr paddlepaddle version pin

Date: 2026-06-19 20:51

---

PaddleOCR 3.7.0 on CPU hung for 60s+ per page (or raised
`ConvertPirAttribute2RuntimeAttribute not support ...`) with PaddlePaddle
3.3.1 / 3.2.0. The cause is an oneDNN/PIR regression on the CPU path, not the
OCR models.

Try PaddlePaddle 3.2.2 with oneDNN disabled:

```
pip install "paddlepaddle==3.2.2"
```

```
import os
os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "0"
os.environ["FLAGS_allocator_strategy"] = "naive_best_fit"

from paddleocr import PaddleOCR
ocr = PaddleOCR(lang="hi")
```

If it still hangs, pin both:

```
pip install "paddlepaddle==3.2.0" "paddleocr==3.3.3"
```

The env vars must be set before importing paddle or PaddleOCR.
