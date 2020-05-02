Title: SWE Day 1: Under the hood of Kafka
Date: 2020-05-01 11:12
Author: Chan Jin Hao
Category: Software Engineering
Tags: kafka
Slug: kafka
Status: published

Since we're facing a lockdown (or circuit breaker, as how we define it) that is being extended all the way till end of May, I thought it would be good to use this time to really dive into various Software Engineering topics each day.

Everyday, from 1st May to 31st May, I would read up on a topic that is entirely new to me, and try to take a deep dive to how it works, and really exercise my brain to try to understand the concepts. I think deep reading and understanding is a good way to prime the brain to be more absorbant, and to keep going down the rabbit hole.

For the most parts, I will not be writing long articles, but rather a summary of what I have learnt, and links to all the resources. Reason being, since most of my learning is obtained from other articles, I find it unneccesary to rewrite it again, and also to give credit where its due. 

On the first day, I'm going to look at Kafka, since it's something that I have touched on at my work place recently.


## What is Kafka

---

Before going into Kafka, lets do a brief overview of what it is, and what it's most commonly used for.

Kafka is a messaging system, where it takes it large amount of data from various sources (Producers), and allows various services to read the data off it (Consumers). Central to the architecture is something called a Kafka Broker, which handles the messages coming in and out (just like a broker does).

Kafka was created by former LinkedIn data engineers, and the whole reason for that was to facilitate quick and scalable passing of messages.


## Under The Hoods of Kafka

---

As mentioned above, the central piece is something called a Kafka broker, and within the broker are 2 more important components:

1. Topics
2. Partitions

How these gel together are: Kafka has a set of Topics, which are distinct logical grouping of messages. One topic could contain messages pertaining to the weather, while the other topics could have messags about the traffic.

Each Topic is then partitioned into... Partitions. This allows parallel access to the various messages in a Topic. To track where the reading of the Partitions have happened until, the Partitions are further broken down into Segments. Each Segment stores a certain amount of messages, before a new Segment is formed.

A single Kafka cluster can have multiple brokers for redundancy. Each Parition is replicated across the various brokers. There is then a concept of a Partition leader and followers, where one of the replicas handle the read/write requests (thereby changing the index and data appended), while the rest of the replicas copy the changes made to the leader.


### Partition Reading and Zero Copy

Tracking of the read data is handled by the consumer. The consumer is responsible for tracking the offset position of the log, which is where it was last read until. After reading the messages, the consumer has a choice of how to move the offset, be it linearly downwards, or resetting to the top to reread all the messages.

These Partitions are read only, and append only. And because we have an index keeping track of where the last message was read, message retrival is exactly O(1). Another reason for Kafka's speed of data transfer is due its adoption of Zero-Copy, which is a kernel level transferof data, instead of going through the User Land, and Kernel Space. [Zero-Copy](https://cloudnweb.dev/2019/05/heres-what-makes-apache-kafka-so-fast-kafka-series-part-3/)


### Partition Writing

Within each topic, writing to a partition is done in a round robin manner. And as mentioned, writing to a partition is append only. This means that a producer wanting to write also operates at O(1)

The producer can also specify which partition to write to by attaching a key to the message. All records with the same key will go to the same partition.

Before a producer write to Kafka, it has to request for metadata, which tells it who is the leader to write to. One common error is setting the key to null or the same, and all the messages end up in the same partition, which defeats scalability.


### Consumers and Consumer Groups

Low-Level Consumer is a single consumer, while a High-Level Consumer is a group of consumers, called a Consumer Group.

The broker dictates which consumer should read from which partition. 1 partition can only be read by 1 consumer, while 1 consumer can read from many partitions (Many-to-One). Because of this, when your number of consumers = number of partitions, optimization makes it One-to-One relationship. Adding more consumers are useless, as each partition is already occupied by a single consumer.

Messages are never pushed down to the consumers, but are always pulled.


### Resource

[cloudkarafka. Amazing write up](https://www.cloudkarafka.com/blog/2016-11-30-part1-kafka-for-beginners-what-is-apache-kafka.html)
