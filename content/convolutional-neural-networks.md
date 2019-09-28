Title: Convolutional Neural Networks
Date: 2019-02-17 16:11
Author: jinhaochan
Category: Data Science
Slug: convolutional-neural-networks
Status: published

<!-- wp:paragraph -->

Convolutional Neural Networks (CNN) are neural networks that are mainly used for image recognition and image classification.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In this post, we'll break down how a CNN works under the hoods.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Backgroud

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

If we used a traditional neural network without any of the prior convolution steps, the network would not scale well at all.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

28 x 28 pixel of MNIST in a fully connected model gives use 784 input weights. Obviously, most pictures are a lot larger than 28 x 28. A 200 x 200 pixel picture would result in 120,000 input weights.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

To minimize the number of input parameters, we need produce lower representations of the image that captures the most amount of information.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

CNN was inspired the visual cortex, where in the human brain, parts of the visual cortex fired when detecting edges. Furthermore, studies have shown that the visual cortex works in layers; a given layer works on the features detected in the previous layer, from lines, to contours, to shapes, to entire objects.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Vector Representation of Images  

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

As we know, all models only take in numerical inputs to perform their actions. Non-numerical data such as text, and in this case images, must first be converted to numerical vectors.

<!-- /wp:paragraph -->

<!-- wp:media-text {"mediaId":190,"mediaType":"image"} -->

<div class="wp-block-media-text alignwide">

