Title: What is Maximum Likelihood Estimation?
Date: 2019-04-28 09:44
Author: jinhaochan
Category: Data Science
Slug: what-is-maximum-likelihood-estimation
Status: published

<!-- wp:paragraph -->

In machine learning, we often perform what we call **parameter estimation**, which are the weights that are assigned to each feature of the input data.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

For example, in a simple linear model, we use the equation `y=mx + c` , and `m` and `c` are your parameters to be estimated. For different values of the parameters, we build different models that produce different estimations of the data

<!-- /wp:paragraph -->

<!-- wp:image {"id":286} -->


![placeholder]({attach}media/2019/01/parameters.png){.wp-image-286}  

<figcaption>
Given different parameter values, we get different models. In the case of a linear model, each model is a different line on the graph.

</figcaption>

<!-- /wp:image -->

<!-- wp:paragraph -->

Maximum likelihood is a technique for parameter value estimation.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### MLE Parameter Estimation

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Whenever we create a model with certain parameters, the outputs of the model (or the prediction) can be plotted as a probability distribution as well.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

What MLE does it to try to make the distribution of the model close to the distribution of the observed data. Intuitively, this makes the model more accurate, as it becomes more representative of the actual data.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

For example, given the following training data distribution points:

<!-- /wp:paragraph -->

<!-- wp:image {"id":287} -->


![placeholder]({attach}media/2019/01/1-z3jjgvetojmplfvmwiur3q.png){.wp-image-287}


<!-- /wp:image -->

<!-- wp:paragraph -->

We want to find out which of the graphs below has the highest probability of plotting those points. Each graph has different parameter values, and so they are plotted in different spaces on the graph.

<!-- /wp:paragraph -->

<!-- wp:image {"id":288} -->


![placeholder]({attach}media/2019/01/1-ulkl0nz1vfg6bmfiqpckzq.png){.wp-image-288}


<!-- /wp:image -->

<!-- wp:paragraph -->

Just by visual inspection, we can see that the blue line is the graph with the correct parameters that produces those data points. But of course in a machine, there is no visual inspection, only **maths**.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Calculating the MLE  

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

We want to calculate what is the total probability of observing all the generated data, or the joint probability of all the data points.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

For a single data point for an assume Gaussian distribution, we have the following equation

<!-- /wp:paragraph -->

<!-- wp:image {"id":289} -->


![placeholder]({attach}media/2019/01/1-t4zrihvhtlzjzsvcx3jrjg.png){.wp-image-289}  

<figcaption>
Probability for observing 1 point

</figcaption>

<!-- /wp:image -->

<!-- wp:paragraph -->

For 3 data points, we have the following joint probability:

<!-- /wp:paragraph -->

<!-- wp:image {"id":290} -->


![placeholder]({attach}media/2019/01/1-rfzbq614ir4zewbm3k1v0q.png){.wp-image-290}  

<figcaption>
Joint probability for observing 3 points

</figcaption>

<!-- /wp:image -->

<!-- wp:paragraph -->

This can be extended to `n` number of points

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

To calculate the MLE of the parameters, we need to find the values of the parameters in the equation that gives us the maximum value of the probability. To find the maximum, we get the differential of the equation and set it to 0, and solve for the parameters.  

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Extending the MLE to the least squares method

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

When the distribution is Gaussian, the process of finding the MLE is similar to the least squared method.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

For least squares estimation we want to find the line that minimizes the total squared distance between the data points and the regression line.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

When the data distribution is assumed to be Gaussian, the maximum probability is found when the data points get closer to the mean value.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Since the Gaussian distribution is symmetric, this is equivalent to minimizing the distance between the data points and the mean value.

<!-- /wp:paragraph -->
