Title: SWE Day 3: JVM
Date: 2020-05-03 16:32
Author: Chan Jin Hao
Category: Software Engineering
Tags: jvm
Slug: jvm
Status: published

When you run any Java applications, they are first translated into Java byte codes, before being run on a JVM, or Java Virtual Machines.

A JVM is a program that executes Java Byte Code, and the JVM program can be run on any platform, be it Unix, Windows or Mac. With this setup, Java programs are able to run on any platform, as long as there is a JVM program installed on it.

And not just Java programs, but any program that can be compiled into Java byte codes can be run on the JVM. For example, the programming language Clojure is transformed into Java byte codes and executed on the JVM.

## JVM as an Environment
---

The JVM provides an environment for other programs to run on it. The JVM as an environment has its own memory mangement, and garbage collect, all distinct from the underlying host OS.


## Types of JVM
---

Not all JVMs are created the same, and there are different implementations of JVMs, just like there are different Operating Systems available.

The most common JVM is implemented from OpenJDK, HotSpot JVM. OpenJDK is usually gotten together when you install a Java Runtime Environment (JRE)

Most licensed JVMs are forks from the HotSpot JVM, including the liscensed version of Oracles JVM.

## Running Java Bytecodes in the JVM
---

The JVM has an instruction set, just like an Assembly Language. The Java bytecode is a very low level instruction set, and many higher level languages are compiled down to it first before running in the JVM.

There are two strategies to executing the Java bytecode:
1. Interpretation
2. Just In Time (JIT) compilation

Intepretation takes each Java bytecode one by one, and converts it to the corresponding instruction set on the host OS. This has a quick startup time, but slow processing time.

JIT compilation translates a whole chunk of bytecode at once into the instruction set. This has a slow startup time (to complie the bytecodes), but a quick processing time.

The strategy is thus a combination of both, where the interpretor runs first, while the JIT runs in the background compiling the code. Once the JIT finishes compiling, the JVM the switches from the interpreter to the compiled code.

## Resource

[General Introduction to JVM](https://www.javaworld.com/article/3272244/what-is-the-jvm-introducing-the-java-virtual-machine.html)

[How Java bytecode is executed](https://www.quora.com/How-is-Java-bytecode-executed)
