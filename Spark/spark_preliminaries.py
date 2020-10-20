#!python3

# Spark Preliminaries 

'''
Apache Spark is an open source cluster computing framework that provides an interface for entire programming clusters with 
implicit data parallelism and fault-tolerance.

Spark runs computations in memory and provides a quicker system for complex applications operating on disk.

Spark covers various workloads needing a dedicated distributed systems namely streaming, interactive queries, iterative algorithms, 
and batch applications.

Spark Components

1. Spark Core : Includes the primary functionality of Spark, namely components for task scheduling, fault recovery, memory management, 
interacting with storage systems, etc
2. Spark SQL : Packages for working with structured data.Enable SQL and HQL. Support various data JSON, Parquet & Hive
3. Spark Streaming : Spark component that allows live-streaming data processing
4. MLlib : ML Features
5. GraphX : A library for performing graph-parallel computations and manipulating graphs.


'''

'''

import sys
from operator import add
from pyspark import SparkSession, Row

spark = SparkSession\
     .builder\
     .appName("PythonWordCount")\
     .getOrCreate()

data = [Row(col1='pyspark and spark', col2=1), Row(col1='pyspark', col2=2), Row(col1='spark vs hadoop', col2=2), Row(col1='spark', col2=2), Row(col1='hadoop', col2=2)]
df = spark.createDataFrame(data)
lines = df.rdd.map(lambda r: r[0])

counters = lines.flatMap(lambda x: x.split(' ')) \
     .map(lambda x: (x, 1)) \
     .reduceByKey(add)

output = counters.collect()
sortedCollection = sorted(output, key = lambda r: r[1], reverse = True)

for (word, count) in sortedCollection:
    print("%s: %i" % (word, count))

'''

'''
import random
from pyspark import SparkContext
sc = SparkContext(appName="EstimatePi")
def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1
NUM_SAMPLES = 1000000
count = sc.parallelize(range(0, NUM_SAMPLES)) \
             .filter(inside).count()
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
sc.stop()

'''

