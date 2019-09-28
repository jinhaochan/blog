Title: Convolutional Neural Networks
Date: 2019-02-17 16:11
Author: jinhaochan
Category: Data Science
Slug: convolutional-neural-networks
Status: published



Convolutional Neural Networks (CNN) are neural networks that are mainly used for image recognition and image classification.





In this post, we'll break down how a CNN works under the hoods.



<!-- wp:heading {"level":3} -->

### Backgroud





------------------------------------------------------------------------



</p>


If we used a traditional neural network without any of the prior convolution steps, the network would not scale well at all.





28 x 28 pixel of MNIST in a fully connected model gives use 784 input weights. Obviously, most pictures are a lot larger than 28 x 28. A 200 x 200 pixel picture would result in 120,000 input weights.





To minimize the number of input parameters, we need produce lower representations of the image that captures the most amount of information.





CNN was inspired the visual cortex, where in the human brain, parts of the visual cortex fired when detecting edges. Furthermore, studies have shown that the visual cortex works in layers; a given layer works on the features detected in the previous layer, from lines, to contours, to shapes, to entire objects.



<!-- wp:heading {"level":3} -->

### Vector Representation of Images  





------------------------------------------------------------------------



</p>


As we know, all models only take in numerical inputs to perform their actions. Non-numerical data such as text, and in this case images, must first be converted to numerical vectors.



<!-- wp:media-text {"mediaId":190,"mediaType":"image"} -->

<div class="wp-block-media-text alignwide">

<figure class="wp-block-media-text__media">
![placeholder]({attach}media/2018/12/1_zy1qfb9affzz66yxxoi2aw1.gif){.wp-image-190}

<div class="wp-block-media-text__content">


</p>
An image with multiple colors can be converted into a grayscale image, and each pixel is represented by its intensity from a range of 0-255.





This gives us a resulting numerical vector representation of an image

<p>






<!-- /wp:media-text -->

<!-- wp:heading {"level":3} -->

### Convolution?





------------------------------------------------------------------------



</p>


Before we talk about convolutional neural networks, we need to understand what is the meaning of convolution first.





In mathematical terms, a convolution is the combination of two functions to produce a third function, which has the properties of the two combined functions.





The term *convolution* refers to the resulting third function, as well as the process of computing the combination of two functions.



<!-- wp:media-text {"mediaId":192,"mediaType":"image"} -->

<div class="wp-block-media-text alignwide">

<figure class="wp-block-media-text__media">
![placeholder]({attach}media/2018/12/convolution_of_box_signal_with_itself2.gif){.wp-image-192}

<div class="wp-block-media-text__content">


</p>
By sliding function *g(t*) onto *f(t)*, we produce a third function *(f\*g)(t)*. We say that *(f\*g)(t)* is the convolution of *f(t)* and *g(t)*

<p>






<!-- /wp:media-text -->



Now we have a rough idea of what convolution is, we can go back to see how convolution works in the context of image processing.



<!-- wp:heading {"level":3} -->

### Convolution of Images





------------------------------------------------------------------------



</p>


To begin, we have converted the image to a *n x n* matrix of numbers from 0-255 which indicates the intensity.





Next, we take a smaller matrix of size *m x m*, where *m &lt; n*, and slide it over the original matrix. This smaller matrix is called a filter.



<!-- wp:media-text {"mediaId":196,"mediaType":"image","mediaWidth":23} -->

<div class="wp-block-media-text alignwide" style="grid-template-columns:23% auto;">

<figure class="wp-block-media-text__media">
![placeholder]({attach}media/2018/12/screen-shot-2016-07-24-at-11-25-13-pm2.png){.wp-image-196}

<div class="wp-block-media-text__content">


</p>
Image that has been converted to a matrix of numbers. For simplicity, we'll just use 0 and 1.

<p>






<!-- /wp:media-text -->

<!-- wp:media-text {"mediaId":197,"mediaType":"image","mediaWidth":15} -->

<div class="wp-block-media-text alignwide" style="grid-template-columns:15% auto;">

<figure class="wp-block-media-text__media">
![placeholder]({attach}media/2018/12/screen-shot-2016-07-24-at-11-25-24-pm1.png){.wp-image-197}

<div class="wp-block-media-text__content">


</p>
A smaller matrix, called a filter, that we'll use to slide over the original matrix

<p>






<!-- /wp:media-text -->

<!-- wp:media-text {"mediaId":198,"mediaType":"image"} -->

<div class="wp-block-media-text alignwide">

<figure class="wp-block-media-text__media">
![placeholder]({attach}media/2018/12/convolution_schematic.gif){.wp-image-198}

<div class="wp-block-media-text__content">


</p>
As we slide the filter over the matrix, we do a matrix multiplication, and take the result of the multiplication for our convolution matrix.

<p>






<!-- /wp:media-text -->



The convolution here can be seen as combining the original matrix and the filter to produce a third matrix, which is our convolved feature matrix.





The intuition behind this is that we are using the filter to extract features from the image. Different filter values will extract out different features from the image.



<!-- wp:paragraph {"align":"center"} -->

![placeholder]({attach}media/2018/12/screen-shot-2016-08-05-at-11-03-00-pm.png){.wp-image-200}





We can also use multiple filters to produce multiple Convoluted feature maps, which is called "Depth"



