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

Features of Dataset
Offers optimized query using **Tungsten**and Catalyst Query optimizer. These will be discussed in upcoming topics.
Capable of analyzing during compile-time.
Capable of converting type-safe dataset to untyped DataFrame using methods - toDS():Dataset[A], toDF():DataFrame and toDF(columnnames:String):DataFrame.
Delivers high performance due to faster computation.
Low memory consumption.
Provides unified API for Java and Scala.

Creating Datasets
Dataset uses a specialized Encoder to serialize the objects for processing or transmitting over the network.

Dataset can be created in the following ways:

Encoders are created for case classes. Call .toDS() on a sequence to convert the sequence to a Dataset.

    val dsCaseClass = Seq(Person("John", 35)).toDS()
    dsCaseClass.show()

Dataset from RDD
A dataset can be created from RDD as shown:

    val ds=rdd.DS()
    ds.show()

Dataset from DataFrame
Dataset can be created from DataFrame as well. Call df.as[SomeCaseClass] to convert the DataFrame to a Dataset.

 val peopleDS = spark.read.json("examples/src/main/resources/data.json").as[Person]
 peopleDS.show()

Lab 01:

spark-shell

import org.apache.spark.sql.SparkSession

val spark= SparkSession.builder.appName("My Spark Application").master("local[*]").config("spark.sql.warehouse.dir", "/root/spark-warehouse").getOrCreate

Call the function spark.range to get the output starting from 5 to 50, with increments of 5
val numDS = spark.range(5, 50, 5)

numDS.show()

Call the function 'orderby' to reverse the order in the DataSet and display the first 5 values
numDS.orderBy(desc("id")).show(5)

Compute descriptive stats and display them
numDS.describe().show()


DataFrames released in Spark 1.3 on 2013.
DataSet released in Spark 1.6 on 2015.

DataFrames is an organized form of distributed data into named columns that is similar to a table in a relational database.
Dataset is an upgraded release of DataFrame that includes the functionality of object-oriented programming interface, type-safe and fast.

In DataFrames, data is represented as a distributed collection of row objects.
In DataSets, data is represented as rows internally and JVM Objects externally.

After RDD transformation into dataframe, it cannot be regenerated to its previous form.
After RDD transformation into a dataset, it is capable of converting back to original RDD.

In dataframe, a runtime error will occur while accessing a column that is not present in the table. It does not provide compile-time type safety.
In dataset, compile time error will occur in the same scenario as dataset provides the compile-time type safety.

The Dataframe API provides a Tungsten execution backend that handles the memory management explicitly and generates bytecode dynamically.
The Dataset API provides the encoder that handles the conversion from JVM objects to table format using Spark internal Tungsten binary format.

Dataframe supports the programming languages such as Java, Python, Scala, and R.
Dataset supports Scala and Java only.

Datatypes in Spark SQL

Numeric Datatypes
ByteType - Represents one-byte signed integer numbers ranging from -128 to 127.
IntegerType - Represents four-byte signed integer numbers.
FloatType - Represents four-byte single precision floating point numbers.
DecimalType - Represents arbitrary-precision signed decimal numbers.

StringType - Represents character string values.

BinaryType - Represents byte sequence values.

BooleanType - Represents boolean values.

TimestampType - Represents date and time values including values of fields - year, month, day, hour, minute, and second.

Complex Datatypes - ArrayType
ArrayType(elementType, containsNull)

Refers to sequence of elements with the type of elementType.
containsNull is used to indicate if elements in a ArrayType value can have null values.
Let's create a DataFrame with an ArrayType column to list best cricket players of some countries.

val playersDF = spark.createDF(
List(
 ("India", Array("Sachin", "Dhoni")),
 ("Australia", Array("Ponting"))), 
List(
("team_name", StringType, true),
("top_players", ArrayType(StringType, true), true)
)
)

MapType(keyType, valueType, valueContainsNull)

Contains a set of key-value pairs.
keyType denotes the data type of keys, and valueType denotes the data type of values.
Keys cannot have null values.
valueContainsNull is used to verify whether values of a MapType value can have null values.

val singerDF = spark.createDF(
List(
("sublime", Map(
  "good_song" -> "santeria",
  "bad_song" -> "doesn't exist")
),
("prince_royce", Map(
  "good_song" -> "darte un beso",
  "bad_song" -> "back it up")
)
), 
List(
("name", StringType, true),
("songs",MapType(StringType, 
 StringType, true), true)
 )
)

StructType(fields)

Represents values with the structure described by a sequence of StructFields (fields). StructField(name, dataType, nullable):

Represents a field in a StructType.

name indicates the name of a field, and datatype indicates the data type of a field.

nullable is used to indicate if values of this fields can have null values.

Let's create a DataFrame with a StructType.

val rdd = sc.parallelize
    (Array(Row(ArrayBuffer(1,2,3,4))))
