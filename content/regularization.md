Title: Regularization
Date: 2019-04-07 09:49
Author: jinhaochan
Category: Data Science
Tags: drop out, regularization
Slug: regularization
Status: published

<!-- wp:paragraph -->

One of the major problems in training a model in machine learning is overfitting. Especially when your model gets more and more complex, it starts to memorize the patterns in the training data. This makes it perform poorly on unseen data, which has new patterns.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Overfitting is the result of low-bias and high-variance, where it performs well for a single data set, but given new data, the error fluctuates. That means that the model is learning too much for each data set.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

One of the ways to overcome overfitting is Regularization

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### What is Regularization

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

The mathematical definition of Regularization is the process of adding information in order to solve ill-posed problems, or to prevent overfitting. Ill-posed meaning that the solution is highly sensitive to the changes in the data.

<!-- /wp:paragraph -->

<!-- wp:image {"id":248,"align":"center","width":238,"height":228} -->

<div class="wp-block-image">

<figure class="aligncenter is-resized">
![](https://chanjinhao.files.wordpress.com/2019/01/1280px-regularization.png){.wp-image-248 width="238" height="228"}  
<figcaption>
The blue line shows the model before regularization, while the green line shows the model after regularization.  
  
Regularization makes the model less complex.  
</figcaption>
</figure>

</div>

<!-- /wp:image -->

<!-- wp:paragraph -->

By introducing regularization, we reduce the complexity of the learned model. This means that we're reducing the accuracy of the model for a given data set, but in doing so we're making it generalize across data sets. This action reduces variance, while not changing your bias too much, and bring us to the idea situation of low-bias low-variance.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Regularization in Machine Learning

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

To put this into a machine learning context, for each model we use, we have a loss function we wish to minimize. We'll use the RSS (Residual Sum Squares) loss function in this example.

<!-- /wp:paragraph -->

<!-- wp:image {"id":249} -->

<figure class="wp-block-image">
![](https://chanjinhao.files.wordpress.com/2019/01/rss.png){.wp-image-249}  

<figcaption>
RSS loss function we want to minimize

</figcaption>
</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

This will calculate how much to adjust your parameters based on your training data. But if your training data has noise, then your parameters will be adjusted to pick up the noise, and your model will be optimized towards the noise in the data. That's overfitting.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

To combat this, we add in a regularization factor, which will shrink the estimated value to adjust your parameters. This way, your parameters won't move too much towards learning the noise in the data.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Ridge Regression (L2)

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:image {"id":250} -->

<figure class="wp-block-image">
![](https://chanjinhao.files.wordpress.com/2019/01/ridge.png){.wp-image-250}

</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

Ridge Regression adds a shrinkage quantity to the original loss function RSS. This works by preventing the change in parameters from being too high in value.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

When *λ = 0* , the penalty term is essentially taken out. Your estimated value to modify the parameters will then simply be RSS

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

When ***λ→∞***, the penalty term, the penalty term grows large, and your estimated value to modify the parameters will approach 0. (But never being 0). Because it never reaches 0, the impact of those noisy features will only be minimized, but never removed.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Lasso Regression (L1)

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:image {"id":251} -->

<figure class="wp-block-image">
![](https://chanjinhao.files.wordpress.com/2019/01/lasso.png){.wp-image-251}

</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

Lasso Regression also adds a shrinkage quantity, but the difference is that it only penalizes high valued coefficients.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The penalty term uses ***|β1|*** instead of ***β1²*** , hence it is named L1, while  
Ridge regularization is named L2.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Lasso also differs from from Ridge in that it can set coefficients to 0, making them not relevant at all. In the end, because the coefficients are 0, you may end up with lesser features, which is an advantage!

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Regularization in Deep Learning - Drop Out

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Regularization in deep learning is slightly different from shallow learning.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In deep learning, we have neurons that are for the most times fully connected. That's to say, every single neuron is connected to every other neuron in the next layer.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This may cause some problems like overfitting again, because the neurons may develop false co-dependencies among each other (which may be due to noise).

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Regularization in deep learning works by occasionally ignoring a fraction of the neurons during the training phase.

<!-- /wp:paragraph -->

<!-- wp:image {"id":252} -->

<figure class="wp-block-image">
![](https://chanjinhao.files.wordpress.com/2019/01/dropout.png){.wp-image-252}

</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->

By using dropout, you're forcing the model to learn more robust features, as opposed to random combinations of neurons. Also, it roughly doubles the number of iterations required to converge.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Conclusion

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

To conclude, we've talked about methods in shallow learning and deep learning to combat overfitting by regularization.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Regularization is the process of adding new information to reduce the value to modify the parameters. This prevents it from learning any noise that is specific to the data set, and reduce the chances of overfitting

<!-- /wp:paragraph -->