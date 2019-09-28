Title: Printing Subsets in a List
Date: 2018-07-10 09:52
Author: jinhaochan
Category: Uncategorized
Tags: codexercise
Slug: the-journey-begins
Status: published

**<u> Problem Statement </u>**

Given a list of distinct items (or a set), print out all of its subset lists.

Input:

` [1, 2, 3, 4] `

Output:

`:empty set: 1 1,2 1,3 1,4 1,2,3 1,2,4 1,3,4 1,2,3,4 2 2,3 2,4 2,3,4 3 3,4 4`

**<u> Proposed Solution </u>**

For each given list, I would need to figure out how many set of subsets there are. In this case, the total number of subsets for a given list is `2^n`, where `n` is the total number of items in the list.

The reason it is `2^n` is because: For each item in the list, you have 2 possible choices to take; Append an item to it, or don't. And since you have `n` items, you have a total of `2^n` choices.

After figuring out how many total subsets there are, that can be the terminating condition in a recursive solution, something like


    if len(answer) == int(math.pow(2,len(myList))):
            return answer

In each step of the code, we need to clone the list into two to model them as the two potential choices; adding an item, or not adding an item. We add an item to each element in one list (adding an item), and preserve the original list (not adding an item), and join the two results together

Example:

`Given List = [1, 2]`

Step 1: Add 1

Initial set = {} (models choice of adding)  
Cloned set = {} (models choice of not adding)

Resulting set that adds: {1}  
Resulting set that does not add: {}

Result = {},{1}

Step 2: Add 2

Initial set = {},{1} (models choice of adding)  
Cloned set = {},{1} (models choice of not adding)

Resulting set that adds: {2}, {1,2}  
Resulting set that does not add: {}, {1}

Result = {}, {1}, {2}, {1,2}</code>

We can see that taking the union of sets that add, and sets that do not add will give us the total subsets. The above is the pseudocode for the main body of code for our solution. Given that we have an idea of what the terminating condition will be like, we can model this as a recursive solution.

In each recursion, we should

1\. Check if total number of items in the set is = `2^(length of list)`  
2. Clone the given set  
3. Add the item to one of the set  
4. Take the union of the original set and the modified set  
5. Go back to step 1

Translated to python3,


    def printPattern(givenList, result, totalSubsets):
            if len(result) == totalSubsets:
                    return result

            # models not adding
            clonedResult = copy.deepcopy(result)

            itemToAdd = givenList[0]

            # omititng the item we just added in the next recursion
            newList = givenList[1:]

            # adding an item to each item in the list
            for item in result:
                    item.append(itemToAdd)

            # taking the union of both the results
            result += clonedResult

            return printPattern(newList, result, totalSubsets)

Read here to understand why I used deepcopy: [How to clone or copy a list?](https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list)

That's it!
