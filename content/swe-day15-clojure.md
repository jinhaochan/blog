Title: SWE Day 15: Example Program
Date: 2020-05-15 16:37
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-example-program
Status: published


We're going to be looking at an example program from the website, and do a deep analysis of what it does. Hopefully, we're also going to be proficient enough to tinker with some of the programs logic, to prove our understanding of the concepts. You can find the description of the exercise [here](https://www.braveclojure.com/do-things/#Pulling_It_All_Together)

## Inputs

The input to the program is `asym-hobbit-body-parts`, which binds the a vector of maps. Each map has 2 keys, `name` and `size`.


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


## Goal of the Program

As you can see in the vector above, it only consists of the left side of the hobbit. The goal is to add in new maps into the vector to complete the right sidedness of the hobbit

## Overview of the Program

This is the solution program given to us

```
01 - (defn matching-part
02 -   [part]
03 -   {:name (clojure.string/replace (:name part) #"^left-" "right-")
04 -    :size (:size part)})
05 -
06 - (defn symmetrize-body-parts
07 -   "Expects a seq of maps that have a :name and :size"
08 -   [asym-body-parts]
09 -   (loop [remaining-asym-parts asym-body-parts
10 -          final-body-parts []]
11 -     (if (empty? remaining-asym-parts)
12 -      final-body-parts
13 -       (let [[part & remaining] remaining-asym-parts]
14 -         (recur remaining
15 -                (into final-body-parts
16 -                      (set [part (matching-part part)])))))))
```

It consists of 2 functions, `matching-part` and `symmetrize-body-parts`

`symmetrize-body-parts` loops through the given input about, and calls `matching-part`.

`matching-part` returns a map of the right-side, with the same size


## Examining `symmetrize-body-parts`

#### Lines 6, 7, 8: Function Definition

```
06 - (defn symmetrize-body-parts
07 -   "Expects a seq of maps that have a :name and :size"
08 -   [asym-body-parts]
```

We first define the function, which takes in parameters `[asym-body-parts]`, and give a brief docstring about what inputs the function expects

#### Lines 9, 10: Looping

```
09 -   (loop [remaining-asym-parts asym-body-parts
10 -          final-body-parts []]
```

Here we're introduced to a new function called `loop`, which provides a way to do recursion in Clojure

In lines 9 and 10, loop binds values with variables. In this case, we're binding `asym-body-parts` to `remaining-asym-parts`, and binding an empty vector to `final-body-parts`.

The `loop` function always contains a `recur` somewhere in the body, which performs a certain action, before return to the top of the loop.When it returns to the top of the loop, it passes new values to bind to the initial variables defined at the top.

For the sake of explanation, if we jump to lines 14, 15 and 16, `recur` passes back the values of `remaining`, and the results of `(into final-body-parts (set [part (matching-part part)]))` back to the top of the loop, which binds them to the variables `remaining-asym-parts` and `final-body-parts`

Essentially, you are doing something like this

```
remaining-asym-parts = remaining

final-body-parts = (into final-body-parts (set [part (matching-part part)]))
```

#### Lines 11, 12: If True

```
11 -     (if (empty? remaining-asym-parts)
12 -      final-body-parts
```

The loop terminates when there is no `recur` being called. Here, the control flow is defined with the `if` statement, which checks if `remaining-asym-parts is empty`. If that is true, we return `final-body-part`. If that evaluates to false, there are still elements in `remaining-asym-parts`, and we evaluate the else body

#### Lines 13, 14, 15, 16: Else, Let

```
13 -       (let [[part & remaining] remaining-asym-parts]
14 -         (recur remaining
15 -                (into final-body-parts
16 -                      (set [part (matching-part part)])))))))
```

If `remaining-asym-parts` is not empty, we evaluate the else body.

The else body is surrounded by a `let` function

`let` binds names to values, before returning something

```
(let [name "value"] name)

=> "value"
```

Here, we're binding `"value"` to `name`, and returning `name`, which prints `"value"`

`let` also allows you to perform destructuring, which deconstructs an existing data structure to another one. When we call `(let [[part & remaining] remaining-asym-parts ...`, we are deconstructing `remaining-asym-parts` into the new structure `[part & remaining]`

What `[part & remaining] remaining-asym-parts` does is it assigns the first value of `remaining-asym-parts` to `part`, and the rest of the values into `remaining` with the keyword `&`. So you now have a resultant vector that looks like this `[val1 (val2 val3 val4 ...)]`, where `val1` is `part` and `(val2 val3 val4 ...)` is `remaining`


In the return portion of the `let` function, it then calls the `recur` function as described above, which throws back some variables for rebinding, and goes back up to the loop. Here, we're throwing `remaining`, which consists of the orignal `remaining-asym-parts` less the first element, and we're also throwing up `(into final-body-parts (set [part (matching-part part)]))`

Let's take a look at what `(into final-body-parts (set [part (matching-part part)]))` does


#### Lines 15, 16: Into, and Function Calling

```
15 -                (into final-body-parts
16 -                      (set [part (matching-part part)])))))))
```

`into` is a function to add the a new element into the existing element `final-body-parts`. The new element is created with by calling `(set [part (matching-part part)])`. 

When both the data type of the `into` functions are sets, the are merged together. Read more about `into`  [here](https://clojuredocs.org/clojure.core/into)

We want to place the `set` of `[part (matching-part part)]`, incase part does not have symmetry, such as nose or abdomen. In that case, `matching-part` will return the same value as part.


#### Line 1, 2, 3, 4: `matching-part` Function

```
01 - (defn matching-part
02 -   [part]
03 -   {:name (clojure.string/replace (:name part) #"^left-" "right-")
04 -    :size (:size part)})
```

The `matching-part` function is pretty straight forward. It takes in a single argument `part`, which is a map containing `{:name "val" :size val`, and returns a set with keys `:name` and `size`. `:name` has a value that takes the original string, and replaces the `"left"` with `"right"`, while `:size` returns the original size defined in `part`

#### Putting It All Together

From the top, we loop through the `remaining-asym-parts`, and places updated right-sidedness into `final-body-parts`.

If `remaining-asym-parts` is empty, we are done, and we return `final-body-parts`, which contans all the left and right parts of the hobbit.

If `remaining-asym-parts` is not empty, we destructure `remaining-asym-parts` by taking out the first element, and passing it to `matching-part` function, which returns the right-sidedness of things.

If the body part is not symmetrical such as nose or abdomen, we remove the duplicate by calling `set`

We return the values `remaining` and `final-body-parts` back up to the loop, and keep going until `remaining-asym-parts` is empty
