Title: SWE Day 13: Clojure Data Types 1
Date: 2020-05-13 10:11
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-data-types1
Status: published

## Value assignment to a variable

In Clojure, we use the keyword `def` to assign or bind a value to a variable name

```
(def var1 "my value")

=> var1

=> "my value"
```

In Clojure, there is rarely any need for re-assigning a variable another value, hence the more prferred word is Binding, where once the variable gets a value, it will stick it with throughout the lifetime of the program.


## Data Structures and Immutability

All of Clojure's data structure are immutable. That means, once assigned with a value, it cannot be changed on the spot. (hence the earlier explanation of Bind over Assign)


## Numbers types in Clojure

An interesting thing about Clojure is that it can work with ratios directly, instead of giving you a weird floating point number

```
93

1.2

1/5
```

Also, BigInts and Floating point types are 'contagious', in that whenever there is an operation that involves such a data type, the result will always be of that type.


## Strings

In Clojure, you are only allowed to use Double Quote to define a string, and never a Single Quote

```
"Hello World!"

"And he said \" Hello World!\""
```

String in Clojure also do not support interpolation, which is inserting string into an already existing string. The only operation that is supported is concatenation via the `str` function

```
(str "\"Hello " "World!\"")

=> "Hello World!"
```

## Maps and Dictionaries

Maps and Dictionaries have a `Key : Value` combination, and it's represented as such

`{:key value}`

You can also Map a value to another object. Here, we can map the string `"add-func"` to the addition function in Clojure

`{"add-func" +}`

The map values can be of any type: Strings, Functions, Maps, Vectors etc


You can also use the function `hash-map` to create a map

```
(hash-map :a 1 :b 2)

=> {:a 1 :b 2}
```

And you can access a values by looking up a map with a key, using the `get` function. If the key does not exist, a `nil` is returned, else, you can define your own default value to return

```
(get {:a 0 :b 1} :b)

=> 1

(get {:a 0 :b 1} :d "default return value")

=> "default return value"
```


To look into a nest map, we can use the keyword `get-in`

```
(get-in {:a 0 :b {:c "nested map"}} [:b :c])

=> "nested map"
```

You can define certain variables as keyword by putting a `:` infront of it. This allows it to function like a key in a key-value pair


```
(:a {:a 1 :b 2})

=> 1

(:d {:a 1 :b 2} "default return value")

=> "default return value"
```

This works exactly the same way as the `get` function with a default value

