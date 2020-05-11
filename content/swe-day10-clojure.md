Title: SWE Day 10: Clojure Syntax and Control Flows
Date: 2020-05-10 19:36
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure-syntax
Slug: clojure-syntax
Status: published


The syntax to clojure is pretty straight forward, and it follows the [S-expression syntax](https://www.computerhope.com/jargon/s/s-expression.htm), or sexpr. Basically, all your commands and instructions are encapsulated by brackets, and they follow this pattern

`(operator operand-1 operand-2 ... operand-n)`

Every. Single. One.

I'll throw a few examples down below

`(+ 1 2 3)`

`=> 6`

`(str "join" " me" " in" " learning")`

`=> "join me in learning"`

## Control Flow

There are a few kinds of control flows in Clojure

1. `if-else`
2. `do`
3. `when`
4. `nil`
5. `=`
5. `or`
6. `and`

### if-else

```
(if (boolean)
  then do this
  else do this)
```

```
(if true
  "true flow"
  "false flow")

=> "true flow"
```

More complex examples would be

```
(if true
  (if false
    "true then false"
    "true else true")
  "else false")

=> "true else true"
```

If you omit the else branch, and the boolean operator is false, the condition return a `nil`

No else statement:

```
(if false
  "false")

=> nil
```

### do

A do is simply a wrapper around many lines of code to encapsulate them. In the earlier examples, the if-else condition only ran a single line of code. If you want to run more lines of code, you can wrap it with a `do` operator.

```
(if true
  (do (println "true operation 1")
      "true operation 2")
  (do (println "false operation 1")
      "false operation 2"))

=> "true operation 1"
=> "true operation 2"
```

Notice that we need to wrap the `true operation 1` with a println, because otherwise, it will not print to the console, but it will get executed anyway.

### when

A `when` operator is used when you want to do multiple thing if something is true. The `when` is a combination of `if` and `do`

```
(when true
  (println "true operator 1")
  "true operator 2")

; => "true operator 1"
; => "true operator 2"
```

### nil

In clojure, `nil` and `false` are falsey, everything else is truthy, even a 0 or negative numbers.

`nil` compares if a value is nil, and only nil. Not 0 or anything else.

```
(nil? 1)

=> false

(nil? nil)

=> true
```

### =

Compares equality between 2 values

```
(= 1 1)

=> true

(= 1 2)

=> false

(= nil nil)

=> true
```

### and/or

`or` returns the first truthy value, or the last value

`and` returns the first falsely value, or the last truthy value

```
(or false nil "str1" "str2")
=> "str1"

(or (= 0 1) (= "yes" "no"))
=> false

(or nil)
=> nil
```

```
(and "str1" "str2")
=> "str2"

(and "str1" nil false)
=> nil
```
