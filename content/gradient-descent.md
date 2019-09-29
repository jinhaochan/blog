Title: Gradient Descent
Date: 2019-02-03 20:10
Author: Chan Jin Hao
Category: Data Science
Tags: Gradient Descent
Slug: gradient-descent
Status: published



A machine learning model consists of weights, and those weights, given a set of inputs, are used in the calculation process to produce a prediction. The prediction is then fed into a loss function, to calculate the the total error. Using this error, we feed it into an optimization algorithm, which goes back to the model and tweaks the weights.





This tweaking process is the learning, and how we do the tweaking is optimization algorithm.





There are a few popular ways to perform weight tweaking and model optimization, that is, how do we decide how to tweak the weights. In this post, we're going to be talking about Gradient Descent.



<!-- wp:heading {"level":3} -->

### Gradient Descent





------------------------------------------------------------------------






In our model, assume we have 2 weights, w1 and w2, for optimization.





We can plot all possible weights w1 and w2 can have, to all possible errors on a graph, and this will produce an bowl shape, where the bottom of the bowl corresponds to the lowest possible error.



<!-- wp:image {"id":165} -->


![placeholder]({attach}media/2018/11/gradient_descent_method.png){.wp-image-165}  

<figcaption>
The X and Y axis represents the values of w1 and w2.  
The Z axis represents the values of the error.

</figcaption>





What we're tweaking here are the values of  w1 and w2. When we start shifting the values around the X and Y axis, the point on the bowl shape also shifts correspondingly. The goal here is to tweak the values of w1 and w2 such that the point on the bowl rests directly at the bottom, which has the lowest error value.





So how do we know, at each point of time on the bowl shape, where do we move to? Here's where we calculate the gradient of that point of the bowl. At the bottom of the bowl, the gradient will be 0, because it'll be a horizontal surface. All other points on the bowl will have a non-zero gradient value.



<!-- wp:image {"id":166} -->


![placeholder]({attach}media/2018/11/512px-gradient_descent-svg.png){.wp-image-166}  

<figcaption>
Top down view of the bowl. As we shift w1 and w2 around, the point on the bowl shifts as well. We want the point to slowly traverse towards the center, where error is minimized.

</figcaption>





The heuristic we'll use is to a new point such that the new gradient value on the bowl is getting smaller. This is the idea of descending gradient, until it reaches a minimum.





One hyper-parameter we can tune in our optimization algorithm is how fast the point moves. That is to say, at each descent step, how far away should the new point be. A big step might get you to the bottom faster, but you might end up overshooting, and be perpetually oscillating around the bottom, never reaching the end. A small step on the other hand will take a much longer time. This distance of each descent step is called the **learning rate**.





In mathematical terms, Gradient Descent is the partial derivative of the error or loss function, with respect to the weights.



<!-- wp:heading {"level":3} -->

### Stochastic Gradient Descent





------------------------------------------------------------------------






The process we described above is the vanilla way of doing Gradient Descent, and it's called **Batch Gradient Descent**. This means that we take all the possible data points in a single batch, and compute the error surface, or the bowl.





In reality, the error surface isn't always so smooth in the shape of a bowl, but may consist several saddle points. Saddle points are points on the graph that are almost horizontal, but it's not the true minimum of the graph. This can lead to an issue of early stoppage, where our Gradient Descent thinks it has found the lowest point on the error surface.



<!-- wp:image {"id":167} -->


![placeholder]({attach}media/2018/11/saddle_point-svg.png){.wp-image-167}  

<figcaption>
The point stops at a saddle point, which has a zero gradient as well. Clearly that is not the lowest point on the graph, and our algorithm has prematurely halted.  

</figcaption>





One of the solutions to this is **Stochastic Gradient Descent**. In batch, we take all possible data points and plot the error surface. In Stochastic, we only use one single data point, and we estimate the error surface. The result is a dynamic error surface, which decreases the chance of us encountering a saddle point.





The downside to Stochastic Gradient Descent is that we're performing an estimation of the error surface based only on 1 point, which may not be an accurate representation of the error surface.





And the obvious solution to this is called **Mini-Batch Gradient Descent**, where instead of performing the error surface estimation based on one point, we use a group of points, or mini batches.



<!-- wp:heading {"level":3} -->

### Conclusion





------------------------------------------------------------------------






To recap, in this post we've talked about one of the optimization algorithm, Gradient Descent. This algorithm tells you how to tweak your weights to minimize the loss function of your model.





There are three models, each improving on the other:



<!-- wp:list {"ordered":true} -->

1.  Batch Gradient Descent: Plots the error surface based on all points. This might lead to early convergence on saddle points.
2.  Stochastic Gradient Descent: Estimates and plots the error surface based on a single point. This leads to a poor estimation of the error surface.
3.  Mini-batch Gradient Descent: Uses small batches of the data set to perform the error surface estimation.


