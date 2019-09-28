Title: Branches of Machine Learning
Date: 2019-06-02 15:30
Author: jinhaochan
Category: Review
Slug: branches-of-machine-learning
Status: published

<!-- wp:paragraph -->

Just finished reading the book "The Master Algorithm", where the author tries to find the ultimate Machine Learning algorithm that can solve different varieties of problems (text, image, predictive, time series etc)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In the book, he goes over the 5 main branches (or tribes) of Machine Learning. They are:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  The Evoluntionaries
2.  The Connectionist
3.  The Symbolist
4.  The Bayesians
5.  The Analogizers

<!-- /wp:list -->

<!-- wp:image {"id":323,"align":"center"} -->

>


![placeholder]({attach}media/2019/02/master-algo_thumb.png){.wp-image-323}




<!-- /wp:image -->

<!-- wp:paragraph -->

Lets look at what the 5 tribes have to offer, and their each individual "Master Algorithm"

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### The Evolutionaries

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Master Algorithm: **Genetic Algorithm**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Loss Function: **Fitness Function**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Optimization Function: **Genetic Search**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This tribe tries to represent learning by mimicking evolution, where the it uses survival-of-the-fittest idea to pick the best model.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Starting with weak and not-fit models, the models go through different biologically inspired evolutionary stages: Mutation, Cross Over and Selection

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Evolutionaries focus on learning the structure of the model, and not so much of the parameters (something which Connectionist with neural networks focus on)

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### The Connectionists

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Master Algorithm: **Neural Networks**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Loss Function: **RMSE**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Optimization Function: **Gradient Descent and Back Propagation**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The Connectionist represent learning by modelling it after the brain and the neuron connections inside them. Dendrites, Axons and the Cell made up the Neural Network.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In Neural Networks, we are trying to learn the weights of the connections between the cells, and not the structure of the neural network itself (Perhaps there could be a combination of GA and NN, where GA finds the structure, and NN finds the weights)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

It follows the notion that a concept can be represented by firing various neurons, and concepts that are similar to each other will cause the same set of neurons firing.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### The Symbolist

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Master Algorithm: **Logic**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Loss Function: **Accuracy**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Optimization Function: **Inverse Deduction**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Symbolist believe that all intelligence can be reduced to symbols, or rules. They build rule base systems, which obviously have huge limitations, because we can't possibly convert all intelligence and edge cases to a hard coded rule. The moment the rule encounters just a slightest bit of noise, it fails to perform.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Also, real life scenarios and concepts are seldom defined in black and white rules, and are usually stochastic and in the grey area.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In some cases, they can perform quite well. A model that Symbolist use are decision trees, which are huge tree that have if-else rules at each branch.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### The Bayesians

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Master Algorithm: **Graphical Models**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Loss Function: **Posterior Probability**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Optimization Function: **Probabilistic Inference**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

As opposed to frequentist, which gives no value to prior beliefs, Bayesians hold prior beliefs at the center of their model.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The Bayesian works on conditional probability, or Bayes Theorem, that tells the probability of event A happening given that B has occurs `P(A|B)`.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

During the training phase, the model takes the training data to build a list of conditional probabilities. During testing, given certain features, the model will use the conditional probabilities to perform predictions.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

A Naive Bayes algorithm is one that assumes that all probabilities are independent of each other. Although it is not a valid assumption in the real world, it still performs quite well.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### The Analogizers

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Master Algorithm: **Support Vector Machines**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Loss Function: **Margin between Support Vectors**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Optimization Function: **Constrained Optimization**

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This tribe uses similarities among various data points to categorize them to distinct classes. Based on the similarity between data points, we can relate them together.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Models in this tribe are K-Nearest-Neighbor and Support Vector Machines.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Summary

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:image {"id":325,"align":"center","width":487,"height":487} -->

>

<figure class="aligncenter is-resized">
![placeholder]({attach}media/2019/02/puzzle_thumb.png){.wp-image-325 width="487" height="487"}




<!-- /wp:image -->

<!-- wp:paragraph -->

The book tries to amalgamate ideas together to form the Master Equation.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

We could use posterior probability as the evaluation function, and genetic search coupled with gradient descent as the optimizer

<!-- /wp:paragraph -->
