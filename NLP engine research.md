# ☘️Goal: Identify and evaluate NLP/ML techniques that can translate free-text user requests into structured parameters for the recommender system.
# Four common NLP/ML techniques:

(1)Keyword extraction (e.g NLTK, spaCy)

(2)Intent classification (transformer-based)

(3)Embedding and semantic similarity

(4)LLM prompt engineering ( few-shot examples to JSON output)

# (1)	Keyword extraction

NLTK (Natural Language Toolkit) is a traditional NLP library that focuses on rule-based and statistical text analysis.
We can combine with the TF-IDF and stopwords to extract the token and require manual rule creation for domain-specific phrase.:

•	Tokenization (word_tokenize)

•	Part-of-Speech (POS) tagging

•	Named Entity Recognition (NER) via built-in chunkers

•	TF-IDF or frequency-based keyword scoring

✅ Advantages
1. Lightweight, simple to customize.
2. Works offline; no need for heavy models.
3. Transparent logic—good for rule-based extraction or prototyping.

❌Disadvantages
1. Limited context understanding.
2. Requires manual rule creation for domain-specific phrases.
3. Accuracy drops on complex or ambiguous user input.

 spaCy is a modern, neural-based NLP library optimized for speed and production use.
It provides:

•  Linguistic features: POS tagging, dependency parsing, NER.

•  Pre-trained models: en_core_web_sm, en_core_web_trf (Transformer-based).

•  Matcher or EntityRuler for rule-based slot detection.

 ✅Advantages
1. Supports deep linguistic context (syntax, dependency).
2. Fast and production-ready.
3. Customizable with Matcher or EntityRuler for slot extraction.
4. Can integrate with transformer models (e.g., en_core_web_trf).

❌ Disadvantages
1.	Requires fine-tuning for domain-specific keywords (like “wheelchair _accessible”).
2.  Slightly heavier and slower than NLTK for small-scale applications.
3.  Doesn’t “infer” missing parameters unless paired with ML/NLU mode

# (2) Intent classification (transformer-based)
BERT（Bidirectional Encoder Representations from Transformers）: deep learning model developed by Google(2018) that understands language in both directions

BERT is a transformers model pretrained on a large corpus of English data in a **self-supervised fashion**. This means it was pretrained on the raw texts only, with **no humans labeling**them in any way (which is why it can use lots of publicly available data) **with an automatic process to generate inputs and labels** from those texts. However, in the **fine tuning stage**, we still need to **label (e.g. BIO Annotation: Begin of slot, I: Inside of slot and O: None of slot)** to perform the supervised learning, such as classification, answer of the questions and etc. More precisely, it was pretrained with two objectives:

•  Masked language modeling (MLM): taking a sentence, the model randomly masks 15% of the words in the input then run the entire masked sentence through the model and has to predict the masked words. This is different from traditional recurrent neural networks (RNNs) that usually see the words one after the other, or from autoregressive models like GPT which internally masks the future tokens. It allows the model to learn a bidirectional representation of the sentence.

•	Next sentence prediction (NSP): the models concatenates two masked sentences as inputs during pretraining. Sometimes they correspond to sentences that were next to each other in the original text, sometimes not. The model then has to predict if the two sentences were following each other or not.

Example: 
| **Utterance**                                     | **Tokens**                                                   | **Labels**                                                  |
| ------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| I want a 2 bedroom apartment in Berlin under 2000 | [I, want, a, 2, bedroom, apartment, in, Berlin, under, 2000] | [O, O, O, B-bedrooms, I-bedrooms, O, O, B-city, O, B-price] |


It provides:

•  Sentence classification (→ Intent detection)

•  Token classification (→ Slot filling / NER)

•  Question answering, summarization, etc.

The models are provided in the Hugging Faces:

google-bert/bert-base-uncased · Hugging Face

✅ Advantages
1.	**Deep bidirectional understanding** of meaning and relationships between words.
2.	**State-of-the-art accuracy** across multiple NLU tasks.
3.	Pre-trained on large corpora → fine-tune with minimal labeled data.
4.	Works well across domains (e.g., housing, healthcare, finance).
5.	Easy to extend for multilingual or multi-intent tasks(BERT multilingual)

•	❌ Disadvantages
1.	Can overfit small datasets if not fine-tuned carefully.
2.	Require **GPU for efficient training/inference**
3.	Still needs some domain-specific data for best results
4.	Can misinterpret highly domain-specific jargon
5.	Large model size needs higher memory and latency
   
#### Applications: Chatbots, Shopping assistant, booking assistants and virtual health assistant


# (3)Embedding and semantic similarity
Embedding is way of representing words, sentences or documents as a numeric vectors(list of numbers) in a continuous vector space. Semantic Similarity means how close in meaning two pieces of text are, using their embeddings. It is often calculated using cosine similarity, which measures the angles between two vectors.
 
 **How It Works**
 
 
	1. Text → Embedding (vector)
	
      Example: embedding("find an apartment in Berlin") → [0.21, -0.33, 0.78, ...]

	2.  Compare embeddings using cosine similarity:

       similarity=(A⋅B)/(∣∣A∣∣×∣∣B∣∣)

	3.  The closer the value is to 1, the more semantically similar the texts are.

