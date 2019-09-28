Title: Feature Engineering
Date: 2019-03-17 09:41
Author: jinhaochan
Category: Data Science
Tags: Feature Engineering
Slug: feature-engineering
Status: published



Feature Engineering is one of the neglected portion of machine learning. Most topics revolve around Model Training (parameter tuning, cross validation). While that might be really important, feature engineering is equally important as well, but I can't seem to find good resources that talk about this. I suspect this is because to perform feature engineering, you need expert knowledge of the data, and what it represents.





A typical workflow would look something like this



<!-- wp:list {"ordered":true} -->

1.  Project Scoping / Data Collection
2.  Exploratory Analysis (EDA)
3.  Data Cleaning
4.  **Feature Engineering**
5.  Model Training
6.  Project Delivery / Insights



<!-- wp:heading {"level":3} -->

### What is not Feature Engineering





------------------------------------------------------------------------






-   Data cleaning (Outlier detection, Missing values)
-   Scaling and Normalization
-   Feature Selection





I would classify these as data massaging, as you're just changing the data (except for Feature Selection). Feature Engineering is the creation of new data.  



<!-- wp:heading {"level":3} -->

### What is Feature Engineering





------------------------------------------------------------------------






There are a few ways to create new features from existing ones



<!-- wp:heading {"level":4} -->

#### Indicator Variables





Indicator variables are new variables that help you isolate data. This new feature is discriminative and can help separate the data.





Examples:





-   Threshold: If you're studying data on alcohol consumption, you could create a new binary feature if the person is `>=21` years old. The expert knowledge in this is knowing where your data came from, and what is the minimum age of drinking in that country/state
-   Special Events: If you're studying sales, there could be seasons that have higher sales, such as `isChristmas`, `isSinglesDay` or `isBlackFriday`. Expert knowledge is knowing what special events there are
-   Groupings: You can create artificial groups for the data, for example in network traffic, you can group the, according to protocols or source. Expert knowledge is knowing how to interpret the data, and what grouping makes sense



<!-- wp:heading {"level":4} -->

#### Interaction of Features





Features can interact with each other to create new variables. Interaction here means some mathematical operation between them.





Examples:





-   Sum of Features: If you're looking at sales of individual items, a new feature might be `overallSales`, where you add the sales of each item together
-   Product of Features: If you're looking at wages, and you have features like `hourlyRate`, and `workingHours`, you can create a new feature called `totalPay`





The expert knowledge in these areas are knowing how the features interact with each other to produce new features. However, from unfortunate experience, I've seen some feature interactions that makes absolutely no sense, but the model seems to think otherwise. An example I saw was a new feature created from the multiplication of `screenHorizontalSize` and `totalRAM` which makes absolutely no sense, but it gave a boost in prediction accuracy. Machine Learning really is still a black box.



<!-- wp:heading {"level":4} -->

#### Feature Representation





For some features, you can better represent them in other formats that give more information.





Examples:





-   Date to integer: When give a `datetime` format string, it almost always makes sense to decompose it to it's integer components such as `day`, `month` and `year`. More than that, you can create features such as `isWeekday` or `isPeakHour`
-   Sparse classes to Other: In a categorical class, if some classes are hugely under-represented, they can be grouped together, and classified as `Others`



<!-- wp:heading {"level":4} -->

#### External Data Augmentation  





Another way to create new features is to bring in new data such as Geolocation information. These external data can be used to add in new features, which in turn can interact, represent or isolate current features.



<!-- wp:heading {"level":3} -->

### Conclusion  





------------------------------------------------------------------------






Indicator Features, Feature Interactions, Feature Representation, External Data Augmentation are all several way to engineer new features. This is different from data massaging.





Feature Engineering is extremely important in your Machine Learning workflow.


