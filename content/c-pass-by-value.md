Title: C# Pass By Value
Date: 2018-11-25 22:37
Author: Chan Jin Hao
Category: Software Engineering
Slug: c-pass-by-value
Status: published

Pass by Value vs Reference
--------------------------

### Pass by value

------------------------------------------------------------------------

When we pass call a function, we sometimes pass in some values for the function to use. Typically, it would look like this

`(parameters)`

or

`void swapValues(int x, int y)`

When we pass a value to the function `swapValue()`, we are passing it by value.

What this means is that, a new memory region is allocated from the stack for the new parameters `x` and `y`, and the value of that memory region is set to the value that was passed to it.

I'll write a post on what happens in the memory region when a function is called in the future (dealing with functions stack frame allocation etc). But for now, when we call a function, it is allocated a function stack frame, with all its variables and paramters contained within the frame.

Let's look at the following code block

\[code lang=text\]  
public static void Main()  
{  
int x = 10;  
int y = 20;

swapValues(10, 20);  
}

void swapValues(int x, int y)  
{  
int temp;

temp = x;  
x = y;  
y = temp;  
}  
\[/code\]

When `Main()` calls `swapValues()`, a new stack frame is allocated just for `swapValues()` to store all its local variables, and parameters passed into it. The stack frame will be the new memory region for the two paramters `x` and `y`, and assigns them to the values that was passed to them, which are `10` and `20`.

Because it's a new memory region, whatever changes that are done in the function `swapValues()` will only affect the newly allocated memory regions of `x` and `y` in the stack frame of `swapValues()`.

That is to say, the values of `x` and `y` in the `Main` function stack frame will be left untouched!

This kind of defeats the purpose of the function...

So how do we fix it?

### Pass by Reference

------------------------------------------------------------------------

Let's tweak the code above slightly to make it pass by reference

\[code lang=text\]  
public static void Main()  
{  
int x = 10;  
int y = 20;

swapValues(10, 20);  
}

void swapValues(ref int x, ref int y)  
{  
int temp;

temp = x;  
x = y;  
y = temp;  
}  
\[/code\]

The only difference is adding the keyword `ref` in front of the function parameters, which tell the function to reference to the objects passed in. This means that whatever work that is done in `swapValues()` will work directly on the values in `Main()`

The difference between passing by value and passing by reference is shown below

-   Passing by value: Allocates memory space on the stack frame and assigns it the value of the object that were passed into the function
    
-   Passing by reference: Does not allocate memory space on the stack frame, uses the object that was passed in directly

In this case, whatever changes done to `x` and `y` in the function `swapValues()` will directly modify the values inside the stack frame of `Main()`!

### Reference Objects

------------------------------------------------------------------------

### Modifying the reference object part 1

Now heres the tricky part. Some objects are reference objects, which is to say they are pointers to begin with. An example would be a string in C, or an array object.

\[code lang=text\]  
public static void Main()  
{  
int\[\] myArrayMain = new int\[\] {1, 2, 3, 4, 5};

editArray(myArrayMain);  
}

void editArray(int\[\] myArrayParam)  
{  
myArrayParam\[0\] = 7;  
}  
\[/code\]

The above code will changes `myArrayMain` to `{0, 2, 3, 4, 5}`

When we call the function `editArray()`, we create a new stack frame for `editArray()` to hold its local variables and paramters. Because `myArrayParam` is a reference object, we create a pointer on the stack frame to hold any value that is passed into `myArrayParam`.

We are passing in `myArrayMain`, which is a reference object. That means, the value of `myArrayMain` is an address, which points to the first element in the array.

When we pass `myArrayMain` to `myArrayParam`, we are assigning `myArrayParam` to the value of the `myArrayMain`, which is an address that points to the first element of `myArrayMain`!

Memory pointer layout:

`myArrayParam` --&gt; `myArrayMain` --&gt; `memory of first element in myArrayMain (1)`

So any changes made to `myArrayParam` in `editArray()` will be propagated to the `myArrayMain`

### Modifying the reference object part 2

Now what happens when we change `editArray()` to create a new array? Will `myArrayMain` be overwritten?

\[code lang=text\]  
public static void Main()  
{  
int\[\] myArrayMain = new int\[\] {1, 2, 3, 4, 5};

editArray(myArrayMain);  
}

void editArray(int\[\] myArrayParam)  
{  
myArrayParam\[0\] = new int\[\] {6, 7, 8, 9, 10};  
}  
\[/code\]

Nope. `myArrayMain` will still remain as `{1, 2, 3, 4, 5}`

When we call `myArrayParam[0] = new int[] {6, 7, 8, 9, 10};`, we are repointing `myArrayParam` to something else. This breaks the memory pointer layout above

\[code lang=text\]  
myArrayParam --&gt; myArrayMain --&gt; memory of first element in myArrayMain (1)

becomes

myArrayParam --&gt; memory of first element in myArrayParam (6)

myArrayMain --&gt; memory of first element in myArrayMain (1)  
\[/code\]

### Modifying the reference object part 3

Lets look at the final attempt. This time, we call `ref` on the array that is passed in

\[code lang=text\]  
public static void Main()  
{  
int\[\] myArrayMain = new int\[\] {1, 2, 3, 4, 5};

editArray(myArrayMain);  
}

void editArray(ref int\[\] myArrayParam)  
{  
myArrayParam\[0\] = new int\[\] {6, 7, 8, 9, 10};  
}  
\[/code\]

Remember that when we call `ref`, in the stack frame of `editArray()`, no new memory is allocted, and the original `myArrayMain` is used.

The memory pointer layout is now

\[code lang=text\]  
myArrayParam --&gt; memory of first element in myArrayMain (1)

myArrayMain --&gt; memory of first element in myArrayMain (1)  
\[/code\]

Both `myArrayParam` and `myArrayMain` now point to the first element in `myArrayMain`

So when the code block is ran, `myArrayMain` will change to `{6, 7, 8, 9, 10}`!

### Conclusion

------------------------------------------------------------------------

Phew! That was a long and confusing read, so here's a TLDR:

-   C\# passes by value
-   When a function is called, a stack frame is allocated for local and parameter variables
-   The parameter variables are assigned to the value that was passed in
-   No memory in the stack frame is allocated for parameters that are prefixed with `ref`, but are accessed directly from the caller function
-   Arrays are reference objects
-   The values they hold are the memory space of the first element in the array

Thanks for reading!!

Further reading: http://www.yoda.arachsys.com/csharp/parameters.html Excellent page!!!
