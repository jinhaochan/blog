Title: Python Tips and Tricks
Date: 2018-11-04 22:32
Author: jinhaochan
Category: Software Engineering
Slug: python-tips-and-tricks
Status: published

Summary of Python tips, tricks, and to-dos
------------------------------------------

These pointers are what I picked up from the book `Python Tricks: The Book`

The book itself is a summary, and here i'll be doing a summary of a summary.

Python is great because of its flexibility, but that itself could potentially be a double edged sword. It can be so easy to abuse and write really messy code, yet the program still runs fine.

Lets talk about the points made in the book. I only picked out points that I feel that are useful and that I have very little exposure to. Don't get me wrong, all the points in the book are great, just some greater than others.

Assertions
----------

If the asserted condition returns true, nothing happens.  
If the asserted condition returns false, `AssertionError` exception is raised.

\[code lang=text\]  
def price\_after\_discount(0ld\_price, discount):  
new\_price = 0ld\_price \* discount  
assert 0 &lt;= new\_price &lt;= old\_price  
\[/code\]

This block of code applies a discount the an item. We assert that the new price is greater than zero, and not more than the old price.

Assert is different from a regular exception in that it's meant for unrecoverable errors. Recoverable errors are things like `File not found`, where you can fix it (by putting the file where it should be) and try to run the program again. Asserts are meant for internal sanity checking.

Don't use Assert for data validation, because it can be optimized away.

\[code lang=text\]  
def delete\_product(prod\_id, user):  
assert user.is\_admin()  
assert store.has\_product(prod\_id) 'Unknown product'  
store.get\_product(prod\_id).delete()  
\[/code\]

When you optimize away asserts, we remove checking if the user is admin, or if the store has the product.

Context Managers
----------------

When you do OO in python and you create classes to use, you can set context managers that dictate what happens when you enter and exit the code.

This is done by defining `__enter__` and `__exit__` functions

\[code lang=text\]  
class ManagedFile:  
def \_\_init\_\_(self, name):  
self.name = name

def \_\_enter\_\_(self):  
self.file = open(self.name, 'w')  
return self.file

def \_\_exit\_\_(self, exc\_type, exc\_val, exc\_tb):  
if self.file:  
self.file.close()

\[/code\]

`__enter__` is called when the execution enters the context of the statement, and `__exit__` is called when it leaves the context.

Underscores and Dunders
-----------------------

On naming the variables in python, each name has a different meaning:

1.  SingleLeadingUnderscore: `_var`

    Purely conventional, this tells the reader that the variable is only meant for use internal to the function.

2.  SingleTrailingUnderscore: `var_`

    Purely conventional, putting an underscore at the back prevents naming conflicts with Python's keywords

3.  DoubleLeadingUnderscore: `__var`

    When double underscores are infront, Python name-mangles the variable, and puts the class name in front of it.

    \[code lang=text\]  
   class Test: def \_\_init\_\_(self):  
   self.foo = 11  
   self.\_bar = 23  
   self.\_\_baz = 42  
   \[/code\]

    When you look at the attributes of object `Test`, we see that `__baz` has become `_Test__baz`

    \[code lang=text\]  
   &gt;&gt;&gt; t = Test()  
   &gt;&gt;&gt; dir(t)  
   \['\_Test\_\_baz', '\_\_class\_\_', '\_\_delattr\_\_' ... \]  
   \[/code\]

    This is done to protect the variable from being overridden in subclasses that extends from the parent class

4.  DoubleLeadingandTrailingUnderscore: `__var__`

    Leading and trailing underscores are left untouched by Python. They are reserved for special usage in Python, such as `__init__` and `__call__`

