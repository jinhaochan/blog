Title: LSTM
Date: 2019-06-30 15:33
Author: jinhaochan
Category: Data Science
Tags: Exploding Gradients, LSTM, Vanishing Gradients
Slug: lstm
Status: published

<!-- wp:paragraph -->

In the previous post, we talked about RNN, and how performing Backpropagation through time (BPTT) on an unrolled RNN with many time steps can lead to the problems of vanishing / exploding gradients, and difficulties in learning long term dependencies.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In this post, we're going to look at a the LSTM (Long Short Term Memory) model that is a variant of an RNN, but is designed specifically to combat the 2 issues.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### LSTM Structure

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Lets visually inspect the difference between a normal RNN cell and an LSTM cell.

<!-- /wp:paragraph -->

<!-- wp:image {"id":362} -->

![placeholder]({attach}media/2019/03/lstm3-simplernn.png){.wp-image-362}  

<!-- /wp:image -->

<!-- wp:image {"id":356} -->

![placeholder]({attach}media/2019/03/lstm3-chain.png) 

An unrolled LSTM cell


<!-- wp:paragraph -->

The A on each of the cells represent the Activation in the cell. In the RNN, this can either be a Sigmoid, tanh, ReLU, or other activation functions. In the LSTM however, its a combination of 3 Sigmoids and a tanh function.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The biggest difference, aside from the more complex internal structure of the LSTM, is that it has two connecting data pipelines from cell to cell.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Cell State

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

<!-- wp:paragraph -->

The top line of an LSTM cell represents the cell state

<!-- /wp:paragraph -->

<!-- wp:image {"id":357,"align":"center"} -->



![placeholder]({attach}media/2019/03/lstm3-c-line.png){.wp-image-357}


<!-- /wp:image -->

<!-- wp:paragraph -->

The LSTM has the ability to modify the cell state by removing information (through the multiplicative forget gate), or adding information (through the additive input gate)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This data flow from cell to cell is modified by two operators: The multiplication operator, and the addition operator denoted by the two pink nodes

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### LSTM Gates

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

The LSTM has 3 gates in the cell:

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Forget Gate
2.  Input gate
3.  Output Gate

<!-- /wp:list -->

<!-- wp:paragraph -->

These gates modify the data that is flowing in and out of the LSTM cell

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### The Common Sigmoid Layer

<!-- /wp:heading -->

<!-- wp:paragraph -->

In all the 3 gates, there exists the common Sigmoid layer. This layer outputs a value from 0 to 1 for each state in the cell state.

<!-- /wp:paragraph -->

<!-- wp:image {"id":365,"align":"center","width":87,"height":106} -->

>

<figure class="aligncenter is-resized">
![placeholder]({attach}media/2019/03/lstm3-gate.png){.wp-image-365 width="87" height="106"}  
<figcaption>
The common Sigmoid layer in all 3 gates
</figcaption>




<!-- /wp:image -->

<!-- wp:paragraph -->

The Sigmoid layer outputs a value from 0 to 1. This value corresponds to a value in the cell state, and this would mean different things for different gates.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In the Forget gate, 0 would mean forget the value in the cell state, and 1 would mean remember the value entirely.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In the Input gate, 0 would mean do not update this value at all, and 1 would mean update the value entirely.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In the Output gate, 0 would mean do not output this cell state value, and 1 would mean output this value entirely.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Forget Gate

<!-- /wp:heading -->

<!-- wp:paragraph -->

The first gate is the forget gate. This gate decides what information to discard from the cell state.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This gate has the Sigmoid activation function. It takes in the previous time step's output, and the current time step input.

<!-- /wp:paragraph -->

<!-- wp:image {"id":359} -->

<figure class="wp-block-image">
![placeholder]({attach}media/2019/03/lstm3-focus-f.png){.wp-image-359}


<!-- /wp:image -->

<!-- wp:paragraph -->

The two inputs are concatenated, and passed through the Sigmoid layer.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Recall that a Sigmoid activation function outputs a value from 0 to 1. A value of 0 means completely forget this input value, while 1 means to remember the value entirely.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Input Gate

<!-- /wp:heading -->

<!-- wp:paragraph -->

The next gate is the input gate, which is a combination of both the Sigmoid and tanh activation function. This gate decides what new information to add to the cell state.

<!-- /wp:paragraph -->

