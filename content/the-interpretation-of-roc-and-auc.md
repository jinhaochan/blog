Title: The Interpretation of ROC and AUC
Date: 2019-04-14 12:52
Author: jinhaochan
Category: Data Science
Slug: the-interpretation-of-roc-and-auc
Status: published



The ROC curve and it's AUC is a common metric for evaluation the performance of a model. In this post, we dig deeper to find out how to interpret the results, and what corrective actions to take to improve it.



<!-- wp:heading {"level":3} -->

### What is it?





------------------------------------------------------------------------



</p>


The ROC curve, or Receiver Operating Characteristic curve works on binary classification problems (True or False). It plots the following values against each other:





-   True Positive Rate (TPR): Of those sample that are true, how many did I predict are true? This is also known as Recall (`TP/P`, where `TP` is how many True samples predicted True, and `P` is the total number of True samples)
-   False Positive Rate (FPR): Of those samples that are false, how many did I predict are true? This is also known as False Alarms (`FP/N`, where `FP` is how many False samples predicted True, and `N` is the total number of False samples)



<!-- wp:heading {"level":3} -->

### So... What is it?





------------------------------------------------------------------------



</p>


Now that we got the formal definitions out of the way, lets talk about the intuition behind the ROC and AUC.





The TPR is also called **sensitivity**, which means how many in the **true positives** have I identified to be **True**.





TNR (True Negative Rate) is also called **specificity**, which means how many in the **true negatives** have I identified to be **False**.





FPR is (`1 - TNR`), which means how many in the **true negatives** have I identified to be **True**.





The ROC curve plots TPR against FPR.



<!-- wp:image {"id":257,"align":"center"} -->




![placeholder]({attach}media/2019/01/roc-curves.png){.wp-image-257}  
<figcaption>
Plotting the TPR against the FPR. There are 4 scenarios here
</figcaption>








The top left graph shows the perfect scenario, where the Area Under Curve (AUC) is 1. This means that the model has 100% TPR, regardless of my FPR rate, and correctly classifies all True samples as True.





The bottom right graph shows a random classifier, which is randomly separated.





The question to ask is: what is the lowest possible FPR, that can give me the highest FPR?





If we look at the perfect scenario, the highest possible TPR corresponds to an almost 0 FPR. That's perfect! It means the model made no classification errors (Excellent Precision and Recall)





Looking at the random separation, the highest TPR corresponds to the highest FPR, which is horrible. It means that for my model to get a good Recall, I must predict all my False samples to be True as well.



<!-- wp:heading {"level":3} -->

### Conclusion





------------------------------------------------------------------------



</p>


A good model will thus have a lower FPR that will give a reasonable TPR (Reasonable here depends on the scenario and use case).





Another way to look at it is, to get a good Recall, what is the amount of Precision I have to sacrifice.





If the model has to sacrifice a lot of Precision to get a good Recall, then it is a bad model. If the model does not have to sacrifice any Precision (In the case of the perfect scenario), then it is a good model.  


