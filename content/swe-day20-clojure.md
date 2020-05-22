Title: SWE Day 20: Clojure Functions In Depth 1
Date: 2020-05-20 10:25
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-functions2
Status: published

In Clojure, operations do not care about the actual data structure of the object it is operating on, as long as it can perform sequence operations on the object. For example, you can call the same function `map` on a list, set, vector, or a hash, even though they all have different data structures.

## Sequences

Sequences are data structures that have some sort of linear order to it, that you can iterate on in sequential way. The elements inside a sequence are called sequence elements

Core sequence, or seq, functions are `first`, `rest`, and `cons`, and if they are able to work on the data structure, then you can say that the data structure implements the sequence abstraction.

```
(map inc '(1 2 3))
=>(2 3 4)

(map inc #{1 2 3})
=>(2 4 3)

(map inc [1 2 3])
=>(2 3 4)
```


## Core Seq Functions

`first` returns the value of the requested node

`rest` returns all remaining values after the requested node

`cons` adds a new node to the beginning of the sequence

By chaining these 3 core functions together, you can implement any sequence functions such as `map`, `reduce` and `filter`

Likewise, `map`, `reduce` and `filter` can work with any data structure as long as they implement these 3 core seq functions.


## Indirection and Polymorphism

Underlying of the 3 core seq functions are concepts of Indirection and Polymorphism, which means that they are able to perform different actions based on the different inputs. Polymorphic functions dispatch different function bodies based on the arguments given.

`first`, `rest` and `cons` are all polymorphic, and hence the abstracted functions like `map`, `reduce` and `filter` are able to work on different data structures.

Whenever you call `map`, it first calls `seq`, which produces a data strucutre that `first`, `rest` and `cons` can operate on. In this case, it always produces a list. In the case of `seq` on a `map`, it returns a list of vectors of those elements.

```
(seq '(1 2 3))
=> (1 2 3)

(seq [1 2 3])
=> (1 2 3)

(seq #{1 2 3})
=> (1 2 3)

(seq {:key1 va1 :key2 val2})
=> ([:key1 val1] [:key2 val2])

```

## More Maps

When you pass in two collections to a `map` function, it will operate between the first element of each collection, second element of each collection, and so on. If the collections are of different sizes, it stops at the smallest collection

```
(map str [1 2 3] [4 5 6])
=>("14" "25" "36")

(map str [1 2 3] [4 5 6 7])
=>("14" "25" "36")
```

Mapping a key on a map data structure returns all the values of the key

```
(def identities
  [{:alias "Batman" :real "Bruce Wayne"}
   {:alias "Spider-Man" :real "Peter Parker"}
   {:alias "Santa" :real "Your mom"}
   {:alias "Easter Bunny" :real "Your dad"}])

(map :real identities)
=> ("Bruce Wayne" "Peter Parker" "Your mom" "Your dad")
```


## More Reduce

Reduce takes in 3 arguments

```
(reduce
  <function>
  <initial value>
  <collection>)
```

The function takes in the initial value and collection as its inputs, and performs whatever operations it has on them.

## take, drop, take-while, drop-while

`take` and `drop` takes in a number and a sequence. It then returns the n element of the sequences, or returns the elements of the seuqence after dropping the first n elements.

```
(take 3 [1 2 3 4 5 6 7 8 9 10])
=> (1 2 3)

(drop 3 [1 2 3 4 5 6 7 8 9 10])
=> (4 5 6 7 8 9 10)
```

`take-while` and `drop-while` does that same thing, but instead of a number, it takes in a predicate, which stops taking or dropping only when the predicate evaluates to false.

```
(def food-journal
  [{:month 1 :day 1 :human 5.3 :critter 2.3}
   {:month 1 :day 2 :human 5.1 :critter 2.0}
   {:month 2 :day 1 :human 4.9 :critter 2.1}
   {:month 2 :day 2 :human 5.0 :critter 2.5}
   {:month 3 :day 1 :human 4.2 :critter 3.3}
   {:month 3 :day 2 :human 4.0 :critter 3.8}
   {:month 4 :day 1 :human 3.7 :critter 3.9}
   {:month 4 :day 2 :human 3.7 :critter 3.6}])

(take-while #(< (:month %) 3) food-journal)
=> ({:month 1 :day 1 :human 5.3 :critter 2.3}
      {:month 1 :day 2 :human 5.1 :critter 2.0}
      {:month 2 :day 1 :human 4.9 :critter 2.1}
      {:month 2 :day 2 :human 5.0 :critter 2.5})

(drop-while #(< (:month %) 3) food-journal)
=> ({:month 3 :day 1 :human 4.2 :critter 3.3}
      {:month 3 :day 2 :human 4.0 :critter 3.8}
      {:month 4 :day 1 :human 3.7 :critter 3.9}
      {:month 4 :day 2 :human 3.7 :critter 3.6})

```

In this example, `take-while` gets a predicate `#(< (:month %) 3)`, which checks if the month value is less than 3, and only takes those map values.

`drop-while` does the same thing, except it drops values until the predicate is false. i.e. all months that are less than 3 are dropped.


## filter and some

`filter` works in the same way as `take-while` and `drop-while`, which basically filters away values that evaluate the predicate to false.

```
(filter #(< (:human %) 5) food-journal)
; => ({:month 2 :day 1 :human 4.9 :critter 2.1}
      {:month 3 :day 1 :human 4.2 :critter 3.3}
      {:month 3 :day 2 :human 4.0 :critter 3.8}
      {:month 4 :day 1 :human 3.7 :critter 3.9}
      {:month 4 :day 2 :human 3.7 :critter 3.6})
```

The downside is that `filter` evaluates the entire collection, while `take-while` and `drop-while` only operates on the head. Depending on the use case, either will be more suitable and computationally efficient.


`some` returns a `true` if at least one value in the collection evaluates the predicate to be true, and `false` if all the values in the collection evalute to be false.

```
(some #(> (:critter %) 3) food-journal)
=> true
```

You can return the entries that evalute to true with the `and` function

```
(some #(and (> (:critter %) 3) %) food-journal)
=> {:month 3 :day 1 :human 4.2 :critter 3.3}
```

This is because `(and true %)`, where `%` contains the value that returns true, will always evaluate to `true`, therefore returning he value


## sort and sort-by, concat

`sort` sorts the sequence in order, while `sort-by` takes in a function to apply on the elemets, and sorts on the return value of that function

```
(sort [3 1 2])
=> (1 2 3)

(sort-by count ["aaa" "c" "bb"])
=> ("c" "bb" "aaa")
```

In the `sort-by` example, we apply the function `count` on each of the elements, and sort them based on the return value of `count`

`concat` simply takes in members of a sequence, and appends one to the end of the other

```
(concat [1 2] [3 4])
=> (1 2 3 4)
```
