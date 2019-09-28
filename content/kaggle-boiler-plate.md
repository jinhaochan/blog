Title: Kaggle Boiler Plate
Date: 2018-12-16 21:33
Author: jinhaochan
Category: Data Science
Slug: kaggle-boiler-plate
Status: published

I've been playing around with Kaggle competitions for a while, and there are usually quite a few steps to perform.

I've compiled a list of them below, in sequential order. These are by no means hard and fast rules, but simple heuristics to follow!

I've added links here and there to guide you a long.

Importing your libraries
========================

------------------------------------------------------------------------

You're gonna have to import the usual `pandas` and `sklearn` to do your dataframe manipulations, and machine learning stuff.

Aside from those, you'll likely be importing other stuff that are relevant in transforming your data.

Reading in training data and testing data
=========================================

------------------------------------------------------------------------

When you first start the project, the first thing you want to do is to read in the data. It's usually named `train.csv` and probably contains a few million lines.

You most probably won't be able to read in all the data at once, so you're gonna have to read in just a few lines to get a preview.

`df_train = pd.read_csv("train.csv", nrows=1000000)`

Of course when you're doing the actual training of the model, you're going to have to read in the whole thing!

We also read in the test set, usually called `test.csv`. The reason why we're reading in the test set, is so that when we perform feature creation and data massaging, we can do it both on the test and train data.

Visualizing data
================

------------------------------------------------------------------------

You're going to want to visualize the data you've read in to analyze for any outliers, or obvious trends that can be helpful in feature creation.

For univariate analysis, I usually apply barchart, or histogram, while for bivariate analysis, I'll apply a scatter plot.

### Univariate Analysis

<https://www.kaggle.com/residentmario/univariate-plotting-with-pandas>

### Bivariate Analysis

<https://www.kaggle.com/residentmario/bivariate-plotting-with-pandas>

Cleaning data
=============

------------------------------------------------------------------------

After visualizing your data, you'll more or less know the upper or lower bounds, outliers, and whats considered to be normal.

You must now remove those values that lie outside those normal ranges. There are a common data abnormalities which are:

1.  Outliers
2.  Missing values

Some examples are: Taxi fares with negative values, coordinates that plot on the ocean, Null or NaN values, and many more.

You want to be cleaning your data BEFORE training your model. If not, there will be unnecessary noise. You'll end up with a few lesser rows than your original training set.

However, DO NOT CLEAN YOUR TESTING SET. The testing set is supposed to be untouched, aside from feature engineering.

Feature Engineering
===================

------------------------------------------------------------------------

After looking at your data, you will definitely need to engineer some features on your own. Doing this allows you to find features that correlated more strongly with the value you're predicting.

We have 2 types of data type: Continuous and Discrete, and each of the data types have to be handled differently when doing feature engineering

Continuous data runs in infinite ranges, while Discrete data are things that fall into categories.

Example of Continuous data are prices, age and temperature. Strings are also considered Continuous data

Examples of Discrete data are gender and types of cars.

### Continuous Data Feature Engineering

For continuous data, we can bin the data into intervals.

An example would be age group, where individual ages might be too scattered, but by grouping them in multiples of 5s or 10s, you might get a better representation.

    [code lang="text"] 51-55 = Group 1 
    56-60 = Group 2 
    61-65 = Group 3 
    [53, 55, 56, 59, 60, 61, 62, 64] = [1, 1, 2, 2, 2, 3, 3, 3] [/code]

For strings, we need to extract out relevant data that can be represented in numeric form. One example is parsing of the dates. In your original data, you're given a datetime string, which isn't helpful at all. You'll want to engineer features such as the day of the week, the hour, month, year, or even the seconds. These numerical features are much more helpful as compared to a string value.

### Discrete Data Feature Engineering

For discrete data, the categories in the data can be one-hot-encoded. The reason why we do that is because when we change the categories to numeric values, we don't want to accidentally imply meaning and hierarchy between the numbers.

For example if we have 5 different categories of cars, and we change them numerically to 0, 1, 2, 3, 4, the machine may end up learning that the 4th category is more important than the 0th category, based on the simple fact that 4 is greater than 0.

So to prevent this problem of false importance, we use one-hot-encoding. The idea of one-hot-encoding can be visually represented as such

