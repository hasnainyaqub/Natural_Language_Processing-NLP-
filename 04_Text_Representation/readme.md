# 🔡 Text Representation in Natural Language Processing (NLP)

Text representation is the process of converting human language into a numerical form that can be understood by machine learning and deep learning models.  
Since computers cannot directly process raw text, we must represent words, phrases, or documents as numerical vectors while preserving their meaning and relationships.

---

## 💡 Why Text Representation Matters

Machine learning models require numerical input.  
Text representation bridges the gap between **human-readable language** and **machine-understandable data**.

A good representation should:
- Capture semantic meaning (similar words have similar vectors)  
- Handle vocabulary efficiently  
- Preserve context and relationships between words  
- Work well for both small and large datasets  

---

## 🧩 Categories of Text Representation

Text representation techniques can be broadly divided into two types:

1. **Traditional (Statistical) Methods**  
2. **Modern (Distributed / Contextual) Methods**

---

## 1️⃣ Traditional (Statistical) Representations

These methods rely on word frequency and statistical relationships between words.

### A. Bag of Words (BoW)
- Represents text as a collection (bag) of individual words.  
- Each document is converted into a vector that counts word occurrences.  
- Word order is ignored.

Example:

| Text | I love NLP | I love AI |
|------|-------------|------------|
| love | 1 | 1 |
| NLP  | 1 | 0 |
| AI   | 0 | 1 |

**Advantages:**
- Simple and easy to implement  
- Works well for basic classification tasks  

**Disadvantages:**
- Ignores context and word order  
- Creates large, sparse matrices  

---

### B. TF-IDF (Term Frequency–Inverse Document Frequency)
- Improves upon Bag of Words by giving more importance to rare words.  
- Balances how often a word appears in a document vs. across all documents.

Formula:  
**TF-IDF = (Term Frequency) × (Inverse Document Frequency)**

**Advantages:**
- Highlights unique and meaningful words  
- Works well for information retrieval and document ranking  

**Disadvantages:**
- Still ignores semantic meaning  
- Sparse representation  

---

### C. N-Grams
- Considers combinations of consecutive words (bigrams, trigrams, etc.)  
- Adds partial context by capturing short word sequences.

Example:  
Sentence: `"I love NLP"`  
Bigrams: `("I love")`, `("love NLP")`

**Advantages:**
- Retains local context  
**Disadvantages:**
- Rapidly increases dimensionality  
- Sparse and memory-heavy  

---

## 2️⃣ Modern (Distributed / Contextual) Representations

These methods use dense vectors to represent words or sentences, capturing meaning and context.

### A. Word Embeddings
Word embeddings are dense vector representations where similar words have similar numerical values.  
They capture **semantic** and **syntactic** relationships between words.

#### Common Word Embedding Models
- **Word2Vec:** Learns embeddings using Skip-Gram or CBOW architecture.  
- **GloVe (Global Vectors):** Combines global co-occurrence statistics and local context.  
- **FastText:** Represents words as character n-grams, handling out-of-vocabulary words better.

**Example:**
vector("king") - vector("man") + vector("woman") ≈ vector("queen")

---

### B. Contextual Word Representations
Unlike static embeddings, contextual models assign **different embeddings** to the same word depending on the sentence.

Example:  
- “I went to the **bank** to deposit money.”  
- “The **bank** of the river was calm.”

Contextual models produce different vectors for “bank” in each sentence.

#### Common Contextual Models
- **ELMo (Embeddings from Language Models)**  
- **BERT (Bidirectional Encoder Representations from Transformers)**  
- **GPT (Generative Pretrained Transformer)**  
- **RoBERTa**, **T5**, and others  

**Advantages:**
- Captures true contextual meaning  
- Handles polysemy (words with multiple meanings)  
- Achieves state-of-the-art results in NLP tasks  

**Disadvantages:**
- Computationally expensive  
- Requires large datasets and resources  

---

## 🧠 Sentence and Document Representations

Beyond word-level embeddings, entire sentences or documents can be represented as vectors using:
- **Averaging word embeddings**
- **Doc2Vec (Paragraph Vector)**
- **Sentence-BERT**
- **Universal Sentence Encoder (USE)**

These representations are useful for:
- Document classification  
- Semantic search  
- Text similarity and clustering  

---

## ⚙️ Choosing the Right Representation

| Task Type | Recommended Representation |
|------------|-----------------------------|
| Simple classification | TF-IDF |
| Large dataset | Word2Vec or GloVe |
| Context-dependent understanding | BERT, RoBERTa, GPT |
| Sentence-level tasks | Sentence-BERT, USE |
| Resource-limited environments | FastText |

---

## 📚 Summary

| Method | Type | Context-Aware | Sparse/Dense | Example Models |
|--------|------|----------------|---------------|----------------|
| BoW | Statistical | No | Sparse | CountVectorizer |
| TF-IDF | Statistical | No | Sparse | TfidfVectorizer |
| Word2Vec | Distributed | No | Dense | CBOW, Skip-Gram |
| GloVe | Distributed | No | Dense | GloVe |
| FastText | Distributed | No | Dense | FastText |
| BERT / GPT | Contextual | Yes | Dense | Transformers |

---

## 🏁 Conclusion

Text representation is the foundation of NLP.  
Choosing the right technique directly affects model performance and accuracy.  
While traditional methods work well for smaller or simpler tasks, modern embeddings and transformer-based representations dominate most advanced NLP applications today.

---

**End of Document**
