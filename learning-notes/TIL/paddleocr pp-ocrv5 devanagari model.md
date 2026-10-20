# paddleocr pp-ocrv5 devanagari model

Date: 2026-05-26 07:54

---

PP-OCRv5 has a Devanagari recognition model, but `lang="ne"` does not select it automatically. The generic PP-OCRv5 path returns `PP-OCRv5_mobile_rec`, which mangles Nepali numerals and conjuncts.

Select the model explicitly:

```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(
    text_detection_model_name="PP-OCRv5_mobile_det",
    text_recognition_model_name="devanagari_PP-OCRv5_mobile_rec",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
)
```

Known-good versions:

```text
paddleocr>=3.5.0
paddlepaddle>=3.1,<3.3   # 3.2.2 tested; 3.3.x has a PIR format bug
paddlex==3.5.2
```

Render PDF pages at 300 DPI before OCR. Accuracy went from roughly 50% with PP-OCRv3 to 85–90% with the v5 Devanagari model: `२॰ट३` became `२०८३`, and `िबहीबार` became `बिहीबार`.
