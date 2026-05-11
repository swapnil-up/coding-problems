# Chapter 1: Understanding Large Language Models — Study Questions
## Before you begin
These questions are designed to be answered **from memory first**. After you answer, we'll probe for shallow answers and deepen them. Don't look at the book. Trust your gut.
---
## §1.1 — What is an LLM?
1. In one sentence, what does an LLM *do* at its core? Don't say "understands" — what does it actually compute?
2. What does "large" refer to in "large language model"?
3. What is the simplest possible task you could train a neural network on to make it "smart" at language?
4. Why is next-word prediction a good training task? What makes it better than, say, filling in the middle of a sentence?
5. What is the transformer architecture, and why does it matter for LLMs?
6. What does "generative AI" mean, and why are LLMs called that?
---
## §1.2 — Applications of LLMs
7. What are LLMs bad at compared to humans? (Be honest — don't just list strengths)
8. If you wanted to use an LLM to build a medical chatbot, what problem might you face?
---
## §1.3 — Stages of building and using LLMs
9. What is the difference between pretraining and fine-tuning? In one sentence each.
10. Why don't you need labeled data for pretraining? Where do the "labels" come from?
11. What is "self-supervised learning"? How does it differ from supervised learning?
12. What is the difference between **instruction fine-tuning** and **classification fine-tuning**? Give an example input/output for each.
13. What is a "base model" or "foundation model"? Name one.
14. Why might a company want to build a custom LLM instead of using ChatGPT?
15. Why is pretraining expensive? What's the rough cost of GPT-3 pretraining?
---
## §1.4 — Introducing the transformer architecture
16. Draw (in words or a ASCII sketch) the original transformer architecture. What's on the left side? What's on the right side?
17. What is an **encoder** and what does it do?
18. What is a **decoder** and what does it do?
19. The original transformer was for machine translation. How does that explain why it has both an encoder and a decoder?
20. What is the difference between BERT and GPT in terms of which part of the transformer they use?
21. BERT does masked word prediction. What does that mean — give an example input/output?
22. GPT does text generation. What does that mean — give an example input/output?
23. What is "self-attention" and why is it important? (Don't just say "paying attention" — what is the mechanism actually doing?)
24. What does "autoregressive" mean for GPT models?
25. Zero-shot vs few-shot: What's the difference? Which one is more impressive and why?
---
## §1.5 — Utilizing large datasets
26. What is a "token" in the context of LLMs? Roughly how many tokens are in this chapter?
27. GPT-3 was trained on ~300 billion tokens. Where did those tokens come from? (Name the sources and roughly how much each contributed)
28. Why does dataset diversity matter for LLM capabilities?
29. What is the relationship between number of training tokens and model capability?
---
## §1.6 — A closer look at the GPT architecture
30. What is an "emergent behavior" in an LLM? Give an example that surprised researchers.
31. GPT was not trained to translate. Yet it can. What does this tell you about how LLMs learn?
32. How many transformer layers did GPT-3 have? How many parameters?
33. What is the difference between GPT-1, GPT-2, GPT-3, and ChatGPT (in terms of architecture and training)?
---
## §1.7 — Building a large language model
34. What are the three main stages of building an LLM from scratch, in order?
35. Why can't most people pretrain a GPT-3-class model from scratch? What's the bottleneck?
36. If you skip pretraining and load pretrained weights instead, what do you gain? What do you lose?
---
## Deeper / Tricky Questions
37. Why did the transformer paper matter so much? What was the key insight?
38. If you removed the self-attention mechanism from a transformer, what would break first?
39. Could you build an LLM without a transformer? (Hint: the chapter says this is possible but rare — why would you try?)
40. What's the difference between "understanding" and "generating coherent text"? Can you have one without the other?