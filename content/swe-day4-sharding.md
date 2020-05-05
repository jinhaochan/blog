Title: SWE Day 4: Sharding
Date: 2020-05-03 18:11
Author: Chan Jin Hao
Category: Software Engineering
Tags: sharding
Slug: sharding
Status: published

Today we're going to be looking at one database optimization technique called Sharding. Before we talk about partitioning, it has to be said that the table first has to have some sort of ordering, so search can be optimized with that key.

Sharding involves splitting the table into partitions, which can be done in two ways: Horizontally and Vertically.

In a horizontal partition, you split table into chunks of different rows. It's like dividing a table equally into different partitions, which each parition carry different parts of data. The number of columns are still the same.

Vertical partitioning is a little bit weird, because instead of splitting row-wise, we split the table column-wise. This method of partitioning is not very common, and requires deep knowledge of the problem and common queries (eg, most queries only hit these subset of columns)

## Benefits of Sharding

Because the original table is split up into multiple logical shardss, we can place these logical shards into different physical database nodes or servers. When we do that, it becomes a physical shard.

As we can physically place differenet logical shards across multiple hardwares, we faciliate Horizontal Scaling, which is the strategy of adding in more physical machines, as opposed to Vertical Scaling, which is adding more compute power to the current machines.

Search time for data thus also falls (if properly indexed), as the number of rows in each physical shard is smaller. You thus have to search lesser rows for the desired data.

Sharding also provides some form of redundancy across different physical locations.

## Drawbacks of Sharding

Sharding can be potentially distruptive to development efforts, as instead of accessing a single table, you now have multiple tables to access, and you have to be careful which one you choose from.

There is also a potential of data corruption during the sharding process.

Imbalanced Shards is also a problem, where one shard contains way too much data compared to other shards. For example, in a database of names, a shard containing keys A-E may be way more populated than the shards containing keys X-Z, as those alphabets appear more often. When this happens, the shard A-E is called a database hotspot.

It is also difficult to revert back to it's original unsharded form, and not all databases support sharding.

## Sharding Architectures

Key based Sharding: Partitioning based on groups of keys

Range based Sharding: Partitioning based on a range of values

Directory based Sharding: In geolocation data, we can group by location proximity

## Considerations for Sharding

It's beneficial to shard if:
1. The amount of data exceed the storage capacity of a single database node
2. The r/w times of the database is too long based on the amount of data
3. Network bandwidth issues if serviced only by a single database node

The problems above seems to be solvable by vertical solutions. Add more ram, add more hard disks, add more bandwidth, and most of the time, it is. Sharding isn't something that should be commonly done.


## Resource

[Digital Ocean explanation](https://www.digitalocean.com/community/tutorials/understanding-database-sharding)
