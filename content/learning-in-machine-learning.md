Title: Learning in Machine Learning
Date: 2019-01-27 17:14
Author: jinhaochan
Category: Data Science
Tags: Machine learning
Slug: learning-in-machine-learning
Status: published



When we talk about machine learning, it's mostly a black box, where everything is nicely wrapped in easy to call library functions.





Scipy, Numpy, Scikit-learn help us abstract all the nitty gritty details underlying machine learning





In this post, we're going to see where exactly the learning takes place, and what happens when you "train" a model.  



<!-- wp:heading {"level":3} -->

### The Steps of Learning  





------------------------------------------------------------------------






In every algorithm, the learning process follows this formula:





Predict -&gt; Evaluate -&gt; Tune -&gt; Repeat





When we first throw in a bunch of features, the model initially makes blind **Predictions** as to what the outcome is. Because it makes shots in the dark, the **Evaluation** of the model is going to be very poor initially. The model then learns of its errors, and **Tunes** its hyper-parameters to minimize the errors. After tuning, it **Repeats** the process of prediction, and the cycle continues until a satisfactory Error value is obtained.  





When training the model, the learning process comes from telling the machine where it went wrong, or the Errors it has committed. The Error is derived from the difference of the model output and the desired outcome.



<!-- wp:heading {"level":3} -->

### The Error/Loss Functions  





------------------------------------------------------------------------






When the model makes a prediction, there is bound to be errors in the the desired outcome, and the actual outcome. The difference between the desired and actual outcome can be represented in various ways called Loss Functions.  





Some way of calculating this Error, or Loss Function, are:





-   Classification Accuracy
-   Log Loss
-   Confusion Matrix  
-   Root Mean Square Error (RMSE)
-   F1 Score
-   Area Under Curve (AUC)





These Loss functions tell the model how badly it has done in its job of prediction, and to kindly go back and tune the way it performs its predictions.  







<!-- wp:heading {"level":3} -->

### The Optimization Functions  





------------------------------------------------------------------------






To tune the way it performs predictions, the model uses Optimization Functions.  





Using the Error value produced by either one of those loss functions, the model then tunes itself using Optimization Functions, which adjusts its hyper-parameters, to try to minimize those Error values.





There are also several ways for the model to tune it hyper-parameters based on the Error value computed. I'll only be listing them, as going through each of them requires a post on its own:





-   Gradient Descent
-   Momentum
-   Adaptive Movement Estimation (Adam)
-   Adagrad





These Optimization algorithms are optimizing, or minimizing, the Error value calculated previously.



<!-- wp:heading {"level":3} -->

### Repeat





------------------------------------------------------------------------






So you got your Loss function to tell you how badly you did, and the Optimization function for your model to tweak it's parameters. Now all you have to do is to keep repeating these steps, and your model is "Learning". But wait!  



<!-- wp:heading {"level":3} -->

### Over/Under Fitting





------------------------------------------------------------------------






Is there such a thing as learning too much? In the context of machine learning, this scenario is entirely possible, where you model learns too much about the training data, which results in poor performance on unseen data.





This is analogous to a student studying for his final exam, and the way he does it is to memorize every single questions and answers from the past year papers, with little contextual understanding. Obviously when he takes the final exam, the questions will be different, and he will do very poorly.  





In machine learning, overfitting is a problem when we have over-tuned the parameters in the model to a specific data set, resulting in poor performance in other data sets.





Some ways to overcome Overfitting are:





-   Throw in more data (akin to studying more past year papers)  
-   Cross validation during training
-   Early stopping to stop learning too much
-   Regularization that forces simplicity on your model  
-   Ensemble to take the average of various models  





Underfitting on the other, is not as common of a problem as overfitting. Underfitting means that your model has not learnt much, and as a result it cant perform well. This is analogous to student studying too little for his final exams.





In Overfitting, your model is too complex. In Underfitting, your model is too simple.



<!-- wp:heading {"level":3} -->

### Conclusion  





------------------------------------------------------------------------






So that's it! You've understood the abstracted underling principles of what happens when a machine "Learns", and the possibility of learning too much or too little.





For each prediction, we get an error value, and using this error value, we use optimization functions to change the way we perform our prediction.  





You've also seen some ways to prevent overfitting, which is a more common problem than underfitting.  


