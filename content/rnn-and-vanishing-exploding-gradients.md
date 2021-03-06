Title: RNN and Vanishing/Exploding Gradients
Date: 2019-06-23 16:23
Author: Chan Jin Hao
Category: Data Science
Tags: RNN, Vanishing Gradients
Slug: rnn-and-vanishing-exploding-gradients
Status: published



In this post, we're going to be looking at:



<!-- wp:list {"ordered":true} -->

1.  Recurrent Neural Networks (RNN)
2.  Weight updates in an RNN
3.  Unrolling an RNN
4.  Vanishing/Exploding Gradient Problem



<!-- wp:heading {"level":3} -->

### Recurrent Neural Networks





------------------------------------------------------------------------






A Recurrent Neural Network (RNN) is a variant of neural networks, where in each neuron, the outputs cycle back to themselves, hence being recurrent.



<!-- wp:image {"id":345} -->


![placeholder]({attach}media/2019/03/0_mrhhgabskajpbt21.png){.wp-image-345}  

<figcaption>
Each neuron's output cycle back to themselves, as compared to a feed-forward neural network

</figcaption>





This means that each neuron in an RNN has two sources of inputs:



<!-- wp:list {"ordered":true} -->

1.  The present data (Which can be one or more inputs)
2.  The recent past data (A single output based on the previous set of inputs)





Intuitively, this means that the network can learn whats happening now, and what happened before.





The RNN has a Short-Term memory, as the recurrent input is only derived from it's most recent past. Anything that happened way before is "forgotten".





For example, if we feed in the word "neuron" letter by letter, in a feed-forward NN, when we reach the letter "r", the model would have forgotten "n", "e", "u".





In an RNN, the model would remember the immediate past, that previously we have seen the letter "u".





Like a normal feed-forward NN, the RNN also has a weight matrix, but with one additional weight to include the recurrent input. When doing backpropagation, this recurrent weights is also subjected to tweaking.



<!-- wp:heading {"level":3} -->

### Weight Updates in an RNN





------------------------------------------------------------------------






This weight updating phase for an RNN is called Backpropagation Though Time. Lets examine first how a feed-forward NN does forward and backward propagation for weight correction





In a feed-forward NN, forward propagation is done to get the predicted output. An error estimate is gotten from the predicted output and the true label.





Using the error estimate, we do backpropgation to find the partial derivatives of the error with respect to the weights of the network.





These derivatives are then used by Gradient Descent to tweak the weights of the model, and ultimately try to minimize the error estimate, so that the predicted output is close to the true output.



<!-- wp:image {"id":346,"align":"center"} -->




![placeholder]({attach}media/2019/03/0_fbugysciqjnfi3n6.png){.wp-image-346}  
<figcaption>
Forward propagation to get the outputs, error estimate calculation, and backpropgation to get the gradients of the error w.r.t. the weights, and apply gradient descent.  
</figcaption>








In an RNN, there is an additional component of the recurrent input in each neuron. This input also has its corresponding weight that needs to be tweaked. To understand how that happens, we need to be able to visualize "unrolling" an RNN



<!-- wp:heading {"level":3} -->

### Unrolling an RNN





------------------------------------------------------------------------






As mentioned earlier, each neuron will 2 sources of inputs: The current input, and the most recent previous input.



<!-- wp:image {"id":348,"align":"center"} -->




![placeholder]({attach}media/2019/03/0_ynlojw7yvjarwmd4-copy.png){.wp-image-348}  
<figcaption>
The output of the RNN cell is fed back.
</figcaption>








In the next time step, it will take the current input plus the previous output. We can visualize this by "unrolling" the RNN, so we can see what happens at each time step.



<!-- wp:image {"id":349,"align":"center"} -->




![placeholder]({attach}media/2019/03/0_ynlojw7yvjarwmd4.png){.wp-image-349}  
<figcaption>
An unolled RNN to visualize what happens to the cell at each time step
</figcaption>








The image above shows what happens when you unroll one recurrent neuron. In a network with 100s of neurons, some layers recurrent, things can get really messy.



<!-- wp:image {"id":350,"align":"center"} -->




![placeholder]({attach}media/2019/03/dpln_0423.png){.wp-image-350}  
<figcaption>
Hidden layers 1 and 2 are recurrent. Here we unroll them for 3 time steps
</figcaption>






<!-- wp:heading {"level":3} -->

### Vanishing/Exploding Gradient Problem





------------------------------------------------------------------------






When we combine the two concepts of applying Backpropagation on an unrolled RNN, we get Backpropagation through time (BPTT).





Recall that we also need to learn the weights of the recurrent input, and BPTT is done to get the gradient by finding the partial derivatives of the error with respect to the recurrent inputs. (Just like how in a normal feed-forward NN, backpropagation is done to get the partial derivatives of the error with respect to the weights). Using the gradients, Gradient Descent is then applied.





In BPTT, the error is backpropagated from the last time step all the way to the first time step to update the weights of the recurrent input.





The problem comes when there are too many time steps, and BPTT has to propagate error back too many times, which will result in the gradients exploding, or vanishing.





At each time step, the gradients are multiplied by each other via matrix multiplication because of chain rule. If the gradient is greater than 1.0, a large number of time steps will cause the gradient to "explode", or become too large.





Likewise, when the gradient is less than 1.0, multiplying it too many times by itself will cause the gradient to "vanish", or become close to zero.





Both exploding and vanishing gradients are problematic, because then Gradient Descent will performing poorly on overly large values, or overly small values.



<!-- wp:heading {"level":3} -->

### Summary





------------------------------------------------------------------------






To recap on a feed-forward NN:



<!-- wp:list {"ordered":true} -->

1.  Forward propagation is done get the output prediction
2.  An error estimate is calculated from the model output to the the true values
3.  Backpropagation is done using the error, to get partial derivative of the error w.r.t. the weights
4.  Gradient Descent is applied using the gradients to minimize the error





And for an RNN:



<!-- wp:list {"ordered":true} -->

1.  Forward propagation is done get the output prediction
2.  An error estimate is calculated from the model output to the the true values
3.  The RNN is unrolled by the total number of time steps
4.  BPTT is done to get partial derivative of the error w.r.t. the weights
5.  Gradient Descent is applied using the gradients to minimize the error





The problem comes when there are too many times steps, and performing BPTT causes the gradients to explode or vanish. This affects the final step of applying Gradient Descent.