val df = sqlContext.createDataFrame(
        rdd,StructType(Seq(StructField 
      ("list", ArrayType(IntegerType, 
      false), false)
)

Aggregations
An aggregation is an act of collecting together.

Spark SQL has:

Built-in aggregations such as functions designed for DataFrames - avg(), max(), min(),count(),approx_count_distinct(), etc.
User-defined aggregations - both UnTyped and Type-Safe.

Untyped Aggregation Functions
To implement a custom untyped user-defined aggregation function, the user has to extend the UserDefinedAggregateFunction abstract class.

Creating a custom aggregation function to calculate the average.

 object CalculateAverage extends UserDefinedAggregateFunction
Aggregate function can have input arguments

def inputSchema: StructType = StructType(StructField("inputColumn", LongType) :: Nil)
Values in the aggregation buffer with data types

def bufferSchema: StructType = {
StructType(StructField("total", LongType) :: StructField("count", LongType) :: Nil)
}
Mention the data type of the returned value of the aggregation function

 def dataType: DataType = DoubleType

Initialize the values of aggregation buffer

def initialize(buffer: MutableAggregationBuffer): Unit = {
buffer(0) = 0L
buffer(1) = 0L
}
Here, the given aggregation buffer is updated with new input data given:

 def update(buffer: MutableAggregationBuffer, input: Row): Unit = {
if (!input.isNullAt(0)) {
  buffer(0) = buffer.getLong(0) + input.getLong(0)
  buffer(1) = buffer.getLong(1) + 1
}
}

Two aggregation buffers merged here and stores the updated buffer values to buffer1.

def merge(buffer1: MutableAggregationBuffer, buffer2: Row): Unit = {
buffer1(0) = buffer1.getLong(0) + buffer2.getLong(0)
buffer1(1) = buffer1.getLong(1) + buffer2.getLong(1)
}
The final average calculation is done here.

def evaluate(buffer: Row): Double = buffer.getLong(0).toDouble / buffer.getLong(1)
The aggregation function is registered here for further accessing.

spark.udf.register("calculateAverage", CalculateAverage)
val result = spark.sql("SELECT calculateAverage(age) as average_age FROM people")

result.show()

Type Safe Aggregation Functions
To implement a custom type safe user-defined aggregation function, the user has to extend the Aggregator abstract class.

Creating a custom aggregation function to calculate the average. People is a base class as input, Average is the buffer and Double is the return type.

object CalculateAverage extends Aggregator[People, Average, Double]
Initializing and compiling two buffer values to produce a new value.

 def zero: Average = Average(0L, 0L)
 def reduce(buffer: Average, people: People): Average = {
buffer.total += people.age
buffer.count += 1
buffer
}
Intermediate values are merged here:

def merge(b1: Average, b2: Average): Average = {
b1.total += b2.total
b1.count += b2.count
b1
}

Aggregation function calculation is done here:

 def finish(reduction: Average): Double = reduction.sum.toDouble / reduction.count
Encoder for the intermediate value type is specified here:

def bufferEncoder: Encoder[Average] = Encoders.product
Encoder for the final output value type is specified here:

 def outputEncoder: Encoder[Double] = Encoders.scalaDouble

Type Safe Aggregation Functions
Read JSON:

val ds = spark.read.json("examples/src/main/resources/data.json").as[Person]
ds.show()

Change the function to a TypedColumn and give it a name.

val averageAge = CalculateAverage.toColumn.name("average_age")
val result = ds.select(averageAge)
result.show()

Spark SQL Optimization
Optimization refers to the fine-tuning of a system to make it more efficient and to reduce its resource utilization.

Spark SQL Optimization is achieved by Catalyst Optimizer.

Catalyst Optimizer is:

The core of Spark SQL.
Provides advanced programming language features to build a query optimizer.
Based on functional programming construct in Scala.
Supports rule-based optimization (defined by a set of rules to execute the query) and cost-based optimization (defined by selecting the most suitable way to execute a query).
To manipulate the tree, the catalyst contains the tree and the set of rules.

Tree
Tree is the main datatype in Catalyst that contains node objects.

Every node will have a node type and zero or more children. The new nodes created are immutable in nature and are defined as subclasses of TreeNode class in Scala. These objects can be manipulated using functional transformations as explained in the following example.

Consider three node classes:

Constant value:

Literal(value:Int)
Attribute value from an input:

attribute(name:String) 
Subtraction of two expressions:

Sub(left:TreeNode,right:TreeNode)

Rule
Trees can be manipulated using rules which can be defined as a function from one tree to another tree. This rule can run the arbitrary code on the input tree.

The common approach is to use a pattern matching function and further the subtree replaced with a specific structure.

Using transform function on trees, we can recursively apply pattern matching on all nodes of the tree, transforming the ones that match each pattern to a result.

Example:

tree.transform 
{
case
   Sub(worth(c1),worth(c2))
       => worth(c1+c2) 
 }

The pattern matching expression that is passed to transform is a partial function. It only needs to match to a subset of all possible input trees.

The catalyst will check to that part of the tree the given rule applies and then skip automatically over the trees that do not match.

The rule can match the multiple patterns with the same transform call.

Example:

tree.transform 
 {
   case Sub(worth(c1), worth(c2))
        => worth(c1-c2)
   case Sub(left , worth(0)) => left
   case Sub(worth(0), right) => right
}

Spark SQL Execution

Front End: Hive Query, SQL Query, DataFrame

Catalyst : Unresolved logical plan -> Logical Plan -> Optimised logical plan
                                    ^
                          Schema catalog

Back End : Physical plan -> Cost Model -> Selected physical plans -> RDD's

In Spark SQL, the Catalyst performs the following functions:

Analysis
Logical Optimization
Physical Planning
Code Generation

1] Analysis Phase
The beginning of Spark SQL optimization is with relation to be computed either from abstract syntax tree returned by SQL parser or dataframe object created using API.

Here in both cases,the query may contains unresolved attributes which means the type of attribute is unknown and have not matched it to an input table.

SELECT value from PROJECT
In the above query,the type of value is not known and not even sure whether its valid existing column.

Catalyst rules and Catalog object is used in Spark SQL to track all data sources to resolve these unresolved attributes. This is done by creating an unresolved logical plan and then apply the below steps.

Lookup the relation BY NAME FROM CATALOG.
Map the named attribute like 'value' as in example above.
Determine the attribute which refer to the same value to give them unique ID.
Propagating and pushing types through expressions.

2] Logical Optimization Phase
In this phase of Spark SQL optimization applies the standard rule-based optimization to the logical plan. It includes-

