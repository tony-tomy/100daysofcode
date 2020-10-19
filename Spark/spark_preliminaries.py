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
input.registerTempTable("students")
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

They can be utilized to implement sums or counters.

Programmers can include support for new types.

Spark natively offers support for accumulators of numeric types.

RDD Operations






'''