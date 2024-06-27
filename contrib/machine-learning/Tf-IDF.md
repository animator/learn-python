## TF-IDF (Term Frequency-Inverse Document Frequency)

### Introduction
TF-IDF stands for Term Frequency Inverse Document Frequency. It is a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents (corpus). It is often used in information retrieval and text mining to identify the most significant words within a document.


### Terminologies
* Term Frequency (tf):It is a scoring of the frequency of word in the current  document. In document d, the frequency represents the number of instances of a given word t. Therefore, we can see that it becomes more relevant when a word appears in the text, which is rational. Since the ordering of terms is not significant, we can use a vector to describe the text in the bag of term models. For each specific term in the paper, there is an entry with the value being the term frequency.
$$tf(t,d) = N(t) / t(d)$$
where, 
N(t) = Number of times term t appears in document d
t(d) = Total number of terms in document d.


* Inverse Document Frequency (idf):It is a scoring of how rare the word is  across documents. Mainly, it tests how relevant the word is. The key aim of the search is to locate the appropriate records that fit the demand. Since tf considers all terms equally significant, it is therefore not only possible to use the term frequencies to measure the weight of the term in the paper. For finding idf we first need to find df.
$$idf(t) = log(N/ df(t))$$
where, 
df(t) = Number of documents containing term t
N = Total number of documents

* TF-IDF: The product of TF and IDF, providing a balanced measure that accounts for both the frequency of terms in a document and their rarity across the corpus. The tf-idf weight consists of two terms :- Normalized Term Frequency (tf) and Inverse Document Frequency (idf)
$$TF-IDF(t,d,D)=TF(t,d)×IDF(t,D)$$

### Applications of TF-IDF
TF-IDF is widely used in various applications in the different fields as follows:
* Information Retrieval
* Content Tagging
* Text Mining and Analysis
* Text Similarity Measurement
* Document Clustering and Classification
* Natural Language Processing (NLP)
* Recommendation Systems

### Advantages
* Simple to implement.
* Useful for information retrieval.
* Effective in highlighting important words.
* Does not require labeled data.
* Versatile across various applications.

### Disadvantages
* Ignores word order and context.
* DDoes not capture semantic relationships.
* Not effective for polysemous words. 
* Assumes independence of terms.
* Large vocabulary size can increase computational complexity.

### Working
###### Consider a simple example with three documents:

* Document 1: "the cat in the hat"
* Document 2: "the quick brown fox"
* Document 3: "the cat and the mouse"

###### Calculating TF-IDF for the term "cat":

1) TF (cat, Document 1):

* Term Frequency: 1 (appears once)
* Total Terms: 5
* TF: 1/5 = 0.2

2) IDF (cat, All Documents):

* Total Documents: 3
* Documents containing "cat": 2 (Document 1 and Document 3)
* IDF: log(3/2) ≈  0.176

3) TF-IDF (cat, Document 1):

* TF-IDF: 0.2 × 0.176 = 0.0352

By calculating TF-IDF for all terms across all documents, we can identify the most significant words in each document and understand their importance relative to the entire corpus.


### Conclusion
TF-IDF (Term Frequency-Inverse Document Frequency) is a widely used technique in text mining and information retrieval for identifying the importance of words in a document relative to a collection of documents. It effectively highlights significant terms by balancing term frequency within a document and the rarity of the term across the corpus.