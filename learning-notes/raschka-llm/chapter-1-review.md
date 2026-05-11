§1.1 — What is an LLM?
Q1 (What does an LLM compute?) — "mass autocomplete" is the right intuition. But be precise: an LLM computes a probability distribution over the next token given all previous tokens. It doesn't just "figure out the next word" deterministically — it assigns a probability to every possible next word, then samples one. The randomness in sampling is why the same prompt can give different answers.

Q4 (Why next-word over middle-of-sentence?) — You said you're unsure. Here's why: next-word prediction is a causal task — the answer at position N only depends on positions 1..N-1. This naturally creates a left-to-right ordering that matches how we generate text. Filling in the middle of a sentence (BERT's task) would let the model "see the future" and cheat — it wouldn't learn sequential reasoning. Next-word prediction also scales trivially: every sentence in the training data becomes a training example for free.
Q4 — Why is next-word prediction better than fill-in-the-middle?
Next-word prediction (called causal or autoregressive training) forces the model to learn directionality — how meaning builds left to right. Every single token in the training corpus becomes a training example automatically: given tokens 1–N, predict token N+1. The signal is incredibly dense. Fill-in-the-middle (BERT's masked prediction) is also useful but it trains a bidirectional understanding, which is great for comprehension tasks but breaks the generation loop — you can't autoregressively generate if your model needs to see future tokens.

Q5 (What is the transformer architecture?) — "Vector multiplication" is too vague. Think of it this way: the transformer is a sequence-to-sequence architecture that processes the entire input in parallel (unlike RNNs that process one word at a time). It uses self-attention to let every token look at every other token and compute relationships between them. The key insight was: you can replace recurrence (RNNs processing sequentially) with attention (everything at once), and it's both faster and more effective.
Your answer ("converts data from one point to another, like vector multiplication") is too vague. The transformer is a specific neural network architecture built around one key mechanism: self-attention. Before transformers, LLMs used RNNs (recurrent neural networks), which processed tokens one at a time sequentially. The transformer's insight was: process all tokens in parallel, but let each token "look at" every other token in the sequence to figure out which ones are relevant to it. This parallelism is what made training on massive datasets feasible.
---
§1.3 — Stages of building and using LLMs

Q10 (Where do pretraining labels come from?) — You said "the patterns it figures out." That's vague. Be specific: the label for position N is simply the token at position N+1. The sentence itself contains both input and label. "The cat sat on the" → label is "mat." No human needed. That's self-supervised.
You're right that labeled data isn't needed, but your explanation of where labels come from is fuzzy. The label for any token is simply the next token in the text. If your training text is "the cat sat on the mat," the model sees "the cat sat on the" and the label is "mat." The text itself generates the supervision signal. This is why it's called self-supervised.

Q11 — Self-supervised vs supervised
Close but slightly off framing. In supervised learning, a human labels the data externally ("this email is spam / not spam"). In self-supervised learning, the labels are derived from the structure of the data itself — no human needed. Next-word prediction is self-supervised because the corpus itself provides the targets. The "self" refers to the data supervising itself, not the model supervising itself.

Q12 — Instruction vs classification fine-tuning
Your intuition is right but worth sharpening:

Instruction fine-tuning: input is a natural language instruction, output is a natural language response. Example input: "Summarize this article in 3 bullet points." Output: three bullet points. This is how ChatGPT was made from GPT-3.
Classification fine-tuning: input is text, output is a category label from a fixed set. Example input: "This movie was fantastic!" Output: "positive." The output vocabulary collapses to just the possible classes.

Q13 (Foundation model example) — GPT-2 was not the foundation for GPT-3. They're both separate model releases by OpenAI. ChatGPT (2022) was GPT-3 fine-tuned on instruction data. GPT-3.5-turbo is a different variant. A better answer: GPT-3 (the base model) was the foundation for the original ChatGPT. Or BERT is a foundation model that was fine-tuned for many downstream tasks.
GPT-2 is not a foundation model for GPT-3 in the sense you implied — they weren't fine-tuned from each other, they were separately pretrained at different scales. A better example: GPT-3 is the foundation model, and InstructGPT (the predecessor to ChatGPT) was built by fine-tuning GPT-3.

Q15 (Cost of GPT-3 pretraining) — You guessed "30 billion worth of data" which is confused. The cost was roughly $4.6 million in cloud compute (from the chapter). The data was 300 billion tokens, not 30 billion.
---
§1.4 — Transformer architecture (biggest gap)

Q16-23 — The encoder/decoder structure is your biggest weakness here. Let me give you the mental model:
Input text → ENCODER (processes full input) → [internal state] → DECODER (generates output one token at a time)
- Encoder: reads the whole input sentence in parallel, builds a rich representation of each token that includes context from all other tokens. "The bank can fall" — the encoder knows "bank" here means financial institution, not river bank.
- Decoder: generates output one token at a time, left to right. At each step, it looks at (a) the encoder's output and (b) the tokens it has already generated. That's why it's called "decoder" — it converts the internal representation into text.
Why both for translation? Imagine translating "The bank can fall" to German. The encoder needs to see the whole English sentence to know which meaning of "bank" is intended. The decoder then generates German words one by one, referencing that full understanding.

Q20-22 (BERT vs GPT) — This is the critical distinction:
- BERT uses only the encoder. It was trained on a task called masked language modeling: you hide random words and the model predicts them. Input: "The MASK sat on the chair." → Output: "dog" (fills the mask). BERT is bidirectional — it sees the whole sentence at once, both left and right context. This makes it great for classification tasks (sentiment analysis, spam detection).
- GPT uses only the decoder. It was trained to generate text left to right, predicting one token at a time. Input: "The dog" → Output: "sat" (predicts next token). GPT is unidirectional — it can only see previous tokens, not future ones. This makes it great for generation.
The original transformer had encoder + decoder. Researchers discovered you could use just one half:

BERT uses only the encoder. The encoder reads the entire input bidirectionally (it can see left and right context simultaneously). BERT was trained on masked prediction: take a sentence, randomly replace some words with [MASK], and train the model to predict what the masked words were. Example: input = "The [MASK] sat on the mat", output = "cat." This makes BERT excellent at understanding tasks (sentiment analysis, question answering over a document) but it cannot generate text.
GPT uses only the decoder. It reads left-to-right only (each token can only see previous tokens). This makes it naturally autoregressive and suited for generation. Example: input = "The cat sat", output = "on" (then "the", then "mat", etc.)

Q23 (Self-attention) — No clue was correct, this is one of the deepest concepts. Here's the core idea:
The model has to figure out, for each word in a sentence, which other words are most relevant to understanding it. In the sentence "The cat sat on the mat because it was tired," the word "it" could refer to "cat" or "mat." Self-attention is the mechanism that lets every word ask questions about every other word and compute a relevance score. The word "it" would attend strongly to "cat" and weakly to "mat." This happens in parallel for all words at once. It's what lets transformers handle long-range dependencies — information can flow directly between any two positions without going through the chain of words between them.
This is the most important mechanism to understand. For each token, self-attention asks: which other tokens in this sequence are most relevant to interpreting this token?
Mechanically: each token gets turned into three vectors — a Query (Q), a Key (K), and a Value (V). To compute attention for token X, you take X's Query and dot-product it against every other token's Key. The resulting scores (after softmax) tell you how much to weight each token's Value. The final output for X is a weighted sum of all Value vectors.
Concretely: in "The animal didn't cross the street because it was too tired," self-attention lets "it" attend strongly to "animal" — resolving the coreference. An RNN would have to carry that information through many sequential steps and often loses it.

Q24 (Autoregressive) — "Auto" means "self," "regressive" here means "going backward" in time. An autoregressive model generates output step by step, and each step's output becomes part of the next step's input. GPT generates "the" → feeds that back in → generates "dog" → feeds that back in → generates "sat"... This feedback loop is why generation is slow — each token depends on all previous tokens.
Autoregressive means: each output token is fed back in as input to generate the next token. GPT generates "the", then feeds "the" back in to generate "cat", then feeds "the cat" back in to generate "sat", etc. It cannot generate the full sequence in parallel at inference time — each step depends on all previous steps.


Q25 (Zero-shot vs few-shot) — You had "zero shot is more impressive." Actually few-shot is impressive given constraints but zero-shot is more remarkable as a capability. In the chapter, GPT-3 notably improved zero-shot performance compared to GPT-2. The reason zero-shot is harder: the model must figure out a completely novel task from a plain-language instruction with no examples to anchor it.
You have these partially backwards. Zero-shot means the model gets no examples at all — just the task description. Few-shot means the model gets 2–5 examples in the prompt demonstrating the pattern, then a new case to solve. Zero-shot is more impressive philosophically (the model generalizes from training alone), but few-shot often performs better in practice because the examples clarify the expected format.

---
§1.5 — Datasets
Q26 (What is a token?) — "A chunk of characters" is too loose. A token is a numerical unit after tokenization — could be a whole word, a syllable, a punctuation mark, or part of a word. "tokenization" might become "token", "ization" — two tokens. LLMs have a fixed vocabulary (e.g., 50,257 tokens for GPT-4). Each token maps to a number. Rough estimate: ~1000-1500 tokens for this chapter. The chapter says the number of tokens ≈ number of words + punctuation.
More precisely, it's a subword unit. Common words are one token ("cat"), uncommon words get split ("unbelievable" → "un", "believ", "able"), and spaces/punctuation also tokenize. A rough rule: 1 token ≈ 0.75 English words. For this chapter specifically, it's probably 3,000–5,000 tokens, not 20,000 — that would be a very long chapter.

Q27 (GPT-3 data sources) — You said "Wikipedia was 3 million words" which is wrong. From the chapter:
- CommonCrawl (filtered web data): 410B tokens, 60%
- WebText2: 19B tokens, 22%
- Books1: 12B tokens, 8%
- Books2: 55B tokens, 8%
- Wikipedia: 3B tokens, 3%
- Total: ~300B tokens trained on
The 3 billion is tokens, not words. Wikipedia being only 3% shows how small but high-quality it is relative to the raw web.

Q29 (More tokens = better?) — You said "the more input we have, the more the model is capable." The relationship isn't linear — there's a threshold, and diminishing returns. But there's a real pattern: GPT-3's capabilities surprised people partly because it was trained on 300B tokens, far more than GPT-2's ~1B. The "Chinchilla scaling laws" (not in this chapter but related) argue models should keep scaling data alongside parameters.
---
§1.6 — GPT architecture
Q30 (Emergent behavior) — No clue. Emergent behavior = a capability that wasn't explicitly trained for and doesn't appear in smaller models, but suddenly appears when the model reaches a certain scale. Example from the chapter: GPT was trained only on next-word prediction, never on translation. Yet it could translate. No one programmed this — it emerged. Another example: GPT-3 could do simple arithmetic despite never being trained on math problems. The bigger the model, the more emergent behaviors appear.
Emergent behaviors are capabilities that appear at larger scales that were not present at smaller scales and were not explicitly trained for. The striking examples: GPT-3 can do multi-step arithmetic, translate between languages it wasn't specifically trained on, and write code — none of these were in the objective function. They just appeared. This surprised researchers because there was no obvious threshold or mechanism — capabilities seemed to switch on suddenly as model size increased.

Q32 (GPT-3 specs) — 96 transformer layers, 175 billion parameters. You can hold this in memory: roughly 350GB of weights in fp32 format. The pretraining cost was roughly $4–12 million in compute (estimates vary). This is why nobody reruns it.

Q33 (GPT-1 vs 2 vs 3 vs ChatGPT) — "Size and capabilities increased" is too vague:
- GPT-1 (2018): 117M parameters, 1B tokens, first demonstration that pretraining + fine-tuning worked
- GPT-2 (2019): 1.5B parameters, showed that scaling helped, controversial release
- GPT-3 (2020): 175B parameters, 300B tokens, strong few-shot and zero-shot abilities, base model
- ChatGPT (late 2022): Based on GPT-3.5 (a variant of GPT-3), but fine-tuned on instruction data (InstructGPT method) to follow human instructions. The base GPT-3 couldn't follow instructions well — the fine-tuning is what made it chatty and helpful.
---
§1.7 — Building an LLM

Q36 (Loading pretrained vs training from scratch) — "An amount of depth not possible" is unclear. Be concrete:
- Gain: You skip the $4.6M compute bill. You get a model that already understands language, grammar, facts, reasoning patterns. Your fine-tuning is fast and cheap by comparison.
- Lose: The model has whatever biases and knowledge were in the pretraining data. You're stuck with the architecture and initial capabilities — you can't reshape the fundamental "brain."
---
Deep Questions
Q37 (Why transformer paper mattered) — "As we increase the number of transformers, quality improves" isn't the right answer. The key insight was replacing recurrence with attention. RNNs (LSTMs) had to process sequences one token at a time, which made training slow and made it hard for information to travel from the start of a long sequence to the end (the "vanishing gradient" problem). Attention lets every token attend to every other token in one step. Parallel processing becomes possible → training on huge datasets becomes feasible → scale up.
The key insight was attention is all you need (literally the paper's title). Before it, sequence models were RNNs — they processed tokens one at a time, which meant: (a) you couldn't parallelize training, and (b) long-range dependencies degraded because information had to pass through many sequential steps. The transformer replaced recurrence entirely with self-attention, which (a) processes the whole sequence in parallel, enabling massive GPU utilization, and (b) connects any two tokens directly regardless of distance.


Q38 (Without self-attention) — You said "coherence would break." That's right but go deeper: without self-attention, the model would have no way to track which words relate to which. It would process each token in isolation (like a bag-of-words model) and lose all long-range context. "The spider that the cat that the dog chased ate was fat" would become incomprehensible — each part processed without understanding the relationships.

Q40 (Understanding vs coherent text) — You touched on it but the key insight is: yes, you absolutely can have one without the other. Current LLMs are proof: they generate coherent, grammatically correct text that often lacks genuine understanding (hallucinations, logical errors). Conversely, humans can understand something deeply but fail to articulate it coherently. Understanding involves grounding in meaning, world models, beliefs about truth — not just statistical patterns of word sequences.




