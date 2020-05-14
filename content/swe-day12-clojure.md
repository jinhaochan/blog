Title: SWE Day 12: Function Body
Date: 2020-05-12 07:35
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-function-body
Status: published


### Function Return Values

The return value of the function body is always the last form evluated

```
(defn illustrative-function
  []
  (+ 1 304)
  30
  "joe")

(illustrative-function)
=> "joe"
```

### Anonymous Functions

You can define anonymous functions with the `fn` keyword. In this case, you don't have to put in a function name or docstring, but just the parameters and function body. This is similar to lambda functions, which are nameless operations.

```
(fn [param-list]
  function body)
```

```
(map (fn [name] (str "Hi, " name)
  ["Jessie" "James"])

=> ("Hi, Jessie" "Hi, James")
```

Another way to create anonymous functions is via `#` combined with `%`. These are called reader macros

```
(#(* % 3) 8)
=> 24

```

```
(map #(str "Hi, " %)
  ["Jessie" "James"])

=> ("Hi, Jessie" "Hi, James")
```

The `%` symbol are where the arguments will be placed in the function body, which can be accessed via certain modifiers

To access the first, second and third argument, you would use `%1`, `%2` and `%3`

```
(#(str %1 " and " %2) "arg1" "arg2")
; => "arg1 and arg2"
```

You can also do the-rest-of-the-arguments with `&`

```
(#(identity %&) "arg1" "arg2" "arg3")

=>("arg1" "arg2" "arg3")
```

### Functions return Functions, and scopes

A function can return a function, and when it does that, the returned function has access to the scope of the function doing the returning. The returned function are called `closures`

```
(defn str-maker
  [arg1]
  #(str % arg1))

(def str-maker2 (str-maker "string 1"))

(str-maker2 "string 2")

=>"string 2string 1"
```

See that `string 1` goes into `arg1`, while whatever you pass in later goes into the `%` place
