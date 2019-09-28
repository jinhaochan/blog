Title: Counts Based Featurization
Date: 2019-03-24 17:48
Author: jinhaochan
Category: Data Science
Tags: Count Feature
Slug: counts-based-featurization
Status: published

<!-- wp:paragraph -->

While doing the Microsoft Malware Classification challenge, I encountered a way of Feature representation called Count Based Features (CBF).

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

CBF is good to use with very high cardinality features, and it transforms the high number of categories in the data to the number of it's occurrences. This representation is helpful because it extracts out a simple inherent feature of the data: count

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

Below shows a simple example of how we get the CBF of a given feature

<!-- /wp:paragraph -->

<!-- wp:table -->

  ----------- --------------
  **Label**   **Feature1**
  0           A
  0           A
  1           A
  0           B
  1           B
  1           B
  1           B
  ----------- --------------

<!-- /wp:table -->

<!-- wp:paragraph -->

CBF can be done in pandas in a single line

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

`Train.groupby([' Feature1 '])[' Feature1 '].transform('count')`

<!-- /wp:paragraph -->

<!-- wp:paragraph -->

The output of this will give you

<!-- /wp:paragraph -->

<!-- wp:table -->

  Label   **Feature1**
  ------- --------------
  0       3
  0       3
  1       3
  0       4
  1       4
  1       4
  1       4

<!-- /wp:table -->

<!-- wp:paragraph -->

As you can see, the categorical values are all converted their count values!  

<!-- /wp:paragraph -->