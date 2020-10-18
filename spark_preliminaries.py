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
