Title: SWE Day 19: Exercises-3
Date: 2020-05-19 09:12
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-exercises3
Status: published

We're going to attempt question 6 from the exercise page [here](https://www.braveclojure.com/do-things/#Exercises)


## Question 6

Create a function that generalizes `symmetrize-body-parts` and the function you created in Exercise 5. The new function should take a collection of body parts and the number of matching body parts to add. If you’re completely new to Lisp languages and functional programming, it probably won’t be obvious how to do this. If you get stuck, just move on to the next chapter and revisit the problem later.

As a generalization of the problem, instead of returning a fixed number of body parts in the function `radial-parts`, we need to accept another paramater that tells us how many parts to return. Also, if the number of parts are odd, we need to return a central unit, else, we return equal number of left and rights.


The inputs for the program will be the same as the hobbit

```
(def asym-hobbit-body-parts [{:name "head" :size 3}
                             {:name "left-eye" :size 1}
                             {:name "left-ear" :size 1}
                             {:name "mouth" :size 1}
                             {:name "nose" :size 1}
                             {:name "neck" :size 2}
                             {:name "left-shoulder" :size 3}
                             {:name "left-upper-arm" :size 3}
                             {:name "chest" :size 10}
                             {:name "back" :size 10}
                             {:name "left-forearm" :size 3}
                             {:name "abdomen" :size 6}
                             {:name "left-kidney" :size 1}
                             {:name "left-hand" :size 2}
                             {:name "left-knee" :size 2}
                             {:name "left-thigh" :size 4}
                             {:name "left-lower-leg" :size 3}
                             {:name "left-achilles" :size 1}
                             {:name "left-foot" :size 2}])
```

And now we modify the original solution

```
(defn part-factory
  "takes in a part, sideness, and number of parts to generate"
   [part number-of-parts side]
   (loop [part-col []]
         (if (= (count part-col) number-of-parts)
           part-col
           (recur (conj part-col {:name (clojure.string/replace (:name part) #"^left-" (str side (inc (count part-col)) "-"))
             :size (:size part)} ))))
)

(defn matching-parts
  "takes in a map and number of parts to return. If the number of parts is odd, we return a central piece, else we return equal number of lefts and rights."
  [part number-of-parts]
  (if (even? number-of-parts)
    (into []
    (concat
       (part-factory part (/ number-of-parts 2) "left")
       (part-factory part (/ number-of-parts 2) "right")
    ))
    (into []
    (concat
       (part-factory part (int (/ number-of-parts 2)) "left")
       (part-factory part (int (/ number-of-parts 2)) "right")
       (part-factory part 1 "central")
    ))
))

(defn general-symmetry
  "Takes in a vector map of body parts, and makes it symmetric, radially or not"
  [asym-body-parts number-of-parts]
  (reduce 
    (fn [final-body-parts part] (into final-body-parts (set (matching-parts part number-of-parts))))
    [] 
    asym-body-parts))
```

In `matching-parts`, I refactored the parts generator to another function `part-factory`, which does the actual making of body parts. We check if the number of parts passed in are even or odd. If it's odd, we do one more extra step of generating the central part.

