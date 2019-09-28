Title: Random Forests
Date: 2019-06-09 20:43
Author: jinhaochan
Category: Data Science
Tags: Decision Tree, Random Forest
Slug: random-forests
Status: published



A random forest is an ensemble approach of combining multiple decision trees. Ensembling and Decision Trees, we first need to explain what these two things are



<!-- wp:heading {"level":3} -->

### Decision Trees





------------------------------------------------------------------------






Decision Trees try to encode and separate the data into if-else rules. It breaks the data down into smaller and smaller subsets. Each node poses the question, and each branch represents the decision.



<!-- wp:image {"id":331,"align":"center"} -->




![placeholder]({attach}media/2019/03/1_jaey3kp7tu2q6hn6lasmrw.png){.wp-image-331}








Given the example above, how do we know which question to ask first at the root node? Do we first split by Age, Pizza consumption, or Exercise? This decision is made by calculating the **Entropy Loss**, or **Information Gain**. Information gain is calculated using Entropy loss, so the two variables are closely linked.





Intuitively, we want to reduce entropy of the data, so that we can separate them nicely. A 0 entropy data means that all the samples are the same, and an entropy of 1 means that the samples are split evenly between the classes.



<!-- wp:image {"id":332,"align":"center"} -->




![placeholder]({attach}media/2019/03/0_klhgarh43lgdoksn.png){.wp-image-332}  
<figcaption>
When there are 0 samples of class P, Entropy is 0.  
When 0.5 of the samples are class P, Entropy is 1.  
When all the samples are class P, Entropy is 0.
</figcaption>








We want to make splits that **Maximizes Information Gain** (or making the resulting data sets more homogeneous). The following steps are involved:



<!-- wp:list {"ordered":true} -->

1.  For each target feature (Age, Pizza consumption, Exercise), calculate the current Entropy value.
2.  Split the data on each target feature, and calculate the resulting entropy after splitting.
3.  Choose the feature that results in the largest information gain, or entropy loss.
4.  Repeat.





That was a gist of a decision tree, now lets look at ensembling and Random Forest



<!-- wp:heading {"level":3} -->

### Ensembling and Random Forest





------------------------------------------------------------------------






Ensembling revolves around the idea of putting together several weak learners to form a strong learner. In Random Forest, the weak learners are Decision Trees



<!-- wp:image {"id":333,"align":"center"} -->




![placeholder]({attach}media/2019/03/skitch.jpg){.wp-image-333}  
<figcaption>
Blue dots represent the data points.  
Grey lines represent the weak learners.  
The red line represents the single strong learner.
</figcaption>








Here's the process of a Random Forest:



<!-- wp:list {"ordered":true} -->

1.  From the full data set, create several subsets by random sampling with replacement.
2.  Using these subsets, we create Decision Trees from them.





Now that we created the Random Forest, when we get a new input to predict, we pass the input to all the Decision Trees in the Random Forest. This gives up multiple outputs, one output for each tree. The final result of the Random Forest would then be an average of the trees (if it's a regression problem), or voting by majority (if it's a classification problem).





Downside of Random Forest are:





-   Random Forest that are used for regression cannot predict beyond the range in the training data they are fed with
-   Random Forests may overfit noisy data sets



<!-- wp:heading {"level":3} -->

### Conclusion





------------------------------------------------------------------------






This post was a fairly simple and straightforwad one, cover basic, but essential topics.





We have seen how a Decision Tree works, and the how the Random Forest makes use of multiple Decision Trees.


