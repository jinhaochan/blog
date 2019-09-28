Title: Word2Vec
Date: 2019-01-20 14:24
Author: jinhaochan
Category: Data Science
Tags: Text processing
Slug: word2vec-and-skip-gram
Status: published



In the field of machine learning, when we're dealing with text processing, we can't just read in the strings of the sentence to train our model. The model requires numerical vectors, and word embedding is a way to convert your sentences into these vectors.





There are various word embedding techniques for converting strings into vectors. Some of the common ones are:





-   Bag of Words (BoW)
-   TF-IDF
-   Word2Vec





I've briefly touched on BoW and TF-IDF in my previous posts. In this post, we're going to be looking at Word2Vec.



<!-- wp:heading {"level":3} -->

### Difference between BoW





Word2Vec is different from BoW, as BoW produces a single value for each word, which is the count of the word occurrence in the corpus. Word2Vec on the other hand, produces a vector representation for each word (as the name implies, word to vector)





Having a numerical vector tied to a single word has more benefits, as compared to a single count number. Some of the features are:





-   Cosine similarity between the vectors can indicate semantic similarity
-   The vectors produced for each word are fixed length, resulting in a low dimensional output (As compared to BoW, which results in a high dimensional and sparse vector)





As a result, it's much easier to perform machine learning related task to the condense Word2Vec representations of the word.



<!-- wp:heading {"level":3} -->

### Generating the vectors





There are two methods for generating the vectors in Word2Vec:





-   Skip-gram model
-   Continuous Bag of Words (CBoW)



<!-- wp:heading {"level":4} -->

#### Skip-gram Model





A Skip-gram is like N-gram, but instead of consecutive words, it skips around the given window.





In the example below, the windows size is 2, which is to say 2 words before, and 2 words after the target word. The Skip-gram model then picks out all combinations of word-pairs within this window, not only consecutive ones (like in N-grams)



<!-- wp:image {"id":135} -->


![placeholder]({attach}media/2018/11/training_data.png){.wp-image-135}  

<figcaption>
http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/

</figcaption>





In the skip-gram model, we're going to train a neural network  with a single hidden layer to perform the following task: Given an input word, output the probabilities of each word being "close" to the input word. This closeness is defined in a window:





We're going to throw all these word pairs in our one layer neural network, and train our model to identify nearby words for a given input word. So, the higher the frequency a pair of words occur together, the model learns this co-occurrence, and is able to give a higher probability that the word exists together.





For example, in our training set, if we feed it with many instances of the word-pair ("Apple", "Orange"), because they happen to be in many sentences such as "Apples and oranges", our model picks up this co-occurrence and gives "Orange" a higher probability. On the other hand, word-pairs like ("Apple", "Day"), which could occur in a sentence, "An apple a day keeps the doctor away" occur less frequently, and model gives "Day" a lower probability.





The catch here however, is that we're going to use the weights trained in the hidden layer of the neural network as our product, instead of the output itself. We want to use the hidden layer of the trained model to give each word a vector representation





The single hidden layer will have N number of neurons. In this example, we're going to assume N = 300, because 300 neurons was what Google used to train their Word2Vec model.





Our model will look something like this



<!-- wp:image {"id":139} -->


![placeholder]({attach}media/2018/11/presentation11.jpg){.wp-image-139}






In the training phase, one hot encoding is used for the input and outputs. During the validation phase, the inputs is a one hot encoding, while the output is a probability for each word indicating their "closeness"





Once the model is trained, we're interested only in the hidden layer. The weight matrix would be of the size (Number of words X Number of neurons), and this is actually the word vector we're looking for.



<!-- wp:image {"id":138} -->


![placeholder]({attach}media/2018/11/weightmatrix1.jpg){.wp-image-138}  

<figcaption>
Word Vector for each word, generated from the hidden layer  

</figcaption>





The feature of this word vector generated from the weight matrix is that, for similar words, their vectors would be "close" to each other (Cosine distance). This is because of the way we used word-pairs to train the model.



<!-- wp:heading {"level":3} -->

### Continuous Bag of Words





A CBoW is just a Skip-gram reversed.





The input to a CBoW is a group of context words, and the output of the model tries to predict a single word that fits into the context of all the input words.





CBoW represents the data differently



<!-- wp:code -->

``` {.wp-block-code}
"Hi fred how was the pizza?"

CBOW: 3-grams {"Hi fred how", "fred how was", "how was the", ...}

Skip-gram 1-skip 3-grams: {"Hi fred how", "Hi fred was", "fred how was", "fred how the", ...}
```

<!-- /wp:code -->



or more intuitively, 



<!-- wp:code -->

``` {.wp-block-code}
CBOW: The cat ate _____. 
Predict the target word, given the context. In this case, it’s “food”.

Skip-gram: ___ ___ ___ food.
Given the target what, what was the context around it? In this case, it’s “The cat ate”
```

<!-- /wp:code -->
