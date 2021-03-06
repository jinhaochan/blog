Title: Text Processing
Date: 2019-01-13 18:41
Author: Chan Jin Hao
Category: Data Science
Tags: Text processing
Slug: text-processing
Status: published



In this post, we're going to be exploring some typical methods for text processing for machine learning. When we're talking about machine learning with text, there are several areas of interest including 





-   Sentiment Analysis
-   Question Answering
-   Information Retrieval





Before we do that, we must first understand that a machine learning model only takes in numerical values, or vectors, and not strings in the text. The problem now is how do we transform the collection of strings into vectors of numbers.





There are several pre-processing steps, and we'll take a look at them below.



<!-- wp:heading {"level":3} -->

### Tokenization





Tokenization is splitting up the sentence into to words or phrases.





There's Sentence Tokenizing, and Word Tokenizing, both of which are apparent in what they do. We'll mostly be using Word Tokenizing to split up a sentence in its constituent words. The example below uses NLTK's word\_tokenize





`from nltk.tokenize import word_tokenize >>> string = "Hello! I am a sentence!" >>> word_tokenize(string ) ['Hello', '!', 'I', 'am', 'a', 'sentence', '!']`



<!-- wp:heading {"level":3} -->

### Normalization





Once the sentence has been broken up into it's words, we need to normalize it, so as to remove any unwanted meaning attached to features like capitalization. This process transforms the words, and picks out useful features.





There are several common methods for normalization:





-   Lemmatization
-   Stemming
-   Capitalization
-   Special Characters
-   Stopwords





Lemmatization and Stemming are pretty similar, where they both transform the words into their generalized forms. The difference is in how they change the word.



<!-- wp:table -->

  ---------- --------------- ----------
             Lemmatization   Stemming
  Studying   Study           Study
  Studies    Study           Studi
  ---------- --------------- ----------

<!-- /wp:table -->



Stemming removes any suffixes, leaving behind it's inflected word. The outcome is not always desirable as you can see, cutting the -es from Studies. One common stemmer is the Porter stemmer, which reduces the words to its 'root' form.





Lemmatization on the other hand is smarter, and uses linguistics to reduce the word to it's base meaning. 'Studies' and 'Studying' both have the same base meaning of 'Study'. However, before you can apply lemmatization, you need to have a trained dictionary for that language to discover what is the base meaning. Luckily for us, the English language has many of such dictionaries.





Capitalization and Special Characters transformation is simply turning all the words into lowercase, and removing non-alphabet characters





`>>> sentence = sentence.lower() >>> sentence = re.sub('[^a-zA-Z]',' ',sentence)`





Stopwords removal is a method for removing common stopwords in a text. Stopwords carry little to no meaning to them, and are sentimentally agnostic, hence they should be removed so as not to generate too much noise in our matrix. A list of common stopwords can be found in [NLTK's collection](https://gist.github.com/sebleier/554280)



<!-- wp:heading {"level":3} -->

### Transforming Tokens to Vectors



<!-- wp:heading {"level":4} -->

#### Bag of Words





Once we have our collection of pre-processed tokens, we now need to transform them into features, or numeric vectors for us to fit into our model





A Bag of Words (BoW) model is one way to quantize the text into numerical information. It is also called Text Vectorization, because we're converting a sentence into a numerical vector.





BoW captures the counts of the words in a sentence 



<!-- wp:code -->

``` {.wp-block-code}
John likes to watch movies. Mary likes movies too.

"John","likes","to","watch","movies","Mary","likes","movies","too"

{"John":1,"likes":2,"to":1,"watch":1,"movies":2,"Mary":1,"too":1}
```

<!-- /wp:code -->



The downside of BoW model is that we lose word order, which is important when it comes to sentiment analysis. The ordering of the words in a sentence can produce very different meanings





"not all apples are bad"





"all apples are not bad"





The former implies that not every single apple is bad, but there can be bad ones. The latter implies that every single apple is not bad, which means there are no bad ones.





Also, BoW counts are not normalized, which loses another feature of word importance. Words that occur very frequently such as stopwords hold little weight if they appear multiple times, and in every document. We want words that are rare, and occur less frequently. These words will have stronger features.



<!-- wp:heading {"level":4} -->

#### TF-IDF





After we have the collection of words generated from BoW, we can count the frequency of the word, and the presence of the word in a given document. This  technique is called Term-Frequency - Inverse Document Frequency (TF-IDF) model.





This is calculated by counting the number of times the word appears in all documents (TF), and the number of documents this word appears in (DF). We take the inverse of DF (IDF), because we don't want words that appear too frequently in all documents. 





A word with a high TF-IDF indicates a high term frequency, low document count. This highlights important issues in a document, but that are not shared across the whole corpus



<!-- wp:heading {"level":4} -->

#### N-Grams





The BoW model grows linearly with each distinct vocabulary. With every new word added, the vector size increases by 1. This leads to an extremely spares and high dimension vector. To attempt to reduce the dimensions, we group words together into what we call N-grams, where N is the number of words in the group.





N-grams are an improvement because it reduces the dimensionality of the vector, and it also captures context from the surrounding words.





Below shows a 2-gram representation of a sentence:



<!-- wp:code -->

``` {.wp-block-code}
John likes to watch movies. Mary likes movies too.

"John likes"
"likes to"
"to watch"
"watch movies"
"movies Mary"
"Mary likes"
"likes movies"
"movies too"
```

<!-- /wp:code -->



We should be careful however, in choosing the appropriate value of N. If we generate too much N-grams (N is small), we end up generating too much noise.





After the N-gram collection is generated, we can future refine the selection with the heuristic:





-   Remove high and low frequency n-grams
-   High Frequency n-grams = Stop words
-   Low Frequency n-grams = Rare words
-   Keep medium frequency n-grams



<!-- wp:heading {"level":3} -->

### Training a Model with the Vectors





Once we have pre-processed the sentences to tokens, and vectorized them into numerical values, we can use those vectors to train our models to answer our questions.


