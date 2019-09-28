Title: Core Design Principles
Date: 2018-07-12 09:08
Author: jinhaochan
Category: Uncategorized
Slug: core-design-principles
Status: published

[Core Design Principles for Software Developers by Venkat Subramaniam](https://www.youtube.com/watch?v=llGgO74uXMI)

Devoxx is a conference directed towards the Java, Android and HTML5 community.

Some points that are language agnostic, and can be applied universally are summarized below:

1.  **Good code can be changed without much hassle.**
2.  It is always impossible to get it right the first time.
3.  Be unemotional in coding.
4.  People who are dangerous to work with (So you shouldn't become them): People who can't follow instructions, and people who only follow instructions.
5.  **Take time to review code. (You can learn, and you can improve the design)**
6.  Simplicity is hard. Strive to achieve that.
7.  Simple keeps you focused (Imperative vs Declarative)
8.  Write code to solve real problems. (Don't code without knowing what it should do)
9.  Complexity (Inherent vs Accidental). Inherent Complexity comes from the problem. Accidental Complexity comes from the solution.
10. Simple != Familiar (just because you know what it does, doesn't mean its simple)
11. **Good Design is one that hides Inherent complexity, and eliminates Accidental Complexity**
12. **YAGNIy (You Aren't Going To Need It (yet)) Don't implement things that you don't need yet. Do the important things first.**
13. Cost of implementing now &gt; Cost of implementing later = Postpone
14. Cost of implementing now = Cost of implementing later = Postpone
15. Cost of implementing now &lt; Cost of implementing later = Do it now
16. **Have a Good Automated Testing. This prevents fear of postponing**
17. Cohesion is a code that does one thing and one thing only. This makes it easier for change.
18. Similar code stays together. Dissimilar code stays away
19. Coupling is what you depend on. Try to see if you can remove coupling. (You can't remove all dependencies, so make them loose)
20. Knock out before you Mock out
21. **Good Design has High Cohesion and Low Coupling**
22. DRY (Don't repeat yourself) (Don't duplicate code, and effort)
23. Every piece of knowledge in a system should have a single unambiguous authoritative representation
24. CPD (Copy Paste Detector to find duplicated code)
25. Don't write overly long functions and methods
26. How long is a long method? SLAP (Single Level of Abstraction Principle)
27. **SLAP: What was the level of abstraction of your function**
28. **Don't comment what, comment why**
29. Open Closed Principle: A software module should be open for extension, but close for modification
30. Use DRY and YAGNI often

