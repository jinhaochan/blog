Title: Non-Kaggle
Date: 2018-10-31 21:43
Author: jinhaochan
Slug: non-kaggle
Status: published



Here, you'll find Data science projects that work on data sets not from Kaggle.



<!-- wp:heading {"level":3} -->

### Detecting Botnet traffic





------------------------------------------------------------------------






Dataset: <https://mcfp.weebly.com/the-ctu-13-dataset-a-labeled-dataset-with-botnet-normal-and-background-traffic.html>





Notebook: [https://github.com/jinhaochan/BotnetDetection/blob/master/NetFlow-Botnet.ipynb](https://github.com/Charmanderander/BotnetDetection/blob/master/NetFlow-Botnet.ipynb)





In this data set, we were given traffic of both Botnet and normal traffic. I built a classifier to determine if a given traffic is anomalous or not.





I used the NetFlow data, and their features to build my model. I removed all source and destination information, as I wanted my classifier to learn solely on network behavioral data. And also, in reality, all the source and destination information will be different, so there is no use for my model to learn them.





In this problem, the data set was hugely unbalanced. I had significantly smaller set of Botnet traffic. To deal with this, I upsampled the amount of Botnet traffic.





Also, I had to find a balance between precision and recall. In detecting Botnet traffic, having a low precision and high recall is more desirable, as the cost of precision is cheap. It is more important for me to catch every single traffic that is a Botnet.


