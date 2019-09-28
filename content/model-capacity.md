Title: Model Capacity
Date: 2019-03-24 20:19
Author: jinhaochan
Category: Data Science
Tags: Capacity, VC Dimension
Slug: model-capacity
Status: published

<!-- wp:paragraph -->

While studying the book Deep Learning by Ian Goodfellow, I came across this concept of model capacity, and it was really intuitive in helping me understand the models representation of a given problem.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This ties to the concept of overfitting and underfitting

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Capacity

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Put simply, the capacity of the model is the complexity of the model, or the ability to represent complex relationships.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

A model with high capacity can represent very complex relationships, while a model with low capacity can represent not so complex relationships

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### How it ties to Overfitting and Underfitting

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Models perform best when their capacity approximately captures the complexity of the task they need to perform.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

If the task or data set has a very low complexity, but the model has a very high capacity, the model will overfit, as it will memorize and represent all the features in the training set that may not be in the testing set.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Conversely, if the task or data set is highly complex, but the capacity of the model is low, the model will underfit, as it cannot sufficiently represent the complex relationships and features in the training data

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Vapnik–Chervonenkis (**VC**) **dimension**

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

The VC dimension is a measurement of a model's capacity, given that the task at hand is a binary classification problem.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The numerical value of a VC dimension tells us the largest set of data point the model can perfectly classify (or shatter). Thus, the larger the VC dimension, the more data points the model is able to perfectly classify, which also means that the model is inherently more complex.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The usage of a VC dimension usually just tells us how complex an algorithm is. A model with a higher VC dimension requires more data to properly train due to the higher complexity.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Conclusion

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

The take away here is that, overly complicated models are not always better as they can overfit. A simple decision tree or random forest can be perfect for data with low complexity.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

A VC dimension is simply a quantification of how complex a model is. Higher VC = Able to separate more data points = more complex = requires more training data.

<!-- /wp:paragraph -->
