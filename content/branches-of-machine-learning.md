Title: Branches of Machine Learning
Date: 2019-06-02 15:30
Author: jinhaochan
Category: Review
Slug: branches-of-machine-learning
Status: published



Just finished reading the book "The Master Algorithm", where the author tries to find the ultimate Machine Learning algorithm that can solve different varieties of problems (text, image, predictive, time series etc)





In the book, he goes over the 5 main branches (or tribes) of Machine Learning. They are:



<!-- wp:list {"ordered":true} -->

1.  The Evoluntionaries
2.  The Connectionist
3.  The Symbolist
4.  The Bayesians
5.  The Analogizers



<!-- wp:image {"id":323,"align":"center"} -->




![placeholder]({attach}media/2019/02/master-algo_thumb.png){.wp-image-323}








Lets look at what the 5 tribes have to offer, and their each individual "Master Algorithm"



<!-- wp:heading {"level":3} -->

### The Evolutionaries





------------------------------------------------------------------------



</p>


Master Algorithm: **Genetic Algorithm**





Loss Function: **Fitness Function**





Optimization Function: **Genetic Search**





This tribe tries to represent learning by mimicking evolution, where the it uses survival-of-the-fittest idea to pick the best model.





Starting with weak and not-fit models, the models go through different biologically inspired evolutionary stages: Mutation, Cross Over and Selection





Evolutionaries focus on learning the structure of the model, and not so much of the parameters (something which Connectionist with neural networks focus on)



<!-- wp:heading {"level":3} -->

### The Connectionists





------------------------------------------------------------------------



</p>


Master Algorithm: **Neural Networks**





Loss Function: **RMSE**





Optimization Function: **Gradient Descent and Back Propagation**





The Connectionist represent learning by modelling it after the brain and the neuron connections inside them. Dendrites, Axons and the Cell made up the Neural Network.





In Neural Networks, we are trying to learn the weights of the connections between the cells, and not the structure of the neural network itself (Perhaps there could be a combination of GA and NN, where GA finds the structure, and NN finds the weights)





It follows the notion that a concept can be represented by firing various neurons, and concepts that are similar to each other will cause the same set of neurons firing.



<!-- wp:heading {"level":3} -->

### The Symbolist





------------------------------------------------------------------------



</p>


Master Algorithm: **Logic**





Loss Function: **Accuracy**





Optimization Function: **Inverse Deduction**





Symbolist believe that all intelligence can be reduced to symbols, or rules. They build rule base systems, which obviously have huge limitations, because we can't possibly convert all intelligence and edge cases to a hard coded rule. The moment the rule encounters just a slightest bit of noise, it fails to perform.





Also, real life scenarios and concepts are seldom defined in black and white rules, and are usually stochastic and in the grey area.





In some cases, they can perform quite well. A model that Symbolist use are decision trees, which are huge tree that have if-else rules at each branch.



<!-- wp:heading {"level":3} -->

### The Bayesians





------------------------------------------------------------------------



</p>


Master Algorithm: **Graphical Models**





Loss Function: **Posterior Probability**





Optimization Function: **Probabilistic Inference**





As opposed to frequentist, which gives no value to prior beliefs, Bayesians hold prior beliefs at the center of their model.





The Bayesian works on conditional probability, or Bayes Theorem, that tells the probability of event A happening given that B has occurs `P(A|B)`.





During the training phase, the model takes the training data to build a list of conditional probabilities. During testing, given certain features, the model will use the conditional probabilities to perform predictions.





A Naive Bayes algorithm is one that assumes that all probabilities are independent of each other. Although it is not a valid assumption in the real world, it still performs quite well.



<!-- wp:heading {"level":3} -->

### The Analogizers





------------------------------------------------------------------------



</p>


Master Algorithm: **Support Vector Machines**





Loss Function: **Margin between Support Vectors**





Optimization Function: **Constrained Optimization**





This tribe uses similarities among various data points to categorize them to distinct classes. Based on the similarity between data points, we can relate them together.





Models in this tribe are K-Nearest-Neighbor and Support Vector Machines.



<!-- wp:heading {"level":3} -->

### Summary





------------------------------------------------------------------------



</p>
<!-- wp:image {"id":325,"align":"center","width":487,"height":487} -->



<figure class="aligncenter is-resized">
![placeholder]({attach}media/2019/02/puzzle_thumb.png){.wp-image-325 width="487" height="487"}








The book tries to amalgamate ideas together to form the Master Equation.





We could use posterior probability as the evaluation function, and genetic search coupled with gradient descent as the optimizer


