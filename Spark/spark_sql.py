#!python3

# Spark SQL

'''
Spark SQL is a component of the Spark ecosystem and is used to access structured and semi-structured information.

It is used for relational big data processing in integration with Scala, Python, Java, etc.
It also provides the SQL query execution support to Spark. The process of querying data can be done on data stored in internal 
Spark RDDs and other external data sources.

Classification of Data

Structure data : clasic databases, CSV's, Excels

Semi-structured data : Emails, Log files, Word files

Unstrcutred data : images, audi , videos 

RDD is Resilient Distributed Datasets. It is an immutable, cacheable, distributed set of data. 
It is the primary distributed Dataset abstraction in Spark.

Spark SQL is the solution for data analysis from the Spark family of tool sets. It runs SQL on top of Spark.

Spark SQL uses easy-to-use and straightforward Domain Specific Language (DSL) for selecting, filtering, and aggregating data.

Goals of Spark SQL
Relational processing can be done on both native RDDs and external sources.

DBMS techniques ensure high performance processing.

Easy to process new data sources (both semi-structured data and external sources).

Supports advanced analytics algorithms such as machine learning and graph processing.

Features of Spark SQL

Integrated: Spark SQL provides the integration of SQL queries with Spark programs.

Unified Data Access: Spark SQL allows users to load and query data from different data sources in a variety of data formats including Hive, JSON, Parquet, Avro, JDBC, and ORC.

Hive Compatibility: Spark SQL reuses the Hive frontend, and Hive MetaStore provides the compatibility with the execution of Hive queries and UDFs.

Standard Connectivity: Spark SQL provides the connection through JDBC or ODBC through the server mode.

Scalability: Spark SQL is highly scalable and supports the mid-query fault tolerance, allowing it scale to large jobs. The same execution engine is used for interactive and long queries.

Architecture

Spark SQL is composed of four libraries that are used to interact with relational and procedural processing. They are:

DataSource API
DataFrame API
SQL Interpreter and Optimizer
SQL Service

Architecture - DataSource API
The bottom layer in the architecture of Spark SQL.
The universal layer used for reading and storing structured and semi-structured data into Spark SQL.
Built-in support to read data from various input formats such as Hive, Avro, JSON, JDBC, and Parquet.
Fetches the data from different sources and moves to next layer DataFrame API.

Architecture - DataFrame API
A DataFrame is considered as a distributed set of data organized into named columns. The data read through DataSource API is converted to a tabular column to execute the SQL operations.

Similar to a relational table in SQL used for storing data into tables.
Processes data with a size ranging from Kilobytes to Petabytes on a single node or multi-node clusters.
Integrated easily with all Big data tools and frameworks.
Provides API for Scala, Python, Java and R programming.
Supports several data formats and storage systems.

SQL Interpreter and Optimiser:
Constructed using Scala functional programming and provides pattern matching abilities.
Supports run-time and resource utilization optimization
Rule-based optimization enables queries to run faster than RDD's.
Converts the dataframe based code to catalyst expressions and then to Java bytecode.
SQL Service:
The starting point to work with structured data in Spark.
Creates DataFrame objects and executes SQL queries.
Includes ANSI SQL parser that supports subqueries.

There are two ways of interacting with the Spark SQL Library. They are:

SQL queries
DataFrame API calls
The queries/calls are converted to language-neutral expressions called unresolved logical plan. A logical plan is derived from the unresolved logical plan by performing validations against the metadata in DataFrame.

By applying standard optimization rules to the logical plan, it is further transformed to a optimized logical plan. Finally, the optimized logical plan is split into multiple physical plans that are pushed down to RDDs to operate on the data.

The best out of multiple physical plans are chosen based on the optimal cost. Cost is the runtime and resource utilization.

The performance of Spark SQL remains the same across all the supported languages, since, the calls/queries are converted into language-neutral expressions.

Introducing SparkSession

In the earlier versions of Spark, RDD being the main API, SparkContext was considered as the entry point to Spark. SparkContext uses SparkConf to determine the configuration details for the given application. There were different connection objects like StreamingContext for Streaming, SqlContext for SQL, HiveContext for Hive and so on. SparkContext connects to any of these Contexts processing.

In Spark 2.0, there is a new entry point for Dataset and Dataframe APIs, known as, SparkSession. It is a combination of SqlContext, HiveContext, and StreamingContext. These contexts need not be created explicitly as SparkSession has access to all these contexts.

Creating SparkSession
SparkSession uses builder design pattern to create an instance. This pattern will reuse a Spark context if it exists, otherwise, creates a new Spark context.

The following code is to create a Spark session.

val sparkSession = SparkSession.builder.
  master("local")
  .appName("Spark session in Fresco")
  .getOrCreate()
The value local for the master is used as a default value to launch the application in test environment locally.

SparkSession with Hive
The following code snippet creates Spark session with Hive support.

val sparkSession = SparkSession.builder.
  master("local")
  .appName("Spark session with hive in Fresco")
  .enableHiveSupport()
  .getOrCreate()
enableHiveSupport() enables Hive support.

Reading Data
SparkSession is used as an entry point to read data.

val jsonData = spark.read.json(<path>)

Running SQL Queries
SparkSession is used to run SQL queries, and the results are returned in the form of DataFrame.

display(spark.sql("select * from Fresco"))

Setting Config Options
Used to set and get runtime configuration options.

spark.conf.set("spark.fresco.config", "play")

spark.conf.get("spark.fresco.config")

Reading Spark SQL from Hive
The following code is used to read from Hivetables using SparkSession object.

//drop the table if it already exists in the same name.

spark.sql("DROP TABLE IF EXISTS sample_hive_table")

//save as a hive table

spark.table("sample_table").write.saveAsTable("sample_hive_table")

// query on hive table 

val resultsHiveDF = spark.sql("SELECT name, rollno,totalmark,division FROM sample_hive_table WHERE totalmark > 40000")

resultsHiveDF.show(10)

DataFrame - Introduction

In Spark SQL, the programming abstraction is achieved using the concept of DataFrames (starting from Spark 1.3 release). It is based on the data frame concept in R language.

Dataframe allows data selection, filtering, and aggregation. Since data frames store more information about the structure of the data, the processing is done efficiently as compared to RDD.

DataFrame is similar to relational database tables with rows of named columns.

DataFrame features

API availability in different programming languages
Hive compatibility
Scales from KiloBytes data to Petabytes data
Easy integration with Big Data tools and applications

Creating DataFrame
With a SparkSession, applications can create DataFrame easily from

an existing RDD
a hive table
Spark data sources.

To create a DataFrame from a List or Seq using spark.createDataFrame:

    val df = spark.createDataFrame(List(("John", 35), ("Thomas", 30), ("Martin", 15)))
Here spark mentioned is the SparkSession object.

To create a DataFrame based on the content of a JSON file:

    val df = spark.read.json("examples/src/main/resources/data.json")

DataFrame Content
To show the content of the DataFrame:

    df.show()

DataFrame Operations
Following are few examples of dataframe operations:

To select people older than 31,

df.filter($"age" > 31).show()
Here $age refers to age column of the dataframe. import spark.implicits._ has to be included to refer to the columns with $notation.

Querying DataFrames
It is possible to run SQL queries programmatically using a dataframe and return the result as a DataFrame.

To do that, the dataframe has to be first registered as a temporary view.

val df =  spark.read.json("examples/src/main/resources/data.json")

df.createOrReplaceTempView("data")

val sqlDF = spark.sql("SELECT * FROM data")
 sqlDF.show()

DataFrames across Sessions
To query DataFrames using SQL, one can also choose to create a temporary global view using createGlobalTempView. This way the temporary view can be made available for querying across the sessions.

However, scope of dataframe view created using createOrReplaceTempView is session restricted and is not visible outside of the session where the view is created.

val df =  spark.read.json("examples/src/main/resources/data.json")

df.createGlobalTempView("data")

val sqlDF = spark.sql("SELECT * FROM data")
sqlDF.show()

Dataframe API in Spark SQL:

Improves performance and scalability.
Avoids garbage-collection cost for individual objects for every row in the dataset.
In spite of the advantages mentioned above, there are few challenges while using DataFrames.

Since compile-time type safety provision is not available with DataFrame API, the data cannot be manipulated if the structure is not known.
Another challenge is that a domain object cannot be regenerated once it is converted into dataframe.

Lab 1 : 

Enter the Spark shell: spark-shell.

Import the SparkSession package: import org.apache.spark.sql.SparkSession.

Create a SparkSession object: val spark= SparkSession.builder.appName("My Spark Application").master("local[*]").config("spark.sql.warehouse.dir", "/root/spark-warehouse").getOrCreate

Create a DataFrame
Paste the following code to create a dataFrame using the 'createDataFrame' function: val langPercentDF = spark.createDataFrame(List(("Scala", 35), ("Python", 30), ("R", 15), ("Java", 20)))

Display the values in the DataFrame
langPercentDF.show()

Rename the columns
Paste the following code to rename the columns, and display the new DataFrame: val lpDF = langPercentDF.withColumnRenamed("_1", "language").withColumnRenamed("_2", "percent")

lpDF.show()

DataFrame in descending order of percentage
Paste the following code to order the DataFrame in descending order of percentage: lpDF.orderBy(desc("percent")).show(false)

Dataset                                      

Dataset is known as a data structure in Spark SQL that provides type safety and object-oriented interface.

Dataset:

Acts as an extension to DataFrame API.
Combines the features of DataFrame and RDD.
Serves as a functional programming interface for working with structured data.
Overcomes the limitations of RDD and DataFrames - the absence of automatic optimization in RDD and absence of compile-time type safety in Dataframes.







'''