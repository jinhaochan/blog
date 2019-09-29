Title: K-Means Clustering
Date: 2019-06-16 21:18
Author: Chan Jin Hao
Category: Data Science
Tags: K means clustering
Slug: k-means-clustering
Status: published



K-Means Clustering is an unsupervised learning algorithm. It works by grouping similar data points together to try to find underlying patterns.





The number of groups are pre-defined by the user as K.



<!-- wp:heading {"level":3} -->

### How the Algorithm works





------------------------------------------------------------------------






Before the iterative update starts, a random selection of centroid locations are picked on the graph. These centroids act as the beginning points for each cluster. (if K = 5, there will be 5 random centroids)



<!-- wp:list {"ordered":true} -->

1.  Data Assignment Step
    -   Each data point is assigned to its nearest centroid, based on the squared Euclidean distance
2.  Centroid Update
    -   Given the new data points, re-calculate the centroid value
3.  Repeat until centroid no longer changes, or until a stopping criteria.



<!-- wp:heading {"level":3} -->

### Choosing K





------------------------------------------------------------------------






How do we choose K? Well, iteratively of cause. We define K to be a range of values, and run K-mean clustering through those values.



<!-- wp:image {"id":341} -->


![placeholder]({attach}media/2019/03/introduction-to-k-means-clustering-elbow-point-example-1.jpg){.wp-image-341}




<!-- wp:heading {"level":3} -->

### Conlcusion





------------------------------------------------------------------------






This was a pretty short post, but it acts as a summary of how K-means clustering works!


