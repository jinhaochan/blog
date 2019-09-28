Title: GAN?
Date: 2019-05-26 13:13
Author: jinhaochan
Category: Data Science
Slug: gan
Status: published



A Generative Adversarial Network (GAN) is a collection of two neural network models: A Discriminator, and a Generator. The goals of the two models are opposing to each other



<!-- wp:list {"ordered":true} -->

1.  Discriminator: Given a set of features, we try to predict the label
2.  Generator: Given a label, we try to predict the features that lead to the label





For example, a Discriminator in a spam email detector identifies if an email is spam, given certain keywords. A Generator on the other hand, given a spam label, tries to come up with keywords that results in the label spam.





The goal of a GAN is to train a generative model that can produce outputs that are believable enough for the discriminator to classify it as a positive label. At the end, the generative model will be able to produce outputs that are close to what the true distribution produces. Examples of this are image generations, text generation and



<!-- wp:heading {"level":3} -->

### How It Works





------------------------------------------------------------------------



</p>


Generator:





-   The generator takes in a random numbers from a noise generator, and produces a random output
-   The outputs of the generator are mixed together with a collection from the actual training data set





Discriminator:





-   The Discriminator takes in data from both the actual data set and the output of the Generator
-   The Discriminator makes a prediction of each data and predicts the probability of the label
-   It tries to predict if the data is from the training set, or generated from the Generator model (Real vs Fake data)





The Discriminator and Generator goes back and forth, Generating new data points, and predicting the data points. This goes on until convergence: When the Generator produces data points that are classified as Real by the Discriminator.





The Discriminator gets the feedback for optimization from the ground truth, and the Generator gets feedback from the Discriminator.



<!-- wp:image {"id":314,"align":"center","width":503,"height":218} -->

>

<figure class="aligncenter is-resized">
![placeholder]({attach}media/2019/02/gans.png){.wp-image-314 width="503" height="218"}






<!-- wp:heading {"level":3} -->

### Visualizing the Generator





------------------------------------------------------------------------



</p>


We can visualize how the Generator learns to generate outputs that goes closer to the distribution of the real distribution



<!-- wp:image {"id":315} -->


![placeholder]({attach}media/2019/02/iterations-1.gif){.wp-image-315}






We can see that initially, the distribution by the Generator was random and scattered all over. Over several iterations, the Generator starts producing outputs that have a distribution getting closer to the actual distribution.



<!-- wp:heading {"level":3} -->

### Math for GAN





------------------------------------------------------------------------



</p>


We have a joint loss function, with the two models (Generative `G` and Discriminative `D`) optimizing for different things.





The Discriminator tries to identify if the data is from the true distribution `x`, and outputs a value `D(x)`. The Discriminator also tries to recognize if the data comes from the Generator `G`, which outputs a value `D(G(z))`. (or `1 - D(G(z))`, because the inverse of the Generated data is the data from the true distribution) Putting these two together, we get the loss function:



<!-- wp:image {"id":316,"align":"center"} -->

>


![placeholder]({attach}media/2019/02/1-4xahmaugxeoqnnjhzjq-4q.jpeg){.wp-image-316}








The Discriminator `D` wants to maximize this, as it wants to correctly identify true data `x` and `1 - D(G(z))`





On the other hand, the Generator `G` tries to generates data to fool the Discriminator, and it wants to minimize the second half of the loss function:



<!-- wp:image {"id":317,"align":"center"} -->

>


![placeholder]({attach}media/2019/02/1-n235xeigxkl3ktl08d-cza.jpeg){.wp-image-317}








By maximizing `D` and minimizing `G`, we get the function:



<!-- wp:image {"id":318} -->


![placeholder]({attach}media/2019/02/1-ihk3whuaz_0uek4sjicyfw.png){.wp-image-318}






We then use alternating gradient descent, one step to Maximize the function by Discriminator `D`, and the other step to Minimize the function by Generator `G`





We fix the Generator's parameters, and perform one iteration of Gradient Descent on the Discriminator. Then we switch and fix the Discriminator's parameters, and perform one iteration of Gradient Descent on the Generator. We keep alternating these steps of Gradient Descent of both models until convergence.





The Discriminator usually wins early on against the Generator, as initially, it is very easy for the Discriminator to identify Generated data because the Generator has not learnt anything yet. As such, the Generator will get diminished gradient, and learning will be very slow. GAN therefore modifies the loss function slightly to backpropagate the gradient to the Generator



<!-- wp:image {"id":319} -->


![placeholder]({attach}media/2019/02/1-6so6q3dwurg8qrmwk1y3jw.jpeg){.wp-image-319}






As the gradient backpropagated to the Generator approaches 0, the GAN changes the function to another one to ensure the gradient to the Generator does not vanish.



<!-- wp:heading {"level":3} -->

### Tips for training a GAN





------------------------------------------------------------------------



</p>


When training the Generator, hold the values of the Discriminator constant.





When training the Discriminator, hold the values of the Generator constant.





You may train one network that is stronger than the other, giving adverse results: If the Generator is too strong, it will always successfully deceive the Discriminator, leading to a lot of false negatives. If the Discriminator is too strong, it will give outputs that are close to 0 or 1, and the Generator will struggle during learning from gradient descent.  


