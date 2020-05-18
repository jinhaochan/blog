Title: SWE Day 16: Exercises-1
Date: 2020-05-15 16:37
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-exercises1
Status: published

Today we're gonna be doing the given exercises of this Chapter. You can find the exercises [here](https://www.braveclojure.com/do-things/#Exercises). For each of these exercises, i'm going to be doing them on the `lein repl`

1. Use the str, vector, list, hash-map, and hash-set functions.

2. Write a function that takes a number and adds 100 to it.

3. Write a function, `dec-maker`, that works exactly like the function `inc-maker` except with subtraction:

```
(def dec9 (dec-maker 9))
(dec9 10)
=> 1
```

4. Write a function, `mapset`, that works like map except the return value is a set:

```
(mapset inc [1 1 2 2])
=> #{2 3}
```

5. Create a function that’s similar to symmetrize-body-parts except that it has to work with weird space aliens with radial symmetry. Instead of two eyes, arms, legs, and so on, they have five.

6. Create a function that generalizes symmetrize-body-parts and the function you created in Exercise 5. The new function should take a collection of body parts and the number of matching body parts to add. If you’re completely new to Lisp languages and functional programming, it probably won’t be obvious how to do this. If you get stuck, just move on to the next chapter and revisit the problem later.


## Question 1

Use the str, vector, list, hash-map, and hash-set functions.

```
user=> (str "Hello " "World!")

"Hello World!"

user=> (vector 1 2 3 4)

[1 2 3 4]

user=> (hash-map 1 2 3 4)

{1 2, 3 4} <-- the 1 and 3 becomes the key, and the 2 and 4 becomes the value

user=> (hash-set 1 1 2 3)

#{1 3 2} <-- the duplicate 1 is removed
```


## Question 2

Write a function that takes a number and adds 100 to it.

```
(defn adder
 "Adds 100 to the given number"
 [input_val]
 (+ input_val 100))

user=> (adder 20)
120
```


## Question 3

Write a function, `dec-maker`, that works exactly like the function `inc-maker` except with subtraction:

```
(def dec9 (dec-maker 9))
(dec9 10)
=> 1
```

```
(defn dec-maker
 "Subtracts n from the given number"
 [n]
 #(- % n)) <-- n belongs to the 9, while % belongs to whatever what was passed in

user=> (def dec9 (dec-maker 9))
user=> (dec9 10)
1
```


## Question 4

Write a function, `mapset`, that works like `map` except the return value is a set:

```
(mapset inc [1 1 2 2])
=> #{2 3}
```

```
(defn mapset
 "Returns a set of the map operator"
 [operator [& mapval]]
 (set (map operator mapval)))

=> (mapset inc [1 1 2 2])
#{3 2}
```


