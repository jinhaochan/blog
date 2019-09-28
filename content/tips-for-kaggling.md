Title: Tips for Kaggling
Date: 2019-05-12 11:31
Author: jinhaochan
Category: Data Science
Tags: Kaggle
Slug: tips-for-kaggling
Status: published



I've been doing Kaggle competitions for awhile (although with not much success), and I've learning quite a few things along the way. One of which is how to properly approach the problem, and iterate through it to climb the LB (leader board).



<!-- wp:heading {"level":3} -->

### Setting the baseline





------------------------------------------------------------------------



</p>


The first thing I would do is to use some very simple features, and build a quick model that has a relatively low bias.





I'll then use cross validation to ensure that I have low variance between train-test splits. This ensures that i'm not overfitting to any segment of the training data.





After getting a satisfactory bias and variance value, we cross our fingers, and submit our prediction to see how well it does on the LB!





There are now 3 things you need to take note of:





Cross Validation Score (CV Score)





Leader board Score (LB Score)





Difference between CV and LB Score (Your variance on the testing set)





If the difference between your CV and LB is high, you're overfitting the training data. Try to tune your model so that the difference isn't too high.



<!-- wp:heading {"level":3} -->

### Feature Generation





------------------------------------------------------------------------



</p>


Now that you got your baseline, **Do Not Modify Your Model's Parameters!**..... yet





Using parameters for the baseline model, you want to generate more features to increase your CV score. Then you make submissions to the LB to checkout your LB score. If your CV score increases, but your LB score stays the same or decreases, you're overfitting.





Here's a snippet of my comments I used to keep track of my CV/LB climb:



<!-- wp:code -->

``` {.wp-block-code}
xgb_params = {
    'max_depth': 4,  # the maximum depth of each tree
    'eta': 0.01,  # the training step for each iteration
    'silent': 1,  # logging mode - quiet
    'objective': 'multi:softprob',  # error evaluation for multiclass training
    'gamma': 0.9,
    'alpha': 0.3,
    'colsample_bytree' : 0.09,
    'subsample' : 0.09,
    'num_class': 9}  # the number of classes that exist in this datset

## Original
nfolds = 5
CV = 0.7299
std: 0.0112
LB = 0.67291

Difference = 0.05699

## changed rolling window size
nfolds = 5
CV = 0.7458
std: 0.0207
LB = 0.67995

Difference = 0.06585

## added quantile features
nfolds = 5
CV = 0.7564
std: 0.0167
LB = 0.68347

Difference = 0.07293

## dropping mean
using smaller feature set (50)
nfolds = 5
CV = 0.7670
std: 0.0243
LB = 0.69284

Difference = 0.07416

## adding iqr and trimming mean
using smaller feature set (70)
nfolds = 5
CV = 0.7740
std: 0.0257
LB = 0.69988

Difference = 0.07412
```

<!-- /wp:code -->



As you can see, my parameters are the same, and I'm only adding or removing features to push up my CV and LB



<!-- wp:heading {"level":3} -->

### Feature Selection





------------------------------------------------------------------------



</p>


Feature generation was the process of adding in new features, but using all the features (if you have a lot of them), is usually too noisy.





Most models like XGBoost and LightGBM have functions to tell you which features have the most impact on your prediction. You would want to trim your selected features to only include those high impact ones.





By doing this, I was able to push my score up just a little bit more!



<!-- wp:heading {"level":3} -->

### Parameter Tuning





------------------------------------------------------------------------



</p>


Once you're done with Feature Generation and Feature Selection, then we come to parameter tuning phase.





In this phase, we want to tune the parameters to reduce bias, variance, and CV-LB difference. You can use functions like GridSearch to efficiently search across a range of parameters



<!-- wp:heading {"level":3} -->

### Conclusion





------------------------------------------------------------------------



</p>


Baseline -&gt; Feature Generation -&gt; Feature Selection -&gt; Parameter Tuning!





This isn't a silver bullet to all competitions, but its the strategy that I use regularly.





In data science and Kaggle, there are plenty of moving parts, and it's easy to get lost in the myriad of factors affecting your prediction. It's always good to have a system to isolate and tackle the problem!


