Title: SWE Day 2: Map Reduce
Date: 2020-05-02 12:33
Author: Chan Jin Hao
Category: Software Engineering
Tags: mapreduce
Slug: mapreduce
Status: published

In day 2 of  our SWE learning journey, we're going to be looking at map reduce. Most topics will be chosen in conceptual proximity, and in this case, we're revolving around big data technologies.

## Before MapReduce

Before MapReduce, a typical way of parallel and distrubuted way was to split the data into equal chunks, and place them on different machines. Each machine will then do their computation, before sending their results back to a central server to do the collation, and final calculation. For example, to find the maximum value in a huge list, the list is split into various chunks and sent to different servers. Each server will then calculate their own local maximum value, before sending the result back to the central server, which will calculate the maximum of all the servers.

There are some challenges that such a layout faces

1. Critical Path Problem - the length of the entire job is dependent on the slowest worker
2. Reliability Problem - If any machine fails, the whole operation fails
3. Equal Split Problem - How do we ensure each machine gets an equal load, not just in size, but in processing power required
4. Fault Tolerance Problem - Stemming from problem 2, what are mechanism catch the problem, and restart the operation
5. Aggregation Problem - Each machine should have an aggregator to collate their local results before sending them to the central machine

There are 2 phases in this operation, first to split, then to operate

## MapReduce

In MapReduce, the splitting is done in the Map stage, and the operations are done in the Reduce stage

In the Map Stage, the data is split into key-value pairs as intermediate outputs

The key-value pair is then sent to the Reducer. A Reducer can recieve key-value pairs from multiple Mappers

Before the Reduction stage, there is a Shuffling and Sorting stage, where all the same keys from the key-value pairs are lumped together. A single Reducer will get all the values that belong to a single unique key.

At the Reduce stage, it will get a key, and all the related values (lumped together by the Shuffling stage). It then performs the relevant operations on these set of values. All the key-value(s) pair results are the output.


## Reducing

What happens when your Mapping stage produces more unique keys than Reducers? Well, each Reducer does not exactly recieve only 1 unique key to process, but there is a function called a HashPartitioner, which decides which key goes to which Reducer. The HashPartitioner works similar to a Hash Table, where we hash a value, and place them into buckets. If there are collisions, the value is appended to the currently existing item.

In the case of a HashPartitioner, when it hashes the keys and there is a collision, they key-value pair is placed in the same Reducer (bucket).

This only happens when the number of unique keys > Reducers. If the number of unique keys are <= Reducers, each Reducer will only get at most 1 key to process.

## In Summary

This was a pretty simple concept (I hope I got it right). In essence, we map the job to various k-v pairs, group then by keys, and place them in Reducers to aggregate them.

## Resource

[MapReduce write up, with an example of a word count](https://www.edureka.co/blog/mapreduce-tutorial/)
