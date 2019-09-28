Title: Model Optimizers Beyond Gradient Descent in Deep Learning
Date: 2019-02-10 09:52
Author: jinhaochan
Category: Data Science
Tags: Optimizers
Slug: model-optimizers-beyond-gradient-descent-in-deep-learning
Status: published

<!-- wp:paragraph -->

In this post, we're going to talk about the draw backs and constrains of a simple Gradient Descent algorithm when applied to Deep Learning models, and also talk about other optimization algorithms that aim to solve those problems.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

These problems mainly arise due to the complex error surface in Deep Learning models, where Gradient Descent is unable to perform as well.  

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Challenges with Gradient Descent  

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:heading {"level":4} -->

#### Too many Local Minimas  

<!-- /wp:heading -->

<!-- wp:paragraph -->

One of the problems that Gradient Descent faces is having a the algorithm converge to a local minima, instead of the true global minima. Even in a simple 2 dimensional problem, we face the issue, which gets even worse when our problem scales up to higher dimensions. But here we'll see that the local minima problem is not a huge issue with Deep Learning models.  

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The first source that contributes to a local minima is **model identifiability**. An identifiable model is a model that given an output, the weights or the structure of the network can be identified. In other words, there is a one-to-one mapping of parameters to out. If a model is non-identifiable, it means that for a given output, there exists more than one set of parameters that can produce it. **A fully connected feed-forward neural network is non-identifiable**.

<!-- /wp:paragraph -->

<!-- wp:image {"id":181,"width":435,"height":388} -->

<figure class="wp-block-image is-resized">
![placeholder]({attach}media/2018/12/multi-layer_neural_network-vector2.png){.wp-image-181 width="435" height="388"}  

<figcaption>
Different paths and connections in the neural network may give the same output. This give rise to the characteristics of being non-identifiable.

</figcaption>

<!-- /wp:image -->

<!-- wp:paragraph -->

Why this is so is because there exists a huge number of different permutations of neuron connections within the model that will produce the same output. A network with *n* neurons has *n!* possible parameter combinations.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

So why is model non-identifiability not an issue with Deep Learning models? That is because, even though the models themselves are non-identifiable, they all have the same behaviors. So given a group of non-identifiable models, they will all react the same way to the same inputs. And because of this property, there exists only a single local minima for a given non-identifiable model.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Spurious Local Minima  

<!-- /wp:heading -->

<!-- wp:paragraph -->

Another problem that a local minima can give us is being spurious. Spurious means giving false information about itself, and a spurious local minima means that the local minima incurring a higher loss function value than the true local minima. In a sense, the local minima is lying to us, and presents itself as the global minima.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

However, there has been many studies that shows that the local minima actually exhibits similar properties to the global minima, and hence, this too isn't a problem.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Wrong Directions in Gradient Descent

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:heading {"level":4} -->

#### Non-Uniform and Changing Gradients  

<!-- /wp:heading -->

<!-- wp:paragraph -->

The actual challenge to Gradient Descent as we shall see, is not the problem of local minima, but finding the right path for the algorithm to descend towards.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Intuitively, the gradient is supposed to descend towards the steepest direction, or the direction that brings the gradient value closer to zero. However, just by using this simple heuristic alone can be problematic on complex error surfaces (which is a common property of Deep Learning Models).

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

A complex error surface has the properties of uneven gradients, and hence when we move from point to point, the gradient underneath our path may possibly change. This is opposed to a simple error surface that is circular, where the gradient is constant throughout a single direction. Having this changing gradient may result in our algorithm going towards the wrong direction, because it doesn't account for the changes that happens as we are moving.  

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Mathematically, we can quantify how much the gradient changes as we are moving by calculating the second derivative. This can be captured by calculating how much the gradient as w2 changes as we change the value of w1, and we store this value in a Hessian Matrix. And a Hessian Matrix that tells us the gradient changes as we move, is called an **ill-conditioned** matrix.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Calculating this Hessian matrix turns out to be extremely expensive if we do it at each step, and so to tackle the problem of changing gradients, we factor in the **momentum** parameter.  

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Momentum-Based Optimization  

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Earlier, we stated that we may go into the wrong direction because we don't account for changing gradients, and also, if we decide to account for changing gradients using second derivatives, calculating a Hessian Matrix is extremely expensive.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The solution to this is instead of calculating the Hessian Matrix at every optimization step, we factor in the value of the previous gradient into the calculation of the current gradient. By taking into account of the previous gradient value to find the current gradient, the fluctuations of gradient value is drastically reduced.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This approach of remembering previous gradients is called **Momentum**. This technique is analogous to taking a moving average of stock prices the market  

<!-- /wp:paragraph -->

<!-- wp:image {"id":178} -->


![placeholder]({attach}media/2018/12/movingaverage.gif){.wp-image-178}  

<figcaption>
Fluctuations in the stock market price are reduced by looking at the averag

</figcaption>

<!-- /wp:image -->

<!-- wp:paragraph -->

We can thinking of the wildly fluctuating gradients at each point being represented by the green line, while the average is represented by the yellow line. Momentum based optimizers use the yellow line to calculate the change in gradient.  
  

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Conclusion

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

To conclude this post, we have seen how there are problems applying simple gradient descent to complex error surfaces that are present in Deep Learning models.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Local minimas are not a problem, but changing gradients due to its complex surface are a problem. To try to factor in changing surfaces, we could calculate the Hessian Matrix, but that turns out to be extremely expensive.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

As a solution, we use Momentum based optimizers instead, which factors in previous gradient values to the calculation of the current gradient.  

<!-- /wp:paragraph -->
