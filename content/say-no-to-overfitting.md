Title: Say NO to Overfitting!
Date: 2019-05-05 13:58
Author: jinhaochan
Category: Data Science
Tags: Overfitting
Slug: say-no-to-overfitting
Status: published

<!-- wp:paragraph -->

Just some experience I've encountered while working on a very small data set of 1703 training samples, and 1705 testing samples.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

One way to combat overfitting is to use cross validation. While doing so, it's important for you not to just look at the final validation score, but also observe the training process itself.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

If we just look at the final CV result, we see an astounding `~92%` accuracy. This should raise some alarms that shout "Overfitting!". And this is an accurate observation, because when submitted to the Kaggle leader board, it got a measly `0.64`, which was below the baseline! And more horribly, the difference between CV and LB score is `~30%`

<!-- /wp:paragraph -->

<!-- wp:image {"id":294} -->

<figure class="wp-block-image">
![placeholder]({attach}media/2019/01/xgb2.png){.wp-image-294}

</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

We can also observe the huge disparity between the training error and validation error. A training error of `0%`? And validation error of `~8%`? Something is really wrong.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Preventing overfitting in XGB

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Since I've used XGBoost, there are several techniques available to combat overfitting, such as regularization, maximum depth of tree and bagging fractions. After applying all of those, I get a final CV score of `~74%`, but if we observe the disparity between the training error and validation error, the difference is only `~2%`!

<!-- /wp:paragraph -->

<!-- wp:image {"id":293} -->

<figure class="wp-block-image">
![placeholder]({attach}media/2019/01/xgb1.png){.wp-image-293}

</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

After uploading that to the leader board, I see my score rise up to `0.69`. The difference between my CV score and the LB is drop drastically from `~30%` to `~3%`! Classic example of overfitting.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Aside from feature engineering, a lot of effort should also go into ensuring your model is not too complex for very simple data.

<!-- /wp:paragraph -->