The tools for embedding: BERT/Sentence-BERT, OpenAI Embedding, spaCy vectors 

✅ Advantages
1.	Capture semantic relationships, beyond exact words
2.	Works well across synonyms and paraphrases
3.	Easy to store embeddings and perform similarity search
4.	Can be used in search, classification, clustering, summarization, etc.
   
❌ Disadvantages
1.	May still confuse subtle context 
2.	Quality depends on pretraining data and model
3.	Computing embedding fpr large corpora can be expensive
4.	Needs post- processing or thresholds to interpret results
   
#### Application: Search Engines(find document match meaning), Chatbots, Recommendation systems(suggest similar content based on meaning), Healthcare NLP(match medical report with similar diagnoses or symptoms), Duplicate detection.

# (4)LLM prompt engineering ( few-shot examples to JSON output)
Prompt engineering is the practice of designing effective prompts(instructions and examples) to guide a large language model(LLM), like GPT, FLAN-T5 or Llama to produce the desired output without training or fine tuning the model. Instead of changing the model parameters, we can change the input prompt to control the output behavior.

It provides: 

• A task instruction

•  A few Examples (input -> output pairs)

•	Performing the task on a new input

•	No training or fine tuning is required

We take FLAN-T5 as an example. It was developed by Google and is based on a text-to-text transformer architecture. The original T5 (Text-to-Text Transfer Transformer) can perform various natural language processing tasks such as translation, summarization, classification, and information extraction.

FLAN-T5 extends T5 by being fine-tuned on thousands of instruction-based tasks, which enables it to better understand and follow human instructions compared to the original T5 model.

Compared with large language models such as OpenAI’s GPT series and Meta’s LLaMA, FLAN-T5 requires less memory and computational resources. If higher accuracy is desired, FLAN-T5 can still be further fine-tuned on domain-specific datasets.

The model is available on the Hugging Face platform, where various versions of FLAN-T5 can be accessed for research and practical applications.


For text abstract: jasonmcaffee/flan-t5-large-samsum · Hugging Face

✅ Advantages
1.	Works instantly — just by giving examples.
2.	Can generalize across domains (housing, medical, finance).
3.	Ideal for proof-of-concept NLP systems.
4.	Can generate machine-readable formats like JSON, CSV, or XML.
5.	Handles complex, natural, and ambiguous language better than rules or classical ML.
   
•	❌ Disadvantages
1.	Outputs can vary slightly across runs (non-deterministic, inconsistent).
2.	Needs careful prompt design to maintain consistent JSON formatting.
3.	Context window limits few-shot capacity for very long examples.
4.	LLM inference (especially large one) can be expensive and slower than lightweight models.
5.	Unlike BERT or spaCy, it is hard to interpret why the model made the decisions.
6.	Results can shift when using different base model or API.

#### Application: Chatbots, Education and Healthcare (extraction patient reports), Information extraction

# Comparsion of these Methods
________________________________________
🧩 Summary Table
| Method     | Pros                         | Cons                            | Best For                | Example                  |
| ---------- | ---------------------------- | ------------------------------- | ----------------------- | ------------------------ |
| Rule-Based | Simple, fast, transparent    | Not scalable, brittle           | Tokenization, regex NER | NLTK, spaCy              |
| ML         | Interpretable, fast          | Needs features, limited context | Intent, slot filling    | Logistic Regression, SVM |
| Embeddings | Semantic match, multilingual | No reasoning, static            | Search, clustering      | MiniLM, E5               |
| LLMs       | Context-rich, versatile      | Expensive, opaque               | Generation, parsing     | BERT, T5, FLAN, GPT      |


________________________________________



# Recommendation: 
Based on this project, since we have a limited number of user requests (training data) and are working on a personal computer (CPU-based environment), we can either use the FLAN-T5 large language model (LLM) with fine-tuning or apply spaCy to convert text strings into structured parameters.

The advantage of using FLAN-T5 is that it can perform well without the need for extensive data annotation or large-scale training, and it requires relatively low memory resources, making it suitable for lightweight or resource-constrained applications.


# References

1. [BERT GitHub Repository](https://github.com/google-research/bert/blob/master/README.md)

2. [Hugging Face - BERT Base Uncased](https://huggingface.co/google-bert/bert-base-uncased)

3. [Hugging Face -Sentence-similarity]( https://huggingface.co/tasks/sentence-similarity?utm_source=chatgpt.com)

4. [Hugging Face - Semantic search with FAISS](https://huggingface.co/learn/llm-course/en/chapter5/6?utm_source=chatgpt.com)

5. [Hugging Face - FLAN-T5 Large (Samsum)](https://huggingface.co/jasonmcaffee/flan-t5-large-samsum)

6. [Pre-Trained Joint Model for Intent Classification and Slot Filling with Semantic Feature Fusion](https://www.mdpi.com/1424-8220/23/5/2848?utm_source=chatgpt.com)




