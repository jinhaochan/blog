Title: LightGBM
Date: 2019-03-24 12:33
Author: jinhaochan
Category: Data Science
Slug: lightgbm
Status: published

<!-- wp:paragraph -->

For some time, XGBoost was considered the Kaggle-Killer, being the winning model for most prediction problems. Recently Microsoft released their own gradient boosting framework called LightGBM, and it is way faster than XGB. In this post, I'm going to touch on the interesting portions of LightGBM.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### What is LightGBM?

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Similar to XGBoost, LightGBM is a gradient boosted tree based algorithm. Unlike other gradient boosted trees which grows hroizontally, LightGBM grows vertically. LightGBM grows Leaf-wise, while others grow Level-wise.

<!-- /wp:paragraph -->

<!-- wp:image {"id":227} -->


![placeholder]({attach}media/2018/12/1-AZsSoXb8lc5N6mnhqX5JCg-1.png){.wp-image-227}  

<figcaption>
LightGBM leaf-wise growth. This allows for deeper vertical growth

</figcaption>

<!-- /wp:image -->

<!-- wp:image {"id":228} -->


![placeholder]({attach}media/2018/12/1-whSa8rY4sgFQj1rEcWr8Ag-1.png){.wp-image-228}  

<figcaption>
Other gradient boosted algortihms grow level wise, which results in longer horizontal growth

</figcaption>

<!-- /wp:image -->

<!-- wp:heading {"level":3} -->

### Dealing with Non-Numeric Data

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

The nice thing about LightGBM is that it can take in data as a whole, and it does not require inputs to be converted into numerical format! This means that if your data has a mix of numbers and strings, you can simply throw everything into the model to learn.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The one thing you have to do however, is to specify the string columns as `category`. Below is a example of how we do it with Pandas Dataframe

<!-- /wp:paragraph -->

<!-- wp:code -->

``` {.wp-block-code}
dtypes = {
        'MachineIdentifier':'category',
        'ProductName': 'category',
        'EngineVersion': 'category',
        'AppVersion':'category',
        'AvSigVersion':'category',
        'IsBeta':'int8',
        'RtpStateBitfield':'float16',
        'IsSxsPassiveMode':'int8'
}

df_train = pd.read_csv('train.csv', nrows=2000000, dtype=dtypes)
```

<!-- /wp:code -->

<!-- wp:paragraph -->

Or if you're creating new features, you have to recast the datatype of the new column to categories

<!-- /wp:paragraph -->

<!-- wp:code -->

``` {.wp-block-code}
for feature in newFeatures:
    Train[feature ] = Train[feature ].astype('category')
```

<!-- /wp:code -->

<!-- wp:heading {"level":3} -->

### Important Parameters to Tune

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

LightGBM has a huge array of parameters to tune, and I wont be listing them here. I will however be highlighting those I think are important, and has helped me increase my model predictions

<!-- /wp:paragraph -->

<!-- wp:list -->

-   `max_depth`: Defines how deep the tree grows
-   `num_leaves`: Defines the maximum number of leaves in a node
-   `max_bin`: Defines the maximum number of bins your feature will be bucketed in

<!-- /wp:list -->

<!-- wp:paragraph -->

For a more comprehensive read, [click here!](https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html)

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Conclusion

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

In this short post, we've very briefly covered about LightGBM, how it is different from other gradient boosted machines, and how to define categories for training.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

An important thing to know is that LightGBM is very sensitive to overfitting, and should not be used for small data sets &lt;10,000 rows.

<!-- /wp:paragraph -->
