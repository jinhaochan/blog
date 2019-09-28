Title: Visualizing Neural Networks
Date: 2019-05-19 09:31
Author: jinhaochan
Category: Data Science
Slug: visualizing-neural-networks
Status: published



Neural Networks have always been sort of a black box when it comes to it's implementation, and how it produces good results. I came across some material that shows visually, how the neural networks morph the problem space so that they are separable.



<!-- wp:heading {"level":3} -->

### Simple Data





------------------------------------------------------------------------






Here's a sample graph that is not linearly separable:



<!-- wp:image {"id":302,"align":"center","width":284,"height":277} -->




![placeholder]({attach}media/2019/02/simple2_data.png){.wp-image-302 width="284" height="277"}








When we try to use a linear model to discriminate the two data, we get a poorly separated model:



<!-- wp:image {"id":303,"align":"center","width":278,"height":271} -->




![placeholder]({attach}media/2019/02/simple2_linear.png){.wp-image-303 width="278" height="271"}








Neural Networks, with the interactions of their hidden layers and nodes, are able to learn more complex information about the graph to plot a non-linear separation:



<!-- wp:image {"id":304,"align":"center","width":270,"height":263} -->




![placeholder]({attach}media/2019/02/simple2_0.png){.wp-image-304 width="270" height="263"}








What a Neural Networks does is that it warps the space of the problem so that it becomes more separable. The hidden layers in the network transforms the problem space by representing it in a different way



<!-- wp:image {"id":305,"align":"center","width":281,"height":274} -->




![placeholder]({attach}media/2019/02/simple2_1.png){.wp-image-305 width="281" height="274"}








By warping the problem space with the hidden layers, we see that it's able to linearly separate the two distributions. That's pretty cool! So what the neural network is doing is finding the most optimal way to represent the problem that is discriminative.





So what happens if the data distribution is too complex, or your neural network model is too simple (too shallow) that it can't properly represent the data?



<!-- wp:heading {"level":3} -->

### Spiral Data





------------------------------------------------------------------------






Given a complex data set that resembles a spiral shape, and a neural network model that is too simple, we can see it struggling to find a representation that is separable. This means that there is not enough hidden layers and hidden nodes to transform the data. We need to go deeper!



<!-- wp:image {"id":308,"align":"center","width":364,"height":355} -->




![placeholder]({attach}media/2019/02/spiral.2.2-2-2-2-2-2-2.gif){.wp-image-308 width="364" height="355"}








Here's the same spiral graph, but with enough hidden layers and nodes to transform the spiral data to a separable space. We can see the model separating the data very clearly



<!-- wp:image {"id":307,"align":"center","width":344,"height":336} -->




![placeholder]({attach}media/2019/02/spiral.1-2.2-2-2-2-2-2-1.gif){.wp-image-307 width="344" height="336"}






<!-- wp:heading {"level":3} -->

### More Complex Data





------------------------------------------------------------------------






In the last example, we see a more complex example, and see how a neural network can separate the data.



<!-- wp:image {"id":309,"align":"center","width":376,"height":283} -->




![placeholder]({attach}media/2019/02/topology_base.png){.wp-image-309 width="376" height="283"}








Given a circular topology data, a shallow neural network will have difficulties trying to separate the data from the inside and outer ring. We see it trying to pull apart the data like how it did with the spiral data, but it fails to do so



<!-- wp:image {"id":310,"align":"center","width":351,"height":343} -->




![placeholder]({attach}media/2019/02/topology_2d-2d_train.gif){.wp-image-310 width="351" height="343"}








By introducing more hidden layers and nodes and going deeper, we see that the data is able to be extracted out into another dimension, making it separable!  



<!-- wp:image {"id":311} -->


![placeholder]({attach}media/2019/02/topology_3d.png){.wp-image-311}




<!-- wp:heading {"level":3} -->

### Conclusion





------------------------------------------------------------------------






In this post, I wanted to show how neural networks warp the space of the data make them separable, and how a shallow network might fail to perform well.





By adding more hidden layers and nodes, we are able to morph and warp the space into different dimensions, representing them differently and making them discriminative