<!-- wp:image {"id":204,"align":"center","width":374,"height":188} -->

>

<figure class="aligncenter is-resized">
![placeholder]({attach}media/2018/12/screen-shot-2016-08-10-at-3-42-35-am.png){.wp-image-204 width="374" height="188"}








When building a CNN, the model learns the values of the filters on its own, while we have to specify other parameters like number of filters, filter size, stride and zero-padding.





For a given set of values, convolution (which is a set of filters) generates a new set of values. The depth of the new set of output corresponds to the number of filters, as each filter generates its own set of values.



<!-- wp:heading {"level":3} -->

### Removing Negative values from Convolved Features





------------------------------------------------------------------------



</p>


After we produce a Convolved feature map from the original image, we perform another operation called ReLU (Rectified Linear Unit) on each element.





What ReLU does is that it replaces all negative values to 0.





Why we need to apply ReLU on a convolved feature map is because the Convolution step is a linear operation. To account for non-linearity, we need to introduce a nonlinear function such as ReLU.





The resulting feature map after applying ReLU is called a Rectified feature map.



<!-- wp:image {"id":201} -->


![placeholder]({attach}media/2018/12/screen-shot-2016-08-07-at-6-18-19-pm.png){.wp-image-201}  

<figcaption>
Convoluted feature map becomes a Rectified feature map, after ReLU is applied to each pixel.  
This process changes all negative values to a 0 value

</figcaption>



<!-- wp:heading {"level":3} -->

### Dimensionality Reduction through Pooling





After we have extracted the Convoluted feature map, and passed it through our ReLU function to produce a Rectified feature map, we can reduce the feature map through a process called pooling.





There are 3 types of pooling: Max pooling, Sum pooling and Average pooling. We'll talk about Max pooling, because it works better in practice, and once you understand Max pooling, Sum pooling and Average pooling works the same way.





In doing Max pooling, we define yet another window size *k x k*, but in this case, we do not slide the window across the Rectified feature map. Instead, we divide the feature map up into the window size, and take the max value from it.



<!-- wp:image {"id":203} -->


![placeholder]({attach}media/2018/12/screen-shot-2016-08-10-at-3-38-39-am.png){.wp-image-203}  

<figcaption>
A Max pooling window size of 2x2.  
After we pass the Convolved feature map through ReLU, we get a Rectified feature map.  
We take the maximum value of the window size to get the reduced matrix.  

</figcaption>



<!-- wp:heading {"level":3} -->

### The Fully Connected Layer





------------------------------------------------------------------------



</p>


After we have broken down the image through iterative process of Convolution, ReLU and pooling, we get a set of matrices to represent the important features of the original image.





We then line up each of the values of the pooled matrix into a single vector, and feed it into a fully connected neural network.





When the neural network does it's learning via gradient descent or some other optimization algorithm, only the weights in the neural network and the values in the filter layer changes. The size of the filter and step size do not change.



<!-- wp:heading {"level":3} -->

### Features at each Layer





------------------------------------------------------------------------



</p>


We now have the 3 basic steps of a CNN: Convolution, ReLU and Pooling.





We can repeat this step numerous times to reduce the image, and extract out important features.



<!-- wp:image {"id":205,"align":"center","width":606,"height":144} -->

>

<figure class="aligncenter is-resized">
![placeholder]({attach}media/2018/12/screen-shot-2016-08-08-at-2-26-09-am.png){.wp-image-205 width="606" height="144"}  
<figcaption>
Repeated Convolution + ReLU and Pooling to reduce the image and extract important features.
</figcaption>








The more layers we have, the more complicated features we can extract out from the image. At each layer, we reconstruct simple layers to form more complex layers.



<!-- wp:media-text {"mediaId":206,"mediaType":"image"} -->

<div class="wp-block-media-text alignwide">

<figure class="wp-block-media-text__media">
![placeholder]({attach}media/2018/12/screen-shot-2016-08-10-at-12-58-30-pm.png){.wp-image-206}

<div class="wp-block-media-text__content">

<!-- wp:paragraph {"align":"left"} -->
</p>
In the first layer, we pick out simple features like edges and lines.





  
In the second layer, we're able to form parts of the face such as eyes and ears.





  
In the last layer, we can form the full face from all the layers

<p>






<!-- /wp:media-text -->



In another example, we can visually see how the CNN breaks down an image using Convolution + ReLU and pooling to extract important features, and make a classification at the end.



<!-- wp:image {"id":207,"align":"center","width":748,"height":423} -->

>

<figure class="aligncenter is-resized">
![placeholder]({attach}media/2018/12/conv_all.png){.wp-image-207 width="748" height="423"}








The intuition here is that we are making predictions here based on several features maps. If we have feature maps telling us there is two eyes, a nose and a mouth, we can make a prediction that it is a face.



<!-- wp:heading {"level":3} -->

### Conclusion 





------------------------------------------------------------------------



</p>


We've seen in this post how to do the following steps in a CNN



<!-- wp:list {"ordered":true} -->

1.  Transform an image to a numerical vector
2.  Apply a filter to extract a Convoluted feature map
3.  Apply ReLU to transform negative values to 0
4.  Apply Pooling to get your Rectified feature map
5.  Repeat until extract important features
6.  Pass them into a fully connected layer to perform prediction
7.  Learning only changes the weights of the connected layer and the filter matrix values