'''

SparkConf

SparkConf stores configuration parameters for a Spark application.

These configuration parameters can be properties of the Spark driver application or utilized by Spark to allot resources on the cluster,
like memory size and cores.

SparkConf object can be created with new SparkConf() and permits you to configure standard properties and arbitrary key-value pairs 
via the set() method.

val conf = new SparkConf()
             .setMaster("local[4]")
             .setAppName("FirstSparkApp")

val sc = new SparkContext(conf)

SparkContext

Main entry point for Spark functionality

SparkContext can be utilized to create broadcast variables, RDDs, and accumulators, and denotes the connection to a Spark cluster.

To create a SparkContext, you first have to develop a SparkConf object that includes details about your application.

There may be only one SparkContext active per JVM. Before creating a new one, you have to stop() the active SparkContext.

val sc = new SparkContext(conf)

RDD 

Resilient distributed datasets (RDDs) are the known as the main abstraction in Spark.

It is a partitioned collection of objects spread across a cluster, and can be persisted in memory or on disk.

Once created, RDDs are immutable.

RRD's Features

Resilient, i.e. tolerant to faults using RDD lineage graph and therefore ready to recompute damaged or missing partitions due to node failures.

Dataset - A set of partitioned data with primitive values or values of values, For example, records or tuples.

Distributed with data remaining on multiple nodes in a cluster.

Creating RDD's

1. Parallelazing a collection of driver programs

val data = Array(1, 2, 3, 4, 5)
val newRDD = sc.parallelize(data)

2. Referencing one dataset in an external storage system, like a shared filesystem, HBase, HDFS, or any data source providing 
a Hadoop InputFormat

val newRDD = sc.textFile("data.txt")

Dataframes 

Similar to an RDD, a DataFrame is an immutable distributed set of data.

Unlike an RDD, data is arranged into named columns, similar to a table in a relational database.

Created to make processing simpler, DataFrame permits developers to impose a structure onto a distributed collection of data, enabling higher-level abstraction

Creating Dataframes

Applications can create DataFrames from a Hive table, data sources, or from an existing RDD with an SQLContext

val sc: SparkContext // An existing SparkContext.
val sqlContext = new org.apache.spark.sql.SQLContext(sc)
val df = sqlContext.read.json("home/spark/input.json")
// Shows the content of the DataFrame to stdout
df.show()

SQL on Dataframes 

The sql function on a SQLContext allows applications to run SQL queries programmatically and returns the result as a DataFrame.

val sc: SparkContext // An existing SparkContext.
val sqlContext = new org.apache.spark.sql.SQLContext(sc)
val df = sqlContext.read.json("home/spark/input.json")
df.registerTempTable("students")
val teenagers = sqlContext.sql("SELECT name, age FROM students WHERE age >= 13 AND age <= 19")

Dataset

Dataset is a new interface included in Spark 1.6, which provides the advantages of RDDs with the advantages of Spark SQL’s optimized execution engine.

It is an immutable, strongly-typed set of objects that are mapped to a relational schema.

A DataFrame is a known as a Dataset organized into named columns.

Dataset will act as the new abstraction layer for Spark from Spark 2.0.


val lines = sqlContext.read.text("/log_data").as[String]
val words = lines
  .flatMap(_.split(" "))
  .filter(_ != "")   # Here, we have created a dataset lines on which RDD operations like filter and split are applied.

Benefits of Dataset APIs

Static-typing and runtime type-safety

High-level abstraction and custom view into structured and semi-structured data

Higher performance and Optimization

SparkSession - a New Entry Point

SparkSession, introduced in Apache Spark 2.0, offers a single point of entry to communicate with underlying Spark feature and enables programming Spark with Dataset APIs and DataFrame.

In previous versions of Spark, spark context was the entry point for Spark. For streaming, you required StreamingContext for hive HiveContext and for SQL SQLContext.

As Dataframe and DataSet APIs are the new standards, Spark 2.0 features SparkSession as the new entry point.

SparkSession is a combination of HiveContext, StreamingContext, and SQLContext. All the APIs available on these contexts are available on SparkSession also. It internally has a spark context for actual computation.

Creating a spark session

val dataLocation = "file:${system:user.dir}/spark-data"
// Create a SparkSession
val spark = SparkSession
   .builder()
   .appName("SparkSessionExample")
   .config("spark.sql.data.dir", dataLocation)
   .enableHiveSupport()
   .getOrCreate()

A SparkSession can be built utilizing a builder pattern. The builder will automatically reuse an existing SparkContext if one exists; and create a SparkContext if it does not exist.

Configuring Properties
Once the SparkSession is instantiated, you can configure the runtime config properties of Spark. E.g: In this code snippet, we can alter the existing runtime config options.

//set new runtime options
spark.conf.set("spark.executor.memory", "1g")
spark.conf.set("spark.sql.shuffle.partitions", 4)
//get all settings
val configMap:Map[String, String] = spark.conf.getAll()

Running SQL Queries
SparkSession is the entry point for reading data, akin to the old SQLContext.read. It can be utilized to execute SQL queries across data, getting the results back as a DataFrame.

val jsonData = spark.read.json("/home/user/employee.json")

display(spark.sql("select * from employee"))

Access to Underlying SparkContext
SparkSession.sparkContext returns the subsequent SparkContext, employed for building RDDs and managing cluster resources.

spark.sparkContext
res17: org.apache.spark.SparkContext = org.apache.spark.SparkContext@2debe9ac

Shared Variables

Spark offers two limited types of shared variables for two common usage patterns: accumulators and broadcast variables.

Broadcast Variables
Enables the programmer to keep a read-only variable cached on each machine instead of shipping a copy of it with tasks.

Generated from a variable v by calling SparkContext.broadcast(v)

Its value can be accessed by calling the value method. The subsequent code shows this:

scala> val broadcastVar = sc.broadcast(Array(1, 2, 3, 4, 5))
broadcastVar: org.apache.spark.broadcast.Broadcast[Array[Int]] = Broadcast(0)
scala> broadcastVar.value
res0: Array[Int] = Array(1, 2, 3, 4, 5)

Accumulators
Accumulators are known as the variables that are only “added” via an associative and commutative operation and can, hence, be efficiently supported in parallel.

val accum = sc.longAccumulator("My Accumulator")

sc.parallelize(Array(1, 2, 3, 4)).foreach(x => accum.add(x))

accum.value

They can be utilized to implement sums or counters.

Programmers can include support for new types.

Spark natively offers support for accumulators of numeric types.

RDD Operations

val file = sc.textFile("hdfs://.../wordcounts-*.gz")
val counts = file.flatMap(line => line.split(" "))
                   .map(word => (word, 1))
                   .reduceByKey(_ + _)
counts.saveAsTextFile("hdfs://.../wordcountOutput")

flatMap, map,reduceByKey and saveAsTextFile are the operations on the RDDs

Transformations

Transformations are functions that use an RDD as the input and return one or more RDDs as the output.
randomSplit, cogroup, join, reduceByKey, filter, and map are examples of few transformations.
Transformations do not change the input RDD, but always create one or more new RDDs by utilizing the computations they represent.
By using transformations, you incrementally create an RDD lineage with all the parent RDDs of the last RDD.
Transformations are lazy, i.e. are not run immediately. Transformations are done on demand.

filter(func): Returns a new dataset (RDD) that are created by choosing the elements of the source on which the function returns true.

map(func): Passes each element of the RDD via the supplied function.

union(): New RDD contains elements from source argument and RDD.

intersection(): New RDD includes only common elements from source argument and RDD.

cartesian(): New RDD cross product of all elements from source argument and RDD

Actions

Actions return concluding results of RDD computations.
Actions trigger execution utilizing lineage graph to load the data into original RDD, and then execute all intermediate transformations and write final results out to file system or return it to Driver program.
Count, collect, reduce, take, and first are few actions in spark.

count(): Get the number of data elements in the RDD

collect(): Get all the data elements in an RDD as an array

reduce(func): Aggregate the data elements in an RDD using this function which takes two arguments and returns one

take (n): Fetch first n data elements in an RDD computed by driver program.

foreach(func): Execute function for each data element in RDD. usually used to update an accumulator or interacting with external systems.

first(): Retrieves the first data element in RDD. It is similar to take(1).

saveAsTextFile(path): Writes the content of RDD to a text file or a set of text files to local file system/HDFS.

records = spark.textFile(“hdfs://...”)
errors = records.filter(_.startsWith(“ERROR”))
messages = errors.map(_.split(‘\t’)(2))
cachedMessages = messages.cache()
cachedMessages.filter(_.contains(“400”)).count

Lazy Evaluation

When we call a transformation on RDD, the operation is not immediately executed. Alternatively, Spark internally records 
meta-data to show this operation has been requested. It is called as Lazy evaluation

Hive Integration
Hive comes packaged with the Spark library as HiveContext that inherits from SQLContext. Utilizing HiveContext, you can create and find tables in the HiveMetaStore and write queries on it using HiveQL.

When hive-site.xml is not configured, the context automatically produces a metastore named as metastore_db and a folder known as warehouse in the current directory.

Data Load from Hive to Spark

scala> val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

scala> sqlContext.sql("CREATE TABLE IF NOT EXISTS employee(id INT, name STRING, age INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'")

scala> sqlContext.sql("LOAD DATA LOCAL INPATH 'employee.txt' INTO TABLE employee")scala> sqlContext.sql("LOAD DATA LOCAL INPATH 'employee.txt' INTO TABLE employee")

scala> val result = sqlContext.sql("FROM employee SELECT id, name, age")

scala> result.show()

A Spark application includes a single driver process and a collection of executor processes scattered over nodes on the cluster.

Both the executors and the driver usually run as long as the application runs.

Spark Driver
Program that produces the SparkContext, connecting to a given Spark Master.

Declares the actions and transformations on RDDs of data.

Spark Executors
Runs the tasks, return results to the driver.

Offers in memory storage for RDDs that are cached by user programs.

Multiple executors per nodes possible

Cluster Managers
Standalone – a simple cluster manager added with Spark that makes it simple to establish a cluster.

Apache Mesos – a cluster manager that can run service applications and Hadoop MapReduce.

Hadoop YARN – the resource manager in Hadoop 2.

Commonly Used Options
class: entry point for your application (e.g. org.apache.spark.examples.SparkPi)

master: master URL for the cluster (e.g. spark://23.195.26.187:7077)

deploy-mode: Whether to deploy your driver on the worker nodes (cluster) or locally as an external client (client) (default: client)

conf: Arbitrary Spark configuration property in key=value format.

application-jar: Path to a bundled jar with the application and dependencies.

application-arguments: Arguments passed to the main method of your main class, if any.

Deployment Modes
Choose which mode to run using the --deploy-mode flag

Client - Driver runs on a dedicated server (e.g.: Edge node) inside a dedicated process. Submitter starts the driver outside of the cluster.

Cluster - Driver runs on one of the cluster's Worker nodes. The Master selects the worker. The driver operates as a dedicated, standalone process inside the Worker.

Running a Spark Job
Spark submit program initiated with spark driver; creates logical DAG.

spark-submit /usr/spark-2.2.0/examples/src/main/python/pi.py

Spark Driver program checks with the cluster manager-YARN (Mesos or Standalone) for resource availability for executors and launches it.

Executors created in Nodes, register to spark driver.

Spark driver converts the actions and transformations defined in the main method and allocate to executors.

Executors performs the transformations and; actions return

values to the driver.

While reading from an HDFS, each executor directly applies the subsequent Operations, to the partition in the same task


RDD Caching and Persisting

RDDs can be cached with the help of cache operation. They can also be persisted using persist operation.

Cache persists with default storage level MEMORY_ONLY.

RDDs can also be unpersisted to eliminate RDD from a permanent storage like memory and disk

result = input.map(<Computation>) 

result.persist(LEVEL)


Final Lab

import org.apache.spark.sql.SparkSession

val data = spark.sparkContext.textFile("C:/tmp/files/text01.csv")

type data

val splitrdd = data.map(line=>line.split(","))

val mofm = splitrdd.map(x=>(x(13),1))

val reduced_rdd = mofm.reduceByKey(_ + _).map(item => item.swap).sortByKey(false).take(5)

val output = sc.parallelize(reduced_rdd)

output.saveAsTextFile("file path")



'''