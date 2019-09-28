Title: Async and Await in C#
Date: 2018-12-09 22:40
Author: jinhaochan
Category: C#
Tags: Async, Await
Slug: async-and-await-in-c
Status: published

Async and Await in C
--------------------

`async` and `await` are used when we are doing asynchronous programming. Why we would want to do asynchronous programming, is due to performance issues. When we have two unrelated tasks that are in the program, and one task takes a long time to process, it should not be holding up the other task.

We use Asynchronous programming to hand over program controls to ensure that no one process is holding up the entire program.

`async` and `await` are used together to make a program asynchronous.

Below is a simple example to make a program asynchronous

\[code lang=text\]  
static void Main(string\[\] args)  
{  
DoSomething();  
Console.WriteLine("Control to Main!");  
Console.ReadLine();  
}

public static async void DoSomething()  
{  
await Delay();  
Console.WriteLine("Control back to Method!");  
}

async static Task Delay()  
{  
await Task.Delay(5000);  
}  
\[/code\]

The output on the console:

\[code lang=text\]  
Control to Main!  
&lt;after a 5 second delay&gt;  
Control back to Method!  
\[/code\]

You first have to declare the method asynchronous with `async`

`async static Task Delay()`

Next, we put the keyword `await` beside the command that will take a long time.

What `await` does is this  
- It awaits for the command to be completed  
- While it is awaiting, it passes control back up to the caller  
- After the command is completed, the control is passed back to the callee

If we look at the code, the program first calls `DoSomething()`, which calls `await Delay()`, which then executes `await Task.Delay(5000);`

When `await Task.Delay(5000);` is executed, `Delay()` passes control back up to the caller, which is `DoSomething()`

Because `DoSomething()` is awaiting `Delay()`, it passes control back up again to `Main()`, which then executes `Console.WriteLine("Control to Main!");`

After `await Task.Delay(5000);` is completed, it returns to `DoSomething()`, which executes `Console.WriteLine("Control back to Method!");`, and finally returns to `Main()`

Another example is given below

\[code lang=text\]  
async Task&lt;int&gt; AccessTheWebAsync()  
{  
HttpClient client = new HttpClient();

Task&lt;string&gt; getStringTask = client.GetStringAsync("http://msdn.microsoft.com");

// You can do work here that doesn't rely on the string from GetStringAsync.  
DoIndependentWork();

string urlContents = await getStringTask;  
//The thing is that this returns an int to a method that has a return type of Task&lt;int&gt;  
return urlContents.Length;  
}  
\[/code\]

Here, `Task getStringTask = client.GetStringAsync("http://msdn.microsoft.com");` is called, followed by `DoIndependentWork();`.

We next call `string urlContents = await getStringTask;`, which awaits on `getStringTask`. There are two possible scenerios here

1.  After `DoIndependentWork()` is completed, `Task getStringTask = client.GetStringAsync("http://msdn.microsoft.com");` is completed as well, and `getStringTask` is fully initialized. In this case, there is no control being passed back to the caller of `AccessTheWebAsync()`, and the program just runs through.
2.  After `DoIndependentWork()` is completed, `Task getStringTask = client.GetStringAsync("http://msdn.microsoft.com");` NOT completed, and `getStringTask` is NOT initialized. In this case, there control is passed back to the caller of `AccessTheWebAsync()` for execution. Only after `getStringTask` has been initialized, will the program pass back control to `AccessTheWebAsync()`

And for obvious reasons, `async` cannot be a modifier on the `Main` method, because it is the root caller.
