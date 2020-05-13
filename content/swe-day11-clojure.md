Title: SWE Day 11: Function Definitions
Date: 2020-05-11 20:59
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure-functions
Status: published


Functions defined in Clojure also take the same sexpr form, surrounded in brackets

The main parts are:
1. Function name
2. Description of the function
3. Parameters
4. Function body

```
(defn my-function-name  <--1
  "Doc string to define the function"  <-- 2
  [param1 param2 param3]  <-- 3
  (str param1 param2 param3)  <-- 4
)
```


To call the function, you call it like any other operation

```
(my-function-name "hello " "world " "!")

=> "hello world !"
```

To read the docstring from a function, we invoke the `doc` operator. The docstring is also used to generate documentation easily

```
(doc my-function-name)

=> "Doc string to define the function"
```

## Overloading function parameters

We can overload the function parameters by defining multiple possible parameters.

The number of parameters are called `arity`, so a 2 parameter function will be called a 2-arity

```
(defn multi-arity
  ;; 3-arity arguments and body
  ([first-arg second-arg third-arg]
     (str first-arg second-arg third-arg))
  ;; 2-arity arguments and body
  ([first-arg second-arg]
     (str first-arg second-arg))
  ;; 1-arity arguments and body
  ([first-arg]
     (str first-arg)))
```

By defining multi-arity functions, you can do things such as a constructor, or default values when left empty.

```
(defn multi-arity
  "Constructor creates the default name"
  ([name age]
     (str "I am " name ", and I am " age))
  ([age]
     (multi-arity "James" age)))
```

If you only key in your age, the 1-arity body will trigger, with the default name of "James"

If you key in both your name and age, the 2-arity body with trigger.

```
(multi-arity 20)

=> "I am John, and I am 20"

(multi-arity "Jessie" 30)

=> "I am Jessie, and I am 30"
```

Its recommended to write your different n-arity bodies so that they are related. What this means is that they all run the same logic, just with different parameters. You dont want your different n-arity bodies doing completely different things.

### Dynamic Parameters in a Function

In the examples above, we had fixed numbers of parameters, but Clojure also allows you to make a function have variable number of parameters called a `rest parameter`, or putting the rest of the stuff in it.

```
(defn basic-function
  [name]
  (str "My name is: " name))

(defn mapper-function
   [& various-parameters]
  (map basic-function various-parameters))

(mapper-function "Billy" "John" "Jessie")
=> ("My name is Billy"
      "My name is John"
      "My name is Jessie")
```

If we look at `mapper-function`, we introduce a new operator called `map` here, which broadcasts all the variables to function `basic-function`.

`mapper-function` will take in as many variables, and they will be placed in `various-parameters`, which will then be broadcasted to `basic-function`

### Destructuring Parameters to a function

Clojure allows you destructure parameters passed to a function. What this means is that, when the function recieves an input with some form of structure like a list, it is able to break it down and process each element. It does this by binding each element in the structure to the number of variables defined.

```
(defn list-destructuror
  [[first-element second-element & other-elements]]
  (println (str "First Element: " first-element))
  (println (str "Second Element: " second-element))
  (println (str "The rest of the Elements: "
                (clojure.string/join ", " other-elements))))

(list-destructor ["Apple", "Orange", "Vegetables", "Cake"])
=> First Element: Apple
=> Second Element: Orange
=> The rest of the Elements: Vegetables, Cake

```

In this example, we're passing in a list structure, thats why in the function parameter, we define a list `[[...]]`. We can pass in other structure like a vector as well, and this case, we need to define a vector `[{...}]`

```
(defn vector-deconstructor
   [{key1 :va1 key2 :val2}]
  (println (str "First value: " va1))
  (println (str "Second value: " val2)))

(vector-deconstructor {:key1 10 :key2 20})
=> First value: 10
=> Second value: 20
```

We can compress the above vector deconstrutor above to get the exact same result, but with a different definition style. The keyword `:as` keeps the original uncompressed structure together.

```
(defn vector-deconstructor
   [{:keys [val1 val2]} :as original-map]
  (println (str "First value: " va1))
  (println (str "Second value: " val2)))
```

### Next Lesson

Today, we learnt about how to define functions. In the next lesson, we'll be looking at how to construct the function body
