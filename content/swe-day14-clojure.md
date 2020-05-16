Title: SWE Day 14: Clojure Data Types 2
Date: 2020-05-14 10:11
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-data-types2
Status: published

## Vectors

Vectors are defined with a square bracket

`[1 2 3]`

You can get an element inside the a vector via it's index also with the `get` function. Vectors are 0 indexed

```
(get [1 2 3] 0)

=> 1
```

Creating a vector is done with the `vector` keyword

```
(vector 1 2 3)

=> [1 2 3]
```


And you can add elements to the end of the vector with `conj`. You ONLY add elements to the end

```
(conj [1 2 3] 4)

=> [1 2 3 4]
```

## Lists

You define a list by adding a single quote and a bracket at the front

```
'(1 2 3 4)

=> (1 2 3 4)
```

You can access the elements in the list with the `nth` function

```
(nth '(1 2 3) 0)

=> 1
```

You can also create a list with the `list` keyword

```
(list 1 "string" 3.4)

=> (1 "string" 3.4)
```

And like vectors, you can add elements to the list with `conj`. For lists, elements are added at the START of the list

```
(conj '(1 2 3) 0)

=> (0 1 2 3)
```

Choosing between a list or vector depends on your use case, and if your operations need to insert values to the front or the back of the group of elements.


### Sets

Sets are a collections of unique values. Hashsets are defined with a `#` in front a curly braces

`#{1 2 3}`

or you can use the `hash-set` keyword to instantiate a hashset

```
(hash-set 1 2 3)

=> #{1 2 3}
```

You can convert a vector into a set with the `set` keyword

```
(set [1 2 3])

=> #{1 2 3}
```

Membership checking can either be done with `get`, or `contains?`. `get` returns the value, or `nil`, while `contains` returns a `true` or `false` depending if the element exists in the set.

```
(contains #{1 2 3} 1)

=> true

(contains #{1 2 3} 4)

=> false
```

You might want to prefer using `contains?` for membership checking, as when `get` returns a nil value, you might not know if the value was truly `nil`, or did not exist.