<figure class="wp-block-media-text__media">
![](https://chanjinhao.files.wordpress.com/2018/12/1_zy1qfb9affzz66yxxoi2aw1.gif){.wp-image-190}
</figure>
<div class="wp-block-media-text__content">

<!-- wp:paragraph -->
</p>
An image with multiple colors can be converted into a grayscale image, and each pixel is represented by its intensity from a range of 0-255.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

This gives us a resulting numerical vector representation of an image

<p>
<!-- /wp:paragraph -->

</div>

</div>

<!-- /wp:media-text -->

<!-- wp:heading {"level":3} -->

### Convolution?

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

Before we talk about convolutional neural networks, we need to understand what is the meaning of convolution first.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In mathematical terms, a convolution is the combination of two functions to produce a third function, which has the properties of the two combined functions.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The term *convolution* refers to the resulting third function, as well as the process of computing the combination of two functions.

<!-- /wp:paragraph -->

<!-- wp:media-text {"mediaId":192,"mediaType":"image"} -->

<div class="wp-block-media-text alignwide">

<figure class="wp-block-media-text__media">
![](https://chanjinhao.files.wordpress.com/2018/12/convolution_of_box_signal_with_itself2.gif){.wp-image-192}
</figure>
<div class="wp-block-media-text__content">

<!-- wp:paragraph -->
</p>
By sliding function *g(t*) onto *f(t)*, we produce a third function *(f\*g)(t)*. We say that *(f\*g)(t)* is the convolution of *f(t)* and *g(t)*

<p>
<!-- /wp:paragraph -->

</div>

</div>

<!-- /wp:media-text -->

<!-- wp:paragraph -->

Now we have a rough idea of what convolution is, we can go back to see how convolution works in the context of image processing.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Convolution of Images

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

To begin, we have converted the image to a *n x n* matrix of numbers from 0-255 which indicates the intensity.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Next, we take a smaller matrix of size *m x m*, where *m &lt; n*, and slide it over the original matrix. This smaller matrix is called a filter.

<!-- /wp:paragraph -->

<!-- wp:media-text {"mediaId":196,"mediaType":"image","mediaWidth":23} -->

<div class="wp-block-media-text alignwide" style="grid-template-columns:23% auto;">

<figure class="wp-block-media-text__media">
![](https://chanjinhao.files.wordpress.com/2018/12/screen-shot-2016-07-24-at-11-25-13-pm2.png){.wp-image-196}
</figure>
<div class="wp-block-media-text__content">

<!-- wp:paragraph -->
</p>
Image that has been converted to a matrix of numbers. For simplicity, we'll just use 0 and 1.

<p>
<!-- /wp:paragraph -->

</div>

</div>

<!-- /wp:media-text -->

<!-- wp:media-text {"mediaId":197,"mediaType":"image","mediaWidth":15} -->

<div class="wp-block-media-text alignwide" style="grid-template-columns:15% auto;">

<figure class="wp-block-media-text__media">
![](https://chanjinhao.files.wordpress.com/2018/12/screen-shot-2016-07-24-at-11-25-24-pm1.png){.wp-image-197}
</figure>
<div class="wp-block-media-text__content">

<!-- wp:paragraph -->
</p>
A smaller matrix, called a filter, that we'll use to slide over the original matrix

<p>
<!-- /wp:paragraph -->

</div>

</div>

<!-- /wp:media-text -->

<!-- wp:media-text {"mediaId":198,"mediaType":"image"} -->

<div class="wp-block-media-text alignwide">

<figure class="wp-block-media-text__media">
![](https://chanjinhao.files.wordpress.com/2018/12/convolution_schematic.gif){.wp-image-198}
</figure>
<div class="wp-block-media-text__content">

<!-- wp:paragraph -->
</p>
As we slide the filter over the matrix, we do a matrix multiplication, and take the result of the multiplication for our convolution matrix.

<p>
<!-- /wp:paragraph -->

</div>

</div>

<!-- /wp:media-text -->

<!-- wp:paragraph -->

The convolution here can be seen as combining the original matrix and the filter to produce a third matrix, which is our convolved feature matrix.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The intuition behind this is that we are using the filter to extract features from the image. Different filter values will extract out different features from the image.

<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center"} -->

![](https://chanjinhao.files.wordpress.com/2018/12/screen-shot-2016-08-05-at-11-03-00-pm.png){.wp-image-200}

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

We can also use multiple filters to produce multiple Convoluted feature maps, which is called "Depth"

<!-- /wp:paragraph -->

<!-- wp:image {"id":204,"align":"center","width":374,"height":188} -->

<div class="wp-block-image">

<figure class="aligncenter is-resized">
![](https://chanjinhao.files.wordpress.com/2018/12/screen-shot-2016-08-10-at-3-42-35-am.png){.wp-image-204 width="374" height="188"}
</figure>

</div>

<!-- /wp:image -->

<!-- wp:paragraph -->

When building a CNN, the model learns the values of the filters on its own, while we have to specify other parameters like number of filters, filter size, stride and zero-padding.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

For a given set of values, convolution (which is a set of filters) generates a new set of values. The depth of the new set of output corresponds to the number of filters, as each filter generates its own set of values.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Removing Negative values from Convolved Features

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

After we produce a Convolved feature map from the original image, we perform another operation called ReLU (Rectified Linear Unit) on each element.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

What ReLU does is that it replaces all negative values to 0.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Why we need to apply ReLU on a convolved feature map is because the Convolution step is a linear operation. To account for non-linearity, we need to introduce a nonlinear function such as ReLU.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The resulting feature map after applying ReLU is called a Rectified feature map.

<!-- /wp:paragraph -->

<!-- wp:image {"id":201} -->

<figure class="wp-block-image">
![](https://chanjinhao.files.wordpress.com/2018/12/screen-shot-2016-08-07-at-6-18-19-pm.png){.wp-image-201}  

<figcaption>
Convoluted feature map becomes a Rectified feature map, after ReLU is applied to each pixel.  
This process changes all negative values to a 0 value

</figcaption>
</figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->

### Dimensionality Reduction through Pooling

<!-- /wp:heading -->

<!-- wp:paragraph -->

After we have extracted the Convoluted feature map, and passed it through our ReLU function to produce a Rectified feature map, we can reduce the feature map through a process called pooling.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

There are 3 types of pooling: Max pooling, Sum pooling and Average pooling. We'll talk about Max pooling, because it works better in practice, and once you understand Max pooling, Sum pooling and Average pooling works the same way.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

In doing Max pooling, we define yet another window size *k x k*, but in this case, we do not slide the window across the Rectified feature map. Instead, we divide the feature map up into the window size, and take the max value from it.

<!-- /wp:paragraph -->

<!-- wp:image {"id":203} -->

<figure class="wp-block-image">
![](https://chanjinhao.files.wordpress.com/2018/12/screen-shot-2016-08-10-at-3-38-39-am.png){.wp-image-203}  

<figcaption>
A Max pooling window size of 2x2.  
After we pass the Convolved feature map through ReLU, we get a Rectified feature map.  
We take the maximum value of the window size to get the reduced matrix.  

</figcaption>
</figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->

### The Fully Connected Layer

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

After we have broken down the image through iterative process of Convolution, ReLU and pooling, we get a set of matrices to represent the important features of the original image.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

We then line up each of the values of the pooled matrix into a single vector, and feed it into a fully connected neural network.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

When the neural network does it's learning via gradient descent or some other optimization algorithm, only the weights in the neural network and the values in the filter layer changes. The size of the filter and step size do not change.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Features at each Layer

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

We now have the 3 basic steps of a CNN: Convolution, ReLU and Pooling.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

We can repeat this step numerous times to reduce the image, and extract out important features.

<!-- /wp:paragraph -->

<!-- wp:image {"id":205,"align":"center","width":606,"height":144} -->

<div class="wp-block-image">

<figure class="aligncenter is-resized">
![](https://chanjinhao.files.wordpress.com/2018/12/screen-shot-2016-08-08-at-2-26-09-am.png){.wp-image-205 width="606" height="144"}  
<figcaption>
Repeated Convolution + ReLU and Pooling to reduce the image and extract important features.
</figcaption>
</figure>

</div>

<!-- /wp:image -->

<!-- wp:paragraph -->

The more layers we have, the more complicated features we can extract out from the image. At each layer, we reconstruct simple layers to form more complex layers.

<!-- /wp:paragraph -->

<!-- wp:media-text {"mediaId":206,"mediaType":"image"} -->

<div class="wp-block-media-text alignwide">

<figure class="wp-block-media-text__media">
![](https://chanjinhao.files.wordpress.com/2018/12/screen-shot-2016-08-10-at-12-58-30-pm.png){.wp-image-206}
</figure>
<div class="wp-block-media-text__content">

<!-- wp:paragraph {"align":"left"} -->
</p>
In the first layer, we pick out simple features like edges and lines.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

  
In the second layer, we're able to form parts of the face such as eyes and ears.

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

  
In the last layer, we can form the full face from all the layers

<p>
<!-- /wp:paragraph -->

</div>

</div>

<!-- /wp:media-text -->

<!-- wp:paragraph -->

In another example, we can visually see how the CNN breaks down an image using Convolution + ReLU and pooling to extract important features, and make a classification at the end.

<!-- /wp:paragraph -->

<!-- wp:image {"id":207,"align":"center","width":748,"height":423} -->

<div class="wp-block-image">

<figure class="aligncenter is-resized">
![](https://chanjinhao.files.wordpress.com/2018/12/conv_all.png){.wp-image-207 width="748" height="423"}
</figure>

</div>

<!-- /wp:image -->

<!-- wp:paragraph -->

The intuition here is that we are making predictions here based on several features maps. If we have feature maps telling us there is two eyes, a nose and a mouth, we can make a prediction that it is a face.

<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->

### Conclusion 

<!-- /wp:heading -->

<!-- wp:separator -->

------------------------------------------------------------------------

<!-- /wp:separator -->

</p>
<!-- wp:paragraph -->

We've seen in this post how to do the following steps in a CNN

<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

1.  Transform an image to a numerical vector
2.  Apply a filter to extract a Convoluted feature map
3.  Apply ReLU to transform negative values to 0
4.  Apply Pooling to get your Rectified feature map
5.  Repeat until extract important features
6.  Pass them into a fully connected layer to perform prediction
7.  Learning only changes the weights of the connected layer and the filter matrix values

<!-- /wp:list -->