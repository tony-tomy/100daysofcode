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

Windowing

We may often come across situations where our interest is only on what happened, say for the last One hour of time and would want 
these statistics to refresh every other minute.

Note : Here One hour is the window length, while one minute is the slide interval.

Window Operation
Window Operations is a feature provided by Spark Streaming.

Window Operations allows you to apply transformations over a sliding window of data.

Batch Interval - This is the interval at which a DStream is created. We specify this interval while we create the Streaming Context(ssc).

Window Duration/Size - This is a duration over which we perform certain fold operations. Window duration should be a multiple of batch interval.

Sliding Interval - This is interval over which, sliding of the window occurs. This interval has to be a multiple of batch interval.

Lab 2:

import org.apache.spark.streaming.Seconds
import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.Duration

val ssc = new StreamingContext(sc, Seconds(5))
val windowLength = new Duration(20 * 1000)
val slideInterval = new Duration(15 * 1000)

val fileDStream = ssc.textFileStream("file:///usr/spark-2.2.0/data/streaming")
val window = fileDStream.window(windowLength,slideInterval)

window.print

ssc.start()
ssc.awaitTermination()


Checkpointing

A streaming application is expected to operate 24/7 without fail, hence it has to be designed very carefully. It should be capable of recovering from system failures, JVM crashes etc.

To enable this, Spark Streaming uses a mechanism called Checkpointing.

Its required to Checkpoint or store enough information to any of the fault-tolerant storage system so that it can recover from failures.

Metadata Checkpointing
Checkpointing information to systems like HDFS. Usually used to recover from failure of the node running the driver of the streaming application.

By metadata we mean;

Configuration - Configuration which was used to create the streaming application.
DStream operations - The set of DStream operations defined in the application.
Incomplete batches- Batches whose jobs are queued but have not completed yet.
Note : primarily used for recovery from driver failures.

Data Checkpointing
Saving the generated RDDs to a storage system like HDFS.

Data Checkpointing has great relevance in cases where the dependency chain keep on growing with time and the recovery of RDD in any intermediate state becomes difficult.

In-order to avoid unbounded increase in the recovery process intermediate RDDs of stateful transformations are periodically checkpointed to a reliable storage systems.


Reference Link : https://spark.apache.org/docs/latest/streaming-programming-guide.html   , A Quick Example

Final Lab

import org.apache.spark._
import org.apache.spark.streaming._
import org.apache.spark.streaming.StreamingContext._ // not necessary since Spark 1.3

// Create a local StreamingContext with two working thread and batch interval of 1 second.
// The master requires 2 cores to prevent a starvation scenario.

val conf = new SparkConf().setMaster("local[2]").setAppName("NetworkWordCount")
val ssc = new StreamingContext(conf, Seconds(1))

// Create a DStream that will connect to hostname:port, like localhost:9999
val lines = ssc.socketTextStream("localhost", 9999)
This lines DStream represents the stream of data that will be received from the data server. Each record in this DStream is a line of text. Next, we want to split the lines by space characters into words.

// Split each line into words
val words = lines.flatMap(_.split(" "))
flatMap is a one-to-many DStream operation that creates a new DStream by generating multiple new records from each record in the source DStream. In this case, each line will be split into multiple words and the stream of words is represented as the words DStream. Next, we want to count these words.

import org.apache.spark.streaming.StreamingContext._ // not necessary since Spark 1.3
// Count each word in each batch
val pairs = words.map(word => (word, 1))
val wordCounts = pairs.reduceByKey(_ + _)


// Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.print()
The words DStream is further mapped (one-to-one transformation) to a DStream of (word, 1) pairs, which is then reduced to get the frequency of words in each batch of data. Finally, wordCounts.print() will print a few of the counts generated every second.

Note that when these lines are executed, Spark Streaming only sets up the computation it will perform when it is started, and no real processing has started yet. To start the processing after all the transformations have been setup, we finally call

ssc.start()             // Start the computation
ssc.awaitTermination()  // Wait for the computation to terminate
The complete code can be found in the Spark Streaming example NetworkWordCount.

If you have already downloaded and built Spark, you can run this example as follows. You will first need to run Netcat (a small utility found in most Unix-like systems) as a data server by using

$ nc -lk 9999



'''