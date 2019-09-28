Title: Activation Functions
Date: 2019-04-14 18:07
Author: jinhaochan
Category: Data Science
Tags: Activation Functions
Slug: activation-functions
Status: published

<!-- wp:paragraph -->

The structure of a deep learning model consists mainly of nodes, and connections between them. Most of the time, every single node is connected to every other node in the next layer, which we call a Dense layer.

<!-- /wp:paragraph -->

<!-- wp:image {"id":260,"align":"center"} -->

>


![placeholder]({attach}media/2019/01/2.png){.wp-image-260}  
<figcaption>
Nodes in a fully connected neural network
</figcaption>




<!-- /wp:image -->

<!-- wp:paragraph -->

Within each node is a mathematical equation, decides, based on the input values and their weights, what values to output to the next layer. These mathematical equations are called Activation Functions.

<!-- /wp:paragraph -->

<!-- wp:image {"id":261,"align":"center"} -->

>


![placeholder]({attach}media/2019/01/3.png){.wp-image-261}  
<figcaption>
The activation function is in the middle box, which performs an operation on the inputs, z, based on their weights and bias value.
</figcaption>




<!-- /wp:image -->

<!-- wp:heading {"level":3} -->

### Different Activation Functions

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

There are several kinds of Activation Functions, or in other words, different kinds of mathematical operations that a node can take. They are:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Sigmoid Function
2.  Tanh Function
3.  ReLU Function
4.  Leaky ReLU Function

<!-- /wp:list -->

<!-- wp:image {"id":262,"align":"center"} -->

>


![placeholder]({attach}media/2019/01/4.png){.wp-image-262}  
<figcaption>
Different Activation Functions and their mathematical equations
</figcaption>




<!-- /wp:image -->

<!-- wp:paragraph -->

These activation functions take in the inputs `z` from the previous layer, and feed it into their equations to produce an output `a`.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Sigmoid vs TanH

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

The TanH function is almost strictly superior to the Sigmoid function, because the TanH function has it's mean centered at `0`. This feature will result in a higher value of derivative, and a faster learning rate. Also, having a `0` value mean will avoid having bias in the gradients.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### ReLU vs (Sigmoid + TanH)

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

The drawback of both Sigmoid and TanH, given that they have a curved graph, is that if the value of `z` is either extremely large or small, the gradient on the curve will be extremely small as well. This small gradient will have an adverse effect on the learning rate when performing Gradient Descent.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The solution to this is ReLU (Rectified Linear Unit), which has a constant gradient regardless of the value of `z`. But for ReLU, having a negative value of `z` will result in a `0` value activation. The solution for that is a Leaky ReLU, which allows for a small value of `a` for negative values of `z`.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Must they Always be Non-Linear?

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Yes, Activation Function must always be non-linear. Having multiple linear activation functions can be condensed together, effectively negating the need for any hidden layers or hidden nodes.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Conclusion

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

In this post, we talked very briefly about the different kinds of Activation Functions, and compared their pro and cons.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

A recommendation for building a neural network model is to have the hidden nodes all be either TanH or ReLU, and never having Sigmoid.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The only time you can have a Sigmoid is at your output layer, if your problem is a binary classification problem.

<!-- /wp:paragraph -->
