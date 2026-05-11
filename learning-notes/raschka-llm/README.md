# Raschka — Build an LLM from Scratch

**Book:** [LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) by Sebastian Raschka

**Study approach:** Socratic. Questions first → answer from memory → probe shallow answers → deepen

---

## Chapters

| # | Title | Status |
|---|-------|--------|
| 1 | Understanding Large Language Models | ✅ Done |
| 2 | Working with Text Data | ⏳ In progress |
| 3 | Attention Mechanisms | 🔜 |
| 4 | Coding a GPT-like LLM | 🔜 |
| 5 | Pretraining | 🔜 |
| 6 | Fine-tuning for Classification | 🔜 |
| 7 | Instruction Fine-tuning | 🔜 |

---

## Key concepts mastered (Ch 1)

- LLM = probability distribution over next token (autocomplete at scale)
- Transformer = parallel sequence processing with self-attention (replaces recurrence)
- Encoder = processes input into contextual representation; Decoder = generates output one token at a time
- BERT = encoder-only, masked word prediction, classification tasks
- GPT = decoder-only, next-word prediction, text generation, autoregressive
- Pretraining = self-supervised (labels are the next token), no labeled data needed
- Fine-tuning = supervised, on labeled data (instruction or classification)
- Self-attention = every token asks "how relevant is every other token to me?" in parallel
- Emergent behavior = capability not explicitly trained, appears at scale (e.g., translation)
- Foundation/base model = pretrained model ready for fine-tuning
- GPT-3: 96 layers, 175B parameters, $4.6M pretraining cost

## Weak areas identified (Ch 1)

- Self-attention mechanism details (addressed in Ch 3)
- BERT masked word prediction specifics
- GPT autoregressive generation loop
- Chinchilla scaling laws (not in this chapter)
- Zero-shot vs few-shot distinction (minor gap)
- GPT-1/2/3/ChatGPT lineage details

---

## Structure of this directory

```
raschka-llm/
├── README.md           # This file
├── chapter-1-questions.md
├── chapter-2-questions.md   # [future]
├── session-log.md          # Failures and insights logged here
├── cards.csv               # Anki flashcards (anki-smith output)
└── workbook.md             # Grand Inquisitor workbook
```

## How to use this

1. Answer chapter questions from memory
2. Paste answers into the questions file
3. I debrief, identify shallow answers, push on gaps
4. Repeat until solid
5. Use `anki-smith` to convert session-log → Anki cards
6. Use `grand-inquisitor` when ready for stress-testing