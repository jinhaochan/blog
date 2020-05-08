Title: SWE Day 6: What happens when you run Python?
Date: 2020-05-06 11:41
Author: Chan Jin Hao
Category: Software Engineering
Tags: python
Slug: python
Status: published


This post is not about how to code in Python, differences between Python 2 or 3, or its stylistic guidelines (PEP8). Rather, it's about what happens in the background when you execute Python code.

When you write you code in Python, it ends with a suffix `.py`, and after you execute it with some command, for example `python3 count.py`, you will see that athere is a folder generated called `__pycache__`. Inside this cache folder, there will be files named after the file you ran, but now it's suffix is `pyc`, or `count.pyc`.

## `.pyc` and the Virtual Machine

When you execute a Python file, the Python interpreter, which is written in C, reads the file's content, parses it to ensure syntax correctness, and compiles down to Python bytecode, which is stored inside the `.pyc` file.

The Python bytecode is then executed in the Python Virtual Machine. Sounds familiar? This sounds like compiling Java program down to Java bytecode, before executing it on the Java Virtual Machine (JVM).

The Python Virtual Machine is also written in C, and it takes in the bytecodes for execution. Although, the bytecode can be read in by other programs, as we will discuss below.

The presence of the `.pyc` files also mean that you can change the code of the orignal Python file while it is running, and the flow execution will not be affected. This is because the original program has already been compiled, and it is the bytecodes that are running, not the original program file itself.


## Python is an Interpreted Language!

But based on what you read above, Python is compiled to bytecode first before being executed on the Python Virtual Machine! So what's what?

Interpreted language is when the translation from code to machine code happens in real time, as the program is being run. Compiled language is when the translation happens before hand, and the entire program is translated to machine code before execution.

In fact, Python is actually compiled first to Python bytecode, and its how the bytecode is being executed by different programs that can either be interpreted, or compiled. The official CPython interprets the bytecode, while others like PyPy does JIT compilation, and IronPython compiles the bytecode into other bytecodes.