constant folding
predicate pushdown
project pruning
null propagation
It is extremely easy to add rules for a wide variety of situations.

3] Physical Planning Phase
In this phase of Spark SQL Optimization,one or more physical plan is formed from the logical plan,using physical operator matches the Spark execution engine.

Here Cost-based optimization is used to select join algorithms. The framework supports broader use of cost-based optimization for small relation SQL uses broadcast join.

Using the rule, it can estimate the cost recursively for the whole tree.

4] Code Generation Phase
In code generation phase of Spark SQL optimization,java byte code is generated to run on each machine.

Its very tough to build code generation engines. Catalyst make use of the special feature of Scala language,QUASIQUOTES to make code generation easier.

Quasiquotes allow the programmatic construction of AST (Abstract syntax tree)in scala language.At runtime this can then fed to the Scala compiler to generate bytecode.

Catalyst can transform a tree which represents an expression in SQL to AST for Scala code to evaluate that expression,compile and run the generated code.

Performance Tuning Options in Spark SQL
Following are the different Spark SQL performance tuning options available.

1. spark.sql.codegen

Used to improve the performance of large queries.
The value of spark.sql.codegen should be true.
The default value of spark.sql.codegen is false.
Since it has to run a compiler for each query, performance will be poor for very short queries.
2. spark.sql.inMemorycolumnarStorage.compressed

We can compress the in-memory columnar storage automatically based on statistics of data.
The value of spark.sql.inMemorycolumnarStorage.compressed should be true.
Its default value will be false.

3. spark.sql.inMemoryColumnarStorage.batchSize

We can boost up memory utilization by giving the larger values for this parameter spark.sql.inMemoryColumnarStorage.batchSize.
The default value will be 10000.
4. spark.sql.parquet.compression.codec

We can enable high speed and reasonable compression using the parameter spark.sql.parquet.compression.codec.
The snappy library can be used for compression and decompression.

Lab : 02

Task
Create a json file named "People.json" using the command vim People.json, and then copy the following data to the file through IDE: {"name":"Rahul","age":"35"} {"name":"Sachin","age":"46"}

Read the json file and create a DataFrame with the json data. Display the result.

val df = spark.read.json("People.json")

df.show()

Create a case class using the following command: case class Person(name: String, age: String)

Read the json file and create a DataSet with the json data using case class. Display the result.

val peopleDS = spark.read.json("People.json").as[Person]
 
peopleDS.show()

Lab : 03

Task
Create a json file named "People.json" using the command vim People.json, and then copy the following data to the file through IDE: {"name":"Rahul","age":"35"} {"name":"Sachin","age":"46"}

Read the json file and create a DataFrame with the json data. Display the result.

val DF = spark.read.json("People.json")

DF.show()

Save the Dataframe to a Parquet file format:

// DataFrames can be saved as Parquet files, maintaining the schema information
DF.write.parquet("data.parquet")

Read the saved parquet file to a Dataframe

val parquetFileDF = spark.read.parquet("data.parquet")

Display the Dataframe contents

parquetDF.show()


Lab : 03

Read the csv file from the Spark CSV Reader.

Read the csv file to the Dataframe cdf.

While reading the csv file, keep Header and Inferschema as true.

Verify the Dataframe by displaying its schema and first 5 contents.

val cdf = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("demography.csv")

cdf.show(5)

Find the Average of Total Population.

cdf.select(avg($"Total Population")).show()

Save the Average to a Parquet file avg

Find the Total of Total Males

cdf.select(sum($"Total Males")).show()

val output = cdf.select(sum($"Total Males"))


val diamonds = spark.read.format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")

display(diamonds)

apt-get update; apt-get install vim -y;.

import org.apache.spark.sql.functions._

import spark.implicits._

df.select(avg($"RBIs")).show()


'''