Title: SWE Day 18: Exercises-2
Date: 2020-05-18 21:03
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-exercises2
Status: published

We're going to attempt question 5 from the exercise page [here](https://www.braveclojure.com/do-things/#Exercises)


## Question 5

Create a function that’s similar to `symmetrize-body-parts` except that it has to work with weird space aliens with radial symmetry. Instead of two eyes, arms, legs, and so on, they have five.

To tackle this question, we need to understand what is radial symmertry, which is a form of symmetry where there are regular parts around a central axis. If we take a starfish for example, it has a radial symmetry of 5.

Therefore, for each body part, the checks are going to be for 2 lefts, 2 rights, and a central piece

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
(defn radial-parts
  "takes in a map, and returns a vector of 2 lefts, 2 rights, and a central piece"
  [part]
  [
    {:name (clojure.string/replace (:name part) #"^left-" "left1-")
     :size (:size part)}
    {:name (clojure.string/replace (:name part) #"^left-" "left2-")
     :size (:size part)}
    {:name (clojure.string/replace (:name part) #"^left-" "right1-")
     :size (:size part)}
    {:name (clojure.string/replace (:name part) #"^left-" "right2-")
     :size (:size part)}
    {:name (clojure.string/replace (:name part) #"^left-" "central-")
     :size (:size part)}
  ])

(defn radial-symmetry
  "Takes in a vector map of body parts, and makes it radially symmetric"
  [asym-body-parts]
  (reduce 
    (fn [final-body-parts part] (into final-body-parts (set (radial-parts part))))
    [] 
    asym-body-parts))
```

What `radial-parts` does is take in a left-sided part, and returns the 5 parts of it. In `radial-symmetry`, its mostly the same except in the reducer, where we don't have to pass in the original part, since it will be replaced.


## Alternative Solution

Here's an alternative solution by someone who is way senior than me

```
(ns tmp.core
  (:require [clojure.string :as s]))

(def asym-hobbit-body-parts
  [{:name "head" :size 3}
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

(defn parts [part]
  (map (fn [part d] (update part :name s/replace #"left-" d))
       (repeat part)
       ["left-1-" "left-2-" "right-1-" "right-2-" "central-"]))

(defn symmetrize-part
  [{:keys [name] :as part}]
  (if (s/starts-with? name "left-")
    (parts part)
    [part]))

(defn symmetrize [parts]
  (mapcat symmetrize-part parts))

(symmetrize asym-hobbit-body-parts)
```
