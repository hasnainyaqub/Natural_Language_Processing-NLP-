## 🧠 Word2Vec

**Word2Vec** is a powerful **word embedding technique** developed by Google that transforms words into continuous **vector representations**. These vectors capture **semantic relationships** between words, allowing models to understand how words relate in meaning and context.

### ⚙️ How It Works
Word2Vec uses a **neural network** with one hidden layer to learn word associations from a large text corpus. It has two main training architectures:

1. **CBOW (Continuous Bag of Words)**  
   - Predicts a target word based on its surrounding context words.  
   - Faster and performs well with smaller datasets.

2. **Skip-Gram**  
   - Predicts surrounding words given a target word.  
   - Works better with larger datasets and rare words.

### 🧩 Example
If the model learns from sentences like:  
> "The cat sits on the mat" and "The dog lies on the mat"  

Then **Word2Vec** can understand that *cat* and *dog* are similar in context because they appear in similar surroundings.

### 📈 Applications
- Sentiment analysis  
- Text classification  
- Machine translation  
- Document similarity  
- Semantic search  

### 📦 Using Pre-trained Models
You can use pre-trained embeddings such as:
- **Google News Vectors (300 dimensions)**  
  File: `GoogleNews-vectors-negative300.bin.gz`

```python
from gensim.models import KeyedVectors

# Load pre-trained Google News Word2Vec model
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

# Example usage
vector = model['king']
similar_words = model.most_similar('king')