5.  SingleUnderscore: `_`

    Meant to represent a variable that is temporary and insignificant

    \[code lang=text\]  
   for \_ in range(5):  
   print("Hello World)  
   \[/code\]

    `_` also represents the last value of the Python interpreter session

String Formatting
-----------------

Old method: `"Hello, %s" % name`

New method: `"Hello, {}".format(name)`

The new method is more powerful, because the order in `format` doesn't matter

`'Hey {name}, there is a 0x{errno:x} error!'.format(errno=errno, name=name)`

Python Functions
----------------

Python's functions are first class objects.

What this means is that they can be assigned to variables, stored in data structures, and passed as arguements

\[code lang=text\]  
&gt;&gt;&gt; funcs = \[bark, str.lower, str.capitalize\]  
&gt;&gt;&gt; funcs  
\[&lt;function yell at 0x10ff96510&gt;, &lt;method 'lower' of 'str' objects&gt;, &lt;method 'capitalize' of 'str' objects&gt;\]  
\[/code\]

Lambdas
-------

Lambdas declare small anonymous functions. It's a declarative way of programming

\[code lang=text\]  
&gt;&gt;&gt; add = lambda x, y: x + y  
&gt;&gt;&gt; add(5, 3)  
8  
\[/code\]

The syntax: `lambda x, y` are the inputs. `x + y` is the action to carry out and return.

A more complete example:

\[code lang=text\]  
&gt;&gt;&gt; tuples = \[(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')\]  
&gt;&gt;&gt; sorted(tuples, key=lambda x: x\[1\])  
\[(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')\]  
\[/code\]

The tuple is passed into the lambda function, and it returns the second element, which is assigned to key. The output is then sorted according to the second value.

Decorators
----------

Decorators let you modify the behavior of the callee, without modifying the callee's code itself.

Some common use case for decorators are:

1.  Logging
2.  User authentication

\[code lang=text\]  
def uppercase(func):  
def wrapper():  
original\_result = func()  
modified\_result = original\_result.upper()  
return modified\_result  
return wrapper

@uppercase  
def greet():  
return 'Hello!'

&gt;&gt;&gt; greet()  
'HELLO!'  
\[/code\]

When we put the decorator on `greet()`, we are passing the function to our decorator function.

The output is then gotten from the decorator

Decorators are done bottom to top

\[code lang=text\]  
@strong  
@emphasis  
def greet():  
return 'Hello!  
\[/code\]

`emphasis` is executed first, before `strong`

Decorators can also accept arguments by using `args` and `kwargs`. The arguments are gotten from the original function, and passed to the decorators.

\[code lang=text\]  
def proxy(func):  
def wrapper(\*args, \*\*kwargs):  
return func(\*args, \*\*kwargs)  
return wrapper  
\[/code\]

\*args and \*\*kwargs
---------------------

`*args` and `**kwargs` are optional arguments to a function.

\[code lang=text\]  
def foo(required, \*args, \*\*kwargs):  
print(required)  
if args:  
print(args)  
if kwargs:  
print(kwargs)

&gt;&gt;&gt; foo() TypeError:  
"foo() missing 1 required positional arg: 'required'"

&gt;&gt;&gt; foo('hello')  
hello

&gt;&gt;&gt; foo('hello', 1, 2, 3)  
hello (1, 2, 3)

&gt;&gt;&gt; foo('hello', 1, 2, 3, key1='value', key2=999)  
hello (1, 2, 3) {'key1': 'value', 'key2': 999}  
\[/code\]

`*args` collects extra positional arguments  
`**kwargs` collects extra keywords as a dictionary

Writing your own exception class
--------------------------------

\[code lang=text\]  
class NameTooShortError(ValueError):  
pass

def validate(name):  
if len(name) &lt; 10::  
raise NameTooShortError(name)  
\[/code\]

References, Shallow Copying and Deep Copying
--------------------------------------------

#### References

\[code lang=text\]  
new\_list = original\_list  
new\_dict = original\_dict  
new\_set = original\_set  
\[/code\]

This just creates references, and any modifications done to `original_` will also modify `new_`

\[code lang=text\]  
&gt;&gt;&gt; xs  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]  
&gt;&gt;&gt; ys  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]

&gt;&gt;&gt; xs.append("Hello")

&gt;&gt;&gt; xs  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\], "Hello"\]  
&gt;&gt;&gt; ys  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\], "Hello"\]  
\[/code\]

#### Shallow Copying

\[code lang=text\]  
new\_list = list(original\_list)  
new\_dict = dict(original\_dict)  
new\_set = set(original\_set)  
\[/code\]

This makes a new list, but the children objects in the list are not copied.

\[code lang=text\]  
&gt;&gt;&gt; xs  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]  
&gt;&gt;&gt; ys  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]

&gt;&gt;&gt; xs.append("Hello")

&gt;&gt;&gt; xs  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\], "Hello"\]  
&gt;&gt;&gt; ys  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]

&gt;&gt;&gt; xs\[1\]\[0\] = "X"

&gt;&gt;&gt; xs  
\[\[1, 2, 3\], \['X', 5, 6\], \[7, 8, 9\], "Hello"\]  
&gt;&gt;&gt; ys  
\[\[1, 2, 3\], \['X', 5, 6\], \[7, 8, 9\]\]

\[/code\]

#### Deep Copying

\[code lang=text\]  
new\_list = copy.deepcopy(original\_list)  
new\_dict = copy.deepcopy(original\_dict)  
new\_set = copy.deepcopy(original\_set)  
\[/code\]

This creates an entirely new instance, and copies all the children too.

\[code lang=text\]  
&gt;&gt;&gt; xs  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]  
&gt;&gt;&gt; ys  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]

&gt;&gt;&gt; xs.append("Hello")

&gt;&gt;&gt; xs  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\], "Hello"\]  
&gt;&gt;&gt; ys  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]

&gt;&gt;&gt; xs\[1\]\[0\] = "X"

&gt;&gt;&gt; xs  
\[\[1, 2, 3\], \['X', 5, 6\], \[7, 8, 9\], "Hello"\]  
&gt;&gt;&gt; ys  
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]

\[/code\]

Generators
----------

Generators generate values JIT (Just In Time). This is opposed to making a list, and iterating through it.

\[code lang=text\]  
genexpr = ('Hello' for i in range(3))

&gt;&gt;&gt; next(genexpr)  
'Hello'

&gt;&gt;&gt; next(genexpr)  
'Hello'

&gt;&gt;&gt; next(genexpr)  
'Hello'

&gt;&gt;&gt; next(genexpr)  
StopIteration  
\[/code\]
