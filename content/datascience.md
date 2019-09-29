Title: Kaggle Data Science
Date: 2018-10-31 22:11
Author: Chan Jin Hao
Slug: datascience
Status: published



I'm branching out my learning into Data Science, mostly from Kaggle.





You'll find my Kaggle kernels here.





Predicting Taxi Fare
--------------------





------------------------------------------------------------------------






<https://www.kaggle.com/c/new-york-city-taxi-fare-prediction>





Notebook: <https://github.com/Chan Jin Hao/TaxiFare/blob/master/Taxi%20Fares.ipynb>





**RMSE: 3.88522**





**Model: XGBoost**





In this problem, I was supposed to predict taxi fares in NYC. It can be modeled as a regression problem.





There was a lot of data cleaning to do, with many odd numbered features such as passenger size, and coordinates on the water.





Without the airport features, my model has an RMSE of 4.14398. After adding in those features, it drastically dropped to 3.88522. Those are some really strong features!





Movie Sentiment Analysis
------------------------





------------------------------------------------------------------------






<https://www.kaggle.com/c/movie-review-sentiment-analysis-kernels-only>[](https://www.kaggle.com/earthshaker/lstm-cnn-glove-bidirectional-gru-aggregation)





Notebook: [https://github.com/Chan Jin Hao/SentimentAnalysis/blob/master/sentanalysis.ipynb](https://github.com/Charmanderander/SentimentAnalysis/blob/master/sentanalysis.ipynb)





**Accuracy: 0.65095**





**Model: Ensemble by Voting**





In this problem, we were given a collection of phrases, which were broken down from sentences. Instead of predicting the sentiment for each sentence, we had to predict the sentiment for each phrase.





The pre-processing steps I did were



<!-- wp:list {"ordered":true} -->

1.  Lower casing
2.  Removing non alphabets
3.  Lemmatization





The final output for each phrase was then chosen by voting from all the models.



<!-- wp:list {"ordered":true} -->

1.  LSTM
2.  CNN
3.  Glove Transfer-Learning with Bidirectional GRU





Interestingly enough, Glove + CNN performs poorer than just CNN. This may be because the word vectors trained in Glove were in a different context (i.e. not Movie Sentiment Analysis)





Predicting Future Sales
-----------------------





------------------------------------------------------------------------






<https://www.kaggle.com/c/competitive-data-science-predict-future-sales>





Notebook: [https://github.com/Chan Jin Hao/salesforcast/blob/master/saleforecast.ipynb](https://github.com/Charmanderander/salesforcast/blob/master/saleforecast.ipynb)





**RMSE: 1.16462**





**Model: LSTM + GRU**





In this competition, we had to predict what the next month's sale was for each item for each shop.





The data given to us was daily sales for each item, so we had to do some data aggregation to convert it to a monthly sales value.





We were given 33 months of training data, so I modeled it to a time series problem.





For training, months 0 - 32 was the training data, and month 33 was the target value.





For testing, months 1 - 33 was the testing data, and we need to predict the values for month 34.





The model I used was a 2 layer GRU using a dropout layer of 0.3  