<!-- wp:image {"id":360} -->

<figure class="wp-block-image">
![placeholder]({attach}media/2019/03/lstm3-focus-i.png){.wp-image-360}


<!-- /wp:image -->

<!-- wp:paragraph -->

There are two steps in the input gate phase

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In the first step, the output of the previous time step and the input of the current time step are concatenated together, and passed into a Sigmoid. This layer decides which cell state values to update. (0 means do not update, 1 means update entirely)

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The inputs are also passed into a tanh activation function, which tells the model what to update the cells states with.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The multiplicative combination of these two outputs tells us which cell state to update (from the sigmoid layer), and what to update it with (tanh layer)

<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->

#### Output Gate

<!-- /wp:heading -->

<!-- wp:paragraph -->

The last gate, output gate, decides what value the cell would output. The output is derived from multiplying the outputs from the Sigmoid layer and tanh layer

<!-- /wp:paragraph -->

<!-- wp:image {"id":361} -->

<figure class="wp-block-image">
![placeholder]({attach}media/2019/03/lstm3-focus-o.png){.wp-image-361}


<!-- /wp:image -->

<!-- wp:paragraph -->

The Sigmoid layer takes in the previous and current time step values, and outputs values 0 to 1 for each value in the cell. A value of 0 means do not output this cell state value at all, and 1 means to output the entire value.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The tanh layer takes in the current cell state, which scales the values to be from -1 to 1. This value is then multiplied by the output of the Sigmoid layer to get the final output value.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Modification of the Cell State

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

The cell states in each LSTM cell are modified either by the forget gate, or the input gate.

<!-- /wp:paragraph -->

<!-- wp:image {"id":364} -->

<figure class="wp-block-image">
![placeholder]({attach}media/2019/03/lstm3-focus-c-2.png){.wp-image-364}


<!-- /wp:image -->

<!-- wp:paragraph -->

The forget gate outputs values 0-1, and is multiplied by the cell state. Cell states multiplied by 0 will be completely forgotten, while those multiplied by value &gt; 0 will be remembered by varying degrees.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The input gate then updates each value in the cell state by a candidate amount (from the tanh layer), scaled by a factor (decided from the Sigmoid layer)

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Conclusion

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

In each LSTM cell, there contains a cell state.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Forget gate decides what to drop from the cell state

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Input gate creates candidate values to update the cell state

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Output gate decides what values to output from the cell state

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Final Notes

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

I usually end with the conclusion, but all the information above was all the technical aspects of an LSTM. Here are some further questions relating to LSTM.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Q: What are you actually training when you do your Backpropagation through time on an LSTM?

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

A: Recall that the gates have to control what to forget, input and output from each LSTM cell. What exactly to forget, input and output are the variables being trained.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Q: So... how does it combat vanishing/exploding gradients?

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Gradients explode when their values are greater than 1, and vanish when their values are lesser than 1, and are backpropagated for too large a time step.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The key to LSTM preventing the vanexplgrad (I just made that up) is cell state updating step. Below shows the formula for updating the cell

<!-- /wp:paragraph -->

<!-- wp:image {"id":369,"align":"center"} -->

>


![placeholder]({attach}media/2019/03/untitled-1.png){.wp-image-369}  
<figcaption>
Calculating the current cell state using values from the previous cell state
</figcaption>




<!-- /wp:image -->

<!-- wp:list -->

-   `c(t)` is the current cell state to compute
-   `i` is the input gate that decides which cell state to update, `g` is the actual value changes to be made to the cell state. These two are multiplied together to get final cell state changes.
-   `f` is the forget gate, and `c(t-1)` is the previous cell state. These two are multiplied to drop values from the previous cell state.

<!-- /wp:list -->

<!-- wp:paragraph -->

When performing backpropagation, we find the derivative w.r.t the error. This gives us the formula

<!-- /wp:paragraph -->

<!-- wp:image {"id":368,"align":"center"} -->

>


![placeholder]({attach}media/2019/03/2.png){.wp-image-368}  
<figcaption>
Derivative of w.r.t the error
</figcaption>




<!-- /wp:image -->

<!-- wp:paragraph -->

This formula does not have any multiplicative element in it, and so when BPTT occurs, a *linear carousel* occurs, thus preventing vanexplgrad.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

<!-- /wp:paragraph -->
