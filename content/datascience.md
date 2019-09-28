Title: Kaggle Data Science
Date: 2018-10-31 22:11
Author: jinhaochan
Slug: datascience
Status: published

<!-- wp:paragraph -->

I'm branching out my learning into Data Science, mostly from Kaggle.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

You'll find my Kaggle kernels here.

<!-- /wp:paragraph -->

<!-- wp:heading -->

Predicting Taxi Fare
--------------------

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

<https://www.kaggle.com/c/new-york-city-taxi-fare-prediction>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Notebook: <https://github.com/jinhaochan/TaxiFare/blob/master/Taxi%20Fares.ipynb>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

**RMSE: 3.88522**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

**Model: XGBoost**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In this problem, I was supposed to predict taxi fares in NYC. It can be modeled as a regression problem.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

There was a lot of data cleaning to do, with many odd numbered features such as passenger size, and coordinates on the water.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Without the airport features, my model has an RMSE of 4.14398. After adding in those features, it drastically dropped to 3.88522. Those are some really strong features!

<!-- /wp:paragraph -->

<!-- wp:heading -->

Movie Sentiment Analysis
------------------------

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

<https://www.kaggle.com/c/movie-review-sentiment-analysis-kernels-only>[](https://www.kaggle.com/earthshaker/lstm-cnn-glove-bidirectional-gru-aggregation)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Notebook: [https://github.com/jinhaochan/SentimentAnalysis/blob/master/sentanalysis.ipynb](https://github.com/Charmanderander/SentimentAnalysis/blob/master/sentanalysis.ipynb)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

**Accuracy: 0.65095**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

**Model: Ensemble by Voting**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In this problem, we were given a collection of phrases, which were broken down from sentences. Instead of predicting the sentiment for each sentence, we had to predict the sentiment for each phrase.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The pre-processing steps I did were

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Lower casing
2.  Removing non alphabets
3.  Lemmatization

<!-- /wp:list -->

<!-- wp:paragraph -->

The final output for each phrase was then chosen by voting from all the models.

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  LSTM
2.  CNN
3.  Glove Transfer-Learning with Bidirectional GRU

<!-- /wp:list -->

<!-- wp:paragraph -->

Interestingly enough, Glove + CNN performs poorer than just CNN. This may be because the word vectors trained in Glove were in a different context (i.e. not Movie Sentiment Analysis)

<!-- /wp:paragraph -->

<!-- wp:heading -->

Predicting Future Sales
-----------------------

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

<https://www.kaggle.com/c/competitive-data-science-predict-future-sales>

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Notebook: [https://github.com/jinhaochan/salesforcast/blob/master/saleforecast.ipynb](https://github.com/Charmanderander/salesforcast/blob/master/saleforecast.ipynb)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

**RMSE: 1.16462**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

**Model: LSTM + GRU**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In this competition, we had to predict what the next month's sale was for each item for each shop.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The data given to us was daily sales for each item, so we had to do some data aggregation to convert it to a monthly sales value.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

We were given 33 months of training data, so I modeled it to a time series problem.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

For training, months 0 - 32 was the training data, and month 33 was the target value.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

For testing, months 1 - 33 was the testing data, and we need to predict the values for month 34.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The model I used was a 2 layer GRU using a dropout layer of 0.3  

<!-- /wp:paragraph -->
