Title: SWE Day 7: What is Webpack?
Date: 2020-05-07 10:13
Author: Chan Jin Hao
Category: Software Engineering
Tags: webpack, web development
Slug: webpack
Status: published

Webpack is a program used in web development to optimize how websites are being built. It's another topic for me to rant about just how bloated web development has become, and hence the development of Webpack.

## Modules and Bundles 

Modules are groups of code, such as CSS, Javascript or images that can be packaged together. Webpack breaks your code down into these separate modules based on how it is used in the application.

These Modules can form a dependency graph, and Webpack creates Bundles from this group of dependency Modules. Bundles are a collection of Modules that has been complied and optimized for execution.

## Building a Bundle

The key to building a Bundle of dependent Modules is the Entry Point. Webpack starts at the entry point of the application, and builds a dependency graph by analyzing what files it imports, and files the imports import. It then takes all these files that are dependent on each other, and compiles them into a Bundle.

A web application may have multiple Entry Points, which may be the case of a multi-page application. For example, you may have a user, admin, and developer homepage, each showing different items. You therefore need to define these 3 entry points, so that Webpack is able to traverse through them and build their own dependency graph, and their Bundles.

## Motivation for Webpack

Because web development has become so bloated, and most applications now lean towards a concept of single-page-applications, the underlying JavaScript code can get very huge.

Therefore, instead of pulling the entire JavaScript code at once to the client end, Webpack cuts up the code into the different Modules, and forms bundles based on depended Modules. On the client end, the imports are therefore smaller, because you are only pulling and executing the Bundles you need, and not the entire codebase.

Also, by pre-grouping the Modules dependencies into Bundles before hand, it speeds things up at the client end, as the client does not have to wait for all the dependencies to trickle down one by one. With Webpack, all the dependencies are compiled into a single file, and so only a single file needs to be downloaded.

## Resources

[Original Webpack documentation explains everything pretty clearly](https://webpack.js.org/concepts/)
