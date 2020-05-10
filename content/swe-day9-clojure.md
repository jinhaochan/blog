Title: SWE Day 9: A Start to Clojure (Get it?)
Date: 2020-05-09 17:18
Author: Chan Jin Hao
Category: Software Engineering
Tags: clojure
Slug: clojure
Status: published


Today we're going to be starting on the Clojure tutorials as detailed [here](https://www.braveclojure.com/introduction/). Everyday, I will be covering some chapters, and instead of copying whatever they taught there to this blog, I will only be taking the summaries or nuggets of information, as well as my own inputs to there lessons. 

Let's Begin!

## Starting a Clojure Project

To start a Clojure project, we use a program called [Leiningen](https://github.com/technomancy/leiningen). Leiningen itself is written in Clojure, and is used as a way to build automation and dependency management for your Clojure projects.

After installing Leiningen, starting a Clojure project can done running

`lein new app my_project`

Running a the project can be done by running 

`lein run`

And exporting the project to a portable Jar file can be done with 

`lein uberjar`

To make the generated Jar file executable, run

`java -jar target/uberjar/clojure-noob-0.1.0-SNAPSHOT-standalone.jar`

## Starting a REPL terminal

To start a REPL terminal, you call 

`lein repl`

When you run commands, the Clojure compiler compiles the code to Java bytecode, which is then JIT-compiled to the native code.

## Clojure with Emacs

Emacs is the chosen editor of choice for Clojure projects, as opposed to others like vim.

Instead of doing an intro to Emacs, here are some useful shortcuts you will be using often.

`ctrl.x b` creates a new buffer, or switches around buffers

`ctrl.x k` kills a buffer

`ctrl.x.f` opens a new file

`ctrl.x.s` saves the edits

`ctrl.k` kills (deletes the entire line)

`ctrl.-./` undo

`alt.space` selects a region for editing

`alt.x` opens up available modules for calling

`ctrl.x o` switches between panes of emacs

`ctrl.x 1` deletes all but the selected pane

`ctrl.x 2` splits horizontally

`ctrl.x 3` splits vertically

`ctrl.x 0` deletes the selected pane

## Next Lesson

In the next lesson tomorrow, we'll be looking more into the coding of Clojure itself, including the Syntax and Control Flows
