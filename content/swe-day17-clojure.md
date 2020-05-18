Title: SWE Day 17: Refactoring Hobbit Code
Date: 2020-05-17 10:24
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-exercises2
Status: published


Today we're going to be refactoring our hobbit code we saw in [day 15](https://www.osfork.com/clojure-example-program.html#clojure-example-program) with the introduction of a new function called `reduce`


## Refactoring the Hobbit code

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


To refactor the code, we're going to introduce one new function called `reduce`. At a more abstract level, `reduce` takes in a collection, an operator, and returns a single result, after applying (map) and aggregating (reduce) the operator on the collection.

In Clojure, `reduce` works like this 

```
(reduce + [1 2 3 4])

=> 10
```

What this is doing is taking an operator `+` and applying it to a collection `[1 2 3 4]`, before aggregating the result. Its telling Clojure to do this

`(+ (+ (+ 1 2) 3) 4)`

Which adds the first two numbers, take the results, and adds in the next number and so on, until there are no more numbers left.

If we add an initial value to the `reduce` function, it works exactly the same way, just that the operator will work on the initial value and the first value in the list


```
(reduce + 1 [2 3 4])

=> 10
```

The basic layout of the function will thus looking something like this

`(reduce operator <optional-initial-value> collection)`

## Really Refactoring the code now

By looking at how `reduce` is defined, we can modify our loop in the program to compress it into a single reduce function

```
01 - (defn better-symmetrize-body-parts
02 -  "Expects a seq of maps that have a :name and :size"
03 -   [asym-body-parts]
04 -   (reduce (fn [final-body-parts part]
05 -             (into final-body-parts (set [part (matching-part part)])))
06 -           []
07 -           asym-body-parts))
```

If we look lines 4, 5, 6 and 7, we see that we have replaced the entire body of the original function with a single reduce call. The inputs to the reduce function are, and i'll break it down for easier analysis:

```
(reduce
  Operator
  Initial-Value
  Collection
)

(reduce
  (fn     <-- Anonymous Function
   [final-body-parts part]        <-- Arguments
   (into final-body-parts (set [part (matching-part part)])))     <-- Operator Body
  []      <-- Initial Value
  asym-body-parts        <-- Collection to work on
)
```

The operator is defined as an anonymous function, which takes in `final-body-parts` and `part`.

Based on the initial value of an empty vector, the first operation of reduce passes in an empty vector, and the first value of `asym-body-parts`. The empty vector is assigned to `final-body-parts`, and the first value is assigned to `part`.

We then call the operator body, which does the matching parts generation and places it into `final-body-parts`.

In the next operation of reduce, the return value of the first operation is passed in as the initial value, and that is `final-body-parts` containing the matching parts of the first `part`.

In essence, it's doing something like this:

`(create-matching (create-matching (create-matching "left ear") "right hand") "left eye")`

## When to use Reduce

We saw how the `reduce` function was able to compress the `loop` operator into a single line, but should we always do this?

When given a `reduce` function, the reader of the code will always know that the input is a collection, and the output is a aggregated result. Whereas if they see a `loop` function, they might not know what it is doing until the read all the lines in it.

You would want to use `reduce` when you have a collection you want to walk through, and apply a function to it and aggregate the results.

You might want to use `loop/recur` when your operations are more complex than applying a function, or your return result is not an aggregation.

In terms of time-complexity, we see that `reduce` is actullay SLOWER than `loop` in some cases. [An example here](https://hackernoon.com/faster-clojure-reduce-57a104448ea4)

I think this example is only meant to show case that there are different ways of solving the same problem with the different functions Clojure has, and it's not to say which is the most optimal or elegant solution.
