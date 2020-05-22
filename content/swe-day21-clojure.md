Title: SWE Day 20: Clojure Functions In Depth 2
Date: 2020-05-20 10:25
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-functions3
Status: published


## Lazy Sequences

We learned previously that when you call a function that works on a sequence like `map`, `filter` or `reduce`, Clojure first calls the function `seq` on it to for a sequence of elements. The returned sequence from `seq` however, are lazy sequences, meaning the actual value of the sequence is not computed until something tries to access it. When it does, it's called realizing the sequence. By doing so, you can theoratically make an infinitely large sequences, because nothing is actually stored in memory.

Lazy Sequences contains two parts:
1. Steps to realize the elements of the sequence
2. Elements that has already been realized

When you call `map`, it does not actually return you the entire mapped sequence, but the steps needed to perform to get the mapped sequence. And when you try to access the sequence element, then the steps are actually performed.

Clojure also does pre-empting realization. When you realize a single element, Clojure will realize a few elements after it as well. This improves lookup time performace.


## Infinite Sequences

Because sequences are lazily realized, you can instantiate an infinite sequence without fearing you would run out of memory. One way to create an infinite sequence in Clojure is via `repeat`, which creates an infinite sequence of arguments you pass in.

```
(take 5 (repeat "value"))
=> ("value" "value" "value" "value" "value")
```

Its like an infinite pool of resources you can dip into.

The function `repeatedly` does the same thing, but instead of a single argument, it takes in a function, and repeatedly calls the function

```
(take 3 (repeatedly (fn [] (rand-int 10))))
=> (1 4 0)
```

Here we are repeatedly calling the `rand-int` function, and taking the first 3 elements it produces.


## Collection Abstraction

Sequence Abstractions deal with each individual element, while Collection Abstraction deals with all the elements in the collection as a whole. Functions such as `empty` and `count` need to account for all the elements inside a collection.

#### into

As all sequence functions call seq, which returns a list rather than the original data structure, in some cases we need to re-cast it back to the original data structure we want. In such cases, we call the function `into`, which casts the list data structure into the desired data structure.

```
(map identity {:key "value"})
=> ([:key "value"])     <-- map returns a list

(into {} (map identity {:key "value"}))
=> {:key "value"}   <-- casting the list back to a map
```

Briefly speaking, into takes two collections, and casts the 2nd collection into the first collection.


#### conj

`conj` does the same thing as into, putting the second collection into the first collection. However, there are slight nuances to how `conj` does it

```
(into [0] [1])
=>[0 1]

(conj [0] [1])
=> [0 [1]]
```


Instead of taking the elements in the second collection to put it in the first like how `into` does it, `conj` takes literally the entire second collection as a whole, and places it inside the first collection.

Thus, when working with `conj`, we want to make sure the elements we are passing into the first collection are the elements themselves, not the collection of elements. In the example below, we are passing in a scalar value of 1, instead of a vector.

```
(conj [0] 1)
=> [0 1]
```


## Calling Functions of Functions


#### apply

`apply` explodes a sequences to it's constituent elements, before passing them into a function. Functionally, it behaves exactly like reduce

```
(apply max [0 1 2])
=> 2
```

#### partial

`partial` is an action that you can define, which you can then stick into any part of a function. The function then performs the original action, but at the same time also performs the partial action.

```
(def add10 (partial + 10))

(add10 3) 
=> 13
```


#### complement

`complement` simply negates a Boolean, changing `true` to `false`, and `false` to `true`

```
(def is-pos? (complement neg?))
(is-pos? 1)  
=> true

(is-pos? -1) 
=> false
```

Here, we compare is the number is negative with `neg?`, but we negate the answer with `complement`, so any negative number returns `true` on `neg?`, which is then complemented and returns `false` on `is-pos?`
