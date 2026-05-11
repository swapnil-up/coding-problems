# Chapter 1: Understanding Large Language Models — Study Questions
## Before you begin
These questions are designed to be answered **from memory first**. After you answer, we'll probe for shallow answers and deepen them. Don't look at the book. Trust your gut.

---

## §1.1 — What is an LLM?

1. In one sentence, what does an LLM *do* at its core? Don't say "understands" — what does it actually compute?
In one line, an LLM is just a mass autocomplete. It figures out what the next word is on and on until it gets sentences.


2. What does "large" refer to in "large language model"?
Large can refer to the large training size as well as the large number of parameters within the model.


3. What is the simplest possible task you could train a neural network on to make it "smart" at language?
Figure out the next word maybe or divide things into either or buckets.

4. Why is next-word prediction a good training task? What makes it better than, say, filling in the middle of a sentence?
unsure

5. What is the transformer architecture, and why does it matter for LLMs?
The transformer architecture refers to the internal processing step of the LML where it converts data from one point into another. Sort of like a vector multiplication.

6. What does "generative AI" mean, and why are LLMs called that?
Generative AI refers to how further content is generated. LLMs can figure out the next word sentence and so on because of which it is called Generative AI.

---

## §1.2 — Applications of LLMs

7. What are LLMs bad at compared to humans? (Be honest — don't just list strengths)
LLMs are worse at things that require a lot of context as well as things that are not included in its training data. Also, things that require more creativity while making sense

8. If you wanted to use an LLM to build a medical chatbot, what problem might you face?
The amount of training data that you have especially for the last fine tuning step that is correct yet large enough for the model

---

## §1.3 — Stages of building and using LLMs

9. What is the difference between pretraining and fine-tuning? In one sentence each.
Pre training is where you have a large amount of data. This point is to basically figure out what the next word is while fine tuning allows it to work for very specific circumstances like coding or medical related domain related tasks.

10. Why don't you need labeled data for pretraining? Where do the "labels" come from?
During the pre-training stage, the LLM is trying to figure out what the next word will be because of which it doesn't exactly matter if the data is labeled or not. It just needs to figure out the underlying grammatical structure. Labels, I think, are the patterns that it figures out as well as what we decide are labeled during fine tuning.

11. What is "self-supervised learning"? How does it differ from supervised learning?
Self-supervised learning is where labels are used to figure out the data but the supervision is done by the LLM itself. While during supervised learning a domain expert specifically tells it what is good data and what is good data and what is not.

12. What is the difference between **instruction fine-tuning** and **classification fine-tuning**? Give an example input/output for each.
Instruction fine tuning is for generating next step type of things like I need to figure out how to create an array would result in it giving me the steps to create an array while classification is more for figuring stuff out like whether or not given enough data samples.

13. What is a "base model" or "foundation model"? Name one.
These models are the initial models that are then fine-tuned. For example, chat GPT-2 was like the foundation model for chat GPT-3.

14. Why might a company want to build a custom LLM instead of using ChatGPT?
Outside of how the data for chargegbt might not be suitable for them in the training stage, especially during the fine-tuning stage where they need data specifically for their own purposes. Custum LLM might be better.

15. Why is pretraining expensive? What's the rough cost of GPT-3 pretraining?
pre-training is expensive because it requires all baddie large 30 billion worth of data which makes it expensive especially because it takes a large number of GPUs a large number of minutes to run, not sure about the cost

---

## §1.4 — Introducing the transformer architecture

16. Draw (in words or a ASCII sketch) the original transformer architecture. What's on the left side? What's on the right side?
The original transformer architecture just had an encoder on the left side and the decoder on the right side. I'm not sure how exactly each of the parts fit within.

17. What is an **encoder** and what does it do?
An encoder converts the input into something within its transformation structure.

18. What is a **decoder** and what does it do?
A decoder converts something within its transformation structure into the output.

19. The original transformer was for machine translation. How does that explain why it has both an encoder and a decoder?
With the machine translation, the English was encoded into the AI bit and then it was decoded into the German bit. So I'm assuming the encoder converts the raw English word into some vector position within its transformers and then the decoder then figures out which position that is with regard to the

20. What is the difference between BERT and GPT in terms of which part of the transformer they use?
No clue

21. BERT does masked word prediction. What does that mean — give an example input/output?
No clue

22. GPT does text generation. What does that mean — give an example input/output?
No clue

23. What is "self-attention" and why is it important? (Don't just say "paying attention" — what is the mechanism actually doing?)
No clue

24. What does "autoregressive" mean for GPT models?
No clue

25. Zero-shot vs few-shot: What's the difference? Which one is more impressive and why?

Few short means that given a few examples, it will figure out the solution to a blind problem, while zero short means that even if it wasn't remotely within the training data, it can still figure out the solution. Zero short is more impressive

---

## §1.5 — Utilizing large datasets

26. What is a "token" in the context of LLMs? Roughly how many tokens are in this chapter?
A token is a chunk of characters that is inserted or given out by an LLM. The chat contained about 20,000 tokens.

27. GPT-3 was trained on ~300 billion tokens. Where did those tokens come from? (Name the sources and roughly how much each contributed)
I'm assuming a lot of that data came from open and closed source texts on the internet. I'm sure where from. I think Wikipedia was 3 million words though.

28. Why does dataset diversity matter for LLM capabilities?
A data set diversity for an LLM allows for it to have avoided overfitting and biases by only focusing on one side. This allows it to figure out more possible solutions?

29. What is the relationship between number of training tokens and model capability?
Currently, we can take it that the more input that we have, the more training tokens that we have, the better the more models capable.

---

## §1.6 — A closer look at the GPT architecture

30. What is an "emergent behavior" in an LLM? Give an example that surprised researchers.
No clue

31. GPT was not trained to translate. Yet it can. What does this tell you about how LLMs learn?
Maybe it means that an LLM learns in patterns and those patterns aren't exactly obvious to human beings?

32. How many transformer layers did GPT-3 have? How many parameters?
No clue

33. What is the difference between GPT-1, GPT-2, GPT-3, and ChatGPT (in terms of architecture and training)?
The size and the capabilities increased as the size and generations evolved

---

## §1.7 — Building a large language model

34. What are the three main stages of building an LLM from scratch, in order?
pre training training post training/fine-tuning?

35. Why can't most people pretrain a GPT-3-class model from scratch? What's the bottleneck?
The compute required to train such a large model combined with the amount of data that it

36. If you skip pretraining and load pretrained weights instead, what do you gain? What do you lose?

I'm going to guess that there is an amount of depth that isn't possible when you just have the model weights instead of generating everything yourself. We gain speed in exchange.

---

## Deeper / Tricky Questions

37. Why did the transformer paper matter so much? What was the key insight?
The transformer paper rapidly increased how models work. The key insight was that as we increase the amount of transformers, the quality of the input output improves? I'm not sure.

38. If you removed the self-attention mechanism from a transformer, what would break first?
Coherence would probably break first.

39. Could you build an LLM without a transformer? (Hint: the chapter says this is possible but rare — why would you try?)
I'm not sure

40. What's the difference between "understanding" and "generating coherent text"? Can you have one without the other?
You can generate sentences that are grammatically correct and sentences that make sense in relation to one another without understanding what the question was asking for and not making logical sense in regards to what the question asked for. together somewhat unless you consider that you need to have some understanding to have some coherent text.