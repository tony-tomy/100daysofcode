# Spark Streaming

'''
Spark Streaming is a microbatch-based streaming library.

Spark and Spark Streaming, with its sophisticated design, unique and unified programming model and processing capabilities have enabled 
us to build complex pipelines that encompass streaming, batch, or even machine learning capabilities with ease

Also, we are free from the hurdle of dealing with multiple frameworks, each meant for its own specific purpose,such as Storm for 
real-time actions, Hadoop MapReduce for batch processing, etc

Stage 1 : Reads streaming data.

Stage 2 : Processes the streaming data.

Stage 3 : Writes the processed data to an HBase Table.

Stage 4 : Provides a visualization of the data.

The live input data streams received by Spark Streaming are divided into several micro batches. Spark Engine take up these batches and 
process it to generate the final streams of results in batches

Streaming Abstraction

The high-level abstraction that Spark Streaming provides is called Discretized stream or DStream.

DStream represents a continuous stream of data.

DStreams can be created in two different ways:

From input data streams from sources such as Kafka, Flume etc.
By applying high-level operations on other DStreams.

Operations that can be applied on DStreams are similar to those of RDD operations.

Transformations : Yield a new DStream.
Output operations : Write data to an external system,

Transformations on DStreams

map(func) : Returns a new DStream by passing each element of the source DStream through a function func.

flatMap(func) : Each input item can be mapped to 0 or more output elements.

filter(func) : Return a new DStream by selecting only those records of the source DStream which returns a true value for the func.

Output Operations on DStreams

print() : Prints the first ten elements of every batch of data in a DStream.

saveAsTextFiles(prefix, [suffix]) : Save this DStream's contents as text files.

saveAsObjectFiles(prefix, [suffix]) : Save this DStream's contents as SequenceFiles of serialized Java objects.

DStreams - Classification

Spark Streaming has two categories of sources.

- Basic sources : Sources that are directly available in the StreamingContext API. e.g., File systems, Socket connections, and 
Akka actors.

- Advanced sources : Sources like Kafka, Flume, Twitter, etc. These are available through extra utility classes.

Shared Variables

Spark provides two different types of shared variables to two known usage patterns.

Accumulators
Broadcast variables

Accumulators

They are simply variables which can be added to the application through associated or commutative operations.

Used to implement counters or sums.

Supports numeric types, but programmers are free to add support for other types as well.

If there is a named accumulator, it can be seen in the Spark UI, which in-turn help us understand the progress of our application workflow.

Creating Accumulators
Accumulators are created from SparkContext(sc) as: val acc = sc.accumulator(0, "test") You can create built-in accumulators for longs, 
doubles, or collections. You are free to create accumulators with or without a name, but only named accumulators are displayed in Spark UI

Accumulators for Executors & Driver
For an Exector/worker node,accumulators are write-only variables. Task running on the executor nodes can manipulate the value set to 
an accumulator. However, they cannot read it's value.

e.g.,
scala>sc.parallelize(Array(1, 2)).foreach(x => acc += x)
The driver, can read the value of the accumulator, using the value method as:
scala> acc.value
res4: Int = 3

Broadcast Variables
These are a kind of shared variables, that allow developers to keep a read-only variable cached on separate nodes rather than 
shipping a copy of it to each node.

Spark distribute broadcast variables using various broadcast algorithms which will largely reduce the network I/O.

Creating Broadcast Variables
Broadcast variables are created with SparkContext.broadcast function as:

scala>val broadVar = sc.broadcast(Array(1, 2))
Note : Explicitly create broadcast variables only if tasks across multiple stages are in need of same data.

value function is used to get the value assigned to a broadcast variable.

scala> broadcastVar.value
res2: Array[Int] = Array(1, 2)

Streaming Application Data Flow

Streaming workflow starts with the Spark Streaming Context, represented by ssc.start()

Workflow Stages

Stage 1 : When the Spark Streaming Context starts, the driver will execute task on the executors/worker nodes.

Stage 2 : Data Streams generated at the streaming sources will be received by the Receivers that sit on top of executor nodes. The receiver is responsible for dividing the stream into blocks and for keeping them in memory.

Stage 3 : In order to avoid data loss, these blocks are also replicated to another executor.

Stage 4 : Block Management Master on the driver keeps track of the block ID information.

Stage 5 : For every batch interval configured in Spark Streaming Context (commonly in seconds), the driver will launch tasks to process the blocks.

After the processing, the resultant data blocks are persisted to any number of target data stores including cloud storage , relational data stores , and NoSQL stores."

Caching / Persistence

DStreams can be persisted in as stream’s of data.

You can make use of the persist() method on a DStream which persist every RDD of that particular DStream in memory.

This is useful if the data in the DStream is computed multiple times.

Default persistence level for input streams is set to replicate the data to two nodes for fault-tolerance.

Creating StreamingContext
The first step in creating a streaming application is to create a StreamingContext.

This is the primary entry point for all streaming functionality.

//creating configuration object
val conf = new sparkConf().setMaster(""local"").setAppName(""MyStreamingApp"")

//creating streaming context and batch interval is set to 1 second
val ssc = new StreamingContext(conf, Seconds(1))
Required imports:

import org.apache.spark._
import org.apache.spark.streaming._

Creating DStreams
You can create a DStream that represents streaming data by using the StreamingContext - ssc.

val lines = ssc.socketTextStream(""samplehost"", 007)
lines DStream represents a stream of data that you will receive from the data server. Each record in lines corresponds to a line of text.

You can now transform the data as per requirements.

Let's perform a word count program.

// splitting the line at <space>
val words = lines.flatMap(_.split(" "))

// creating (<word>,1) as a pair
val pairs = words.map(word => (word, 1))

//summing up all values(1's) for a particular word
val wordCounts = pairs.reduceByKey(_ + _)

//printing the result
wordCounts.print()

Most Important Step!!!
Streaming is not yet started!

All the above computations are performed only at the start of StreamingContext(ssc)

// Start computation   
ssc.start()     

// Wait for computation to terminate 
ssc.awaitTermination()

Spark Streaming with Kafka

Apache Kafka : An open source distributed publish - subscriber messaging system which manages and maintains real time data stream from different systems.

Kafka Components

Broker : Servers that manages and mediates the conversations between two systems. Responsible for delivery of message to right party.

Messages : Simplebyte arrays and any objects can be stored in any format by developers. String, Json, Avro etc.

Topics : Messages are maintained in topics. Msgs are stored, published and organised in kafka topics.

Clusters : A sets of brokers or servers are called clusters.

Producers : Proccess that publish the data or msg to one or more topics. These are the source of data stream

Consumers : Proccess that read and proccess the data from topics by subscribing to one or more topics.

Partitions : Every broker hold few partitons. Each can either be a leader or a replica for a topic. 

Demo

zookeeper-server-start.sh property file path // start the zookeeper

kafka-server-start.sh property file path // start kafka

jps // shows the status

kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partition 1 --topic mytopic1 

kafka-console-producer.sh --broker-list localhost:9092 --topic mytopic1

previous msg 

Ingesting Flume input streams

Flume is a distributed reliable service for collecting, aggregating and moving large amount of log data. 

Available as separate jar : spark-streaming-flume

Two different approaches for receiving data are

Flume style push based
Pull based using a custome sink


'''