![placeholder]({attach}media/2018/12/mtimfxh.png?w=300){.alignnone .wp-image-170 width="560" height="220"}

This way, the categories are represented as 1s and 0s, which minimizes the possibility of learning false importance.

We should take note that one-hot-encoding should be done on your train and test set combined. The reason why we want to do this is so we don't miss out data that is in the test and not in the train, vice-versa. If there is missing data, and we perform one-hot-encoding separately on the train and test, we will end up with missing columns, as one-hot-encoding does not generate them.

### Feature Interaction

There is also Feature interaction, where two or more features are correlated or have interactions between each other. We can capture this interaction between two features by creating a new feature, which is a multiplication of these two correlated features.

Splitting of Data
=================

------------------------------------------------------------------------

Once you've cleaned your data and created your features, you can now start training your model! But before you do that, you first need to split your data in a train and test set. This is for performing a validation test to evaluate your model.

`X_train, X_test, y_train, y_test = train_test_split(df_train, y, test_size=0.2)`

Where `y` is your target value to predict.

The way you use these values are:

1.  `X_train` and `y_train` for training the model
2.  Feed `X_test` to your model
3.  Evaluate the output with `y_test`

Scaling Data
============

------------------------------------------------------------------------

Because not all of your data will be in the same scale, we have to normalize them all to be of the same scale.

For example, the scale for age can range from 0-90, while a pay range can go from 2000 - 10,000. This is bad for machine learning, because the model might attribute a hidden (but wrong) meaning to this difference in range.

0 - 90 has a small range, while 2000 - 10,000 has a larger range.

How we scale this is by using sklearn packages such as MinMax scaling.

A potential problem to scaling is having data leakage, where we learn some attributes from the testing data set into the training dataset.

How we overcome the problem of data leakage is to perform fit-transform on the training set, and only perform transform on your testing set

Training
========

------------------------------------------------------------------------

You got to first identify if you're solving a classification or a regression problem, and a supervised or unsupervised problem.

`sklearn` provides a wide range of models for you to pick from.

Models for Supervised learning in `sklearn`: <http://scikit-learn.org/stable/supervised_learning.html>

Models for Unsupervised learning in `sklearn`: <http://scikit-learn.org/stable/unsupervised_learning.html>

There's an overpowered model right now called XGBoost, but I highly recommend using it AFTER you've played around with other models. This is to allow you to have an understanding of how other models work, because XGBoost is definitely not a silver bullet.

Installing XGBoost is a little bit tricky, because its an external library.

If you're using Windows, these are the steps I followed: <https://www.ibm.com/developerworks/community/blogs/jfp/entry/Installing_XGBoost_For_Anaconda_on_Windows?lang=en>

And the Linux version:

    [code lang="text"]
    $ pip install xgboost
    $ git clone https://github.com/dmlc/xgboost# cd xgboost-master
    $ make
    $ cd python-package/
    $ python setup.py install
    [/code]

You can now `import xgboost`

See how much easier it is on Linux.

Validation
==========

------------------------------------------------------------------------

Once your model is trained, you would need to validate the output with `y_test`. `y_test` contains the true values, while your model outputs a set of predicted values.

Again, `sklearn` provides a suite of tools for performing evaluation, depending on what model you were using: <http://scikit-learn.org/stable/modules/model_evaluation.html>

If you get a bad score here, you'll want to revisit your feature engineering, or data cleaning again to see what you can do differently. Remember, more features != better model!

Prediction
==========

------------------------------------------------------------------------

Pump in the testing set into your model you trained, and get a set of output values. There'll be no evaluation on your side here. Evaluation will be done by Kaggle once you submit them. This is essentially your answer to their problem.

Writing to CSV
==============

------------------------------------------------------------------------

Kaggle usually provides a file called `sample_submission.csv` to show you the format with the competition requires for submission.

Transform your answers to fit into that model, then write the answers to CSV for submission

`​​​​​df.to_csv("my_submission.csv", index=False)`

I notice that you'll want to include `index=False` to exclude the row numbers in the dataframe

Submit Your Entry
=================

------------------------------------------------------------------------

That's it! Go on and submit your entry to Kaggle, and see how you rank against other Kagglers. Don't be disheartened if you didn't perform well, it takes a few iterations to improve your model.

Also, don't be afraid to read up on other people's kernels to gain inspiration!

<!-- wp:image -->


<img alt></img>



