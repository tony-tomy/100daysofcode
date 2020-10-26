#!python3

# Pyspark



'''
Data
The Large Hadron Collider produces about 30 petabytes of data per year
Facebook’s data is growing at 8 petabytes per month
The New York stock exchange generates about 4 terabyte of data per day
YouTube had around 10 Exabytes of storage in 2017
Internet Archive stores around 19 petabytes of data

Apache Spark is an open-source,lightning fast big data framework which is designed to enhance the computational speed

Capable of leveraging the Hadoop ecosystem, e.g. HDFS, YARN, HBase, S3, …
Has many other workflows, i.e. join, filter, flatMapdistinct, groupByKey, reduceByKey, sortByKey, collect, count, first…
In-memory caching of data (for iterative, graph, and machine learning algorithms, etc.)
Native Scala, Java, Python, and R support
Supports interactive shells for exploratory data analysis
Spark API is extremely simple to use
Developed at AMPLab UC Berkeley, now by Databricks.com

Spark Features

Speed:Spark runs up to 100 times faster than Hadoop MapReduce for large-scale data processing. By controlled partitioning it is achieving this speed.
Deployment:It can be deployed through Mesos, Hadoop via YARN, or Spark’s own cluster manager.
Real-Time: Latency of Spark is very low and in addition it offers computation in Real-time. Both of them are achieved by in-memory computation.
Polyglot:Spark provides high-level APIs in Java, Scala, Python, and R. Spark code can be written in any of these four languages. Spark has shells in both Scala and Python.
Powerful Caching:Simple programming layer provides powerful caching and disk persistence

A Polyglot API
Spark was first coded as a Scala project.
But now it has become a polyglot framework that the user can interface with using Scala, Java, Python or the R language.
The development language is still Scala.

Spark: Python or Scala?
Scala lacks the amount of Data Science libraries and tools as Python.
These limitations in data analytics and data science lead to make a separate API in python for spark usage
In addition python is easy to learn and work with
Code readability, maintainability and familiarity is far better with Python.

PySpark

PySpark is nothing but the Python API for Apache Spark.

It offers PySpark Shell which connects the Python API to the spark core and in turn initializes the Spark context

For any spark functionality, the entry point is SparkContext.
SparkContext uses Py4J to launch a JVM and creates a JavaSparkContext.
By default, PySpark has SparkContext available as sc, so creating a new SparkContext won't work.

Py4J
PySpark is built on top of Spark's Java API.
Data is processed in Python and cached / shuffled in the JVM.
Py4J enables Python programs running in a Python interpreter to dynamically access Java objects in a Java Virtual Machine.
Here methods are called as if the Java objects resided in the Python interpreter and Java collections. can be accessed through standard Python collection methods.
In the Python driver program, SparkContext uses Py4J to launch a JVM and create a JavaSparkContext.
To establish local communication between the Python and Java SparkContext objects Py4J is used on the driver.

Installing and Configuring PySpark
PySpark requires Python 2.6 or higher.
PySpark applications are executed using a standard CPython interpreter in order to support Python modules that use C extensions.
By default, PySpark requires python to be available on the system PATH and use it to run programs.
Among PySpark’s library dependencies all of them are bundled with PySpark including Py4J and they are automatically imported.

RDD in PySpark

Resilient Distributed Datasets (RDDs)
Resilient distributed datasets (RDDs) are known as the main abstraction in Spark.
It is a partitioned collection of objects spread across a cluster, and can be persisted in memory or on disk.
Once RDDs are created they are immutable.
There are two ways to create RDDs:

Parallelizing a collection in driver program.

Referencing one dataset in an external storage system, like a shared filesystem, HBase, HDFS, or any data source providing a Hadoop InputFormat.

Features Of RDDs
Resilient, i.e. tolerant to faults using RDD lineage graph and therefore ready to recompute damaged or missing partitions due to node failures.
Dataset - A set of partitioned data with primitive values or values of values, For example, records or tuples.
Distributed with data remaining on multiple nodes in a cluster.

Creating RDDs
Parallelizing a collection in driver program.

E.g., here is how to create a parallelized collection holding the numbers 1 to 5:

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)

Referencing one dataset in an external storage system, like a shared filesystem, HBase, HDFS, or any data source providing a Hadoop InputFormat.

For example, text file RDDs can be created using the method SparkContext’s textFile.

For the file (local path on the machine, hdfs://, s3n://, etc URI) the above method takes a URI and then reads it as a collection containing lines to produce the RDD.

distFile = sc.textFile("data.txt")

RDD Operations
RDDs support two types of operations: transformations, which create a new dataset from an existing one, and actions, which return a value to the driver program after running a computation on the dataset.

For example, map is a transformation that passes each dataset element through a function and returns a new RDD representing the results.

Similiarly, reduce is an action which aggregates all RDD elements by using some functions and then returns the final result to driver program.

More On RDD Operations
As a recap to RDD basics, consider the simple program shown below:

lines = sc.textFile("data.txt")
lineLengths = lines.map(lambda s: len(s))
totalLength = lineLengths.reduce(lambda a, b: a + b)
The first line defines a base RDD from an external file.

The second line defines lineLengths as the result of a map transformation.

Finally, in the third line, we run reduce, which is an action.

Transformations
Transformations are functions that use an RDD as the input and return one or more RDDs as the output.
randomSplit, cogroup, join, reduceByKey, filter, and map are examples of few transformations.
Transformations do not change the input RDD, but always create one or more new RDDs by utilizing the computations they represent.
By using transformations, you incrementally create an RDD lineage with all the parent RDDs of the last RDD.
Transformations are lazy, i.e. are not run immediately. Transformations are done on demand.
Transformations are executed only after calling an action.

Examples Of Transformations
filter(func): Returns a new dataset (RDD) that are created by choosing the elements of the source on which the function returns true.
map(func): Passes each element of the RDD via the supplied function.
union(): New RDD contains elements from source argument and RDD.
intersection(): New RDD includes only common elements from source argument and RDD.
cartesian(): New RDD cross product of all elements from source argument and RDD.

Actions
Actions return concluding results of RDD computations.
Actions trigger execution utilising lineage graph to load the data into original RDD, and then execute all intermediate transformations and write final results out to file system or return it to Driver program.
Count, collect, reduce, take, and first are few actions in spark.

Example of Actions
count(): Get the number of data elements in the RDD.
collect(): Get all the data elements in an RDD as an array.
reduce(func): Aggregate the data elements in an RDD using this function which takes two arguments and returns one.
take (n): Fetch first n data elements in an RDD computed by driver program.
foreach(func): Execute function for each data element in RDD. usually used to update an accumulator or interacting with external systems.
first(): Retrieves the first data element in RDD. It is similar to take(1).
saveAsTextFile(path): Writes the content of RDD to a text file or a set of text files to local file system/HDFS.

What is Dataframe ?
In general DataFrames can be defined as a data structure, which is tabular in nature. It represents rows, each of them consists of a number of observations.

Rows can have a variety of data formats (heterogeneous), whereas a column can have data of the same data type (homogeneous).

They mainly contain some metadata in addition to data like column and row names.

Why DataFrames ?
DataFrames are widely used for processing a large collection of structured or semi-structured data
They are having the ability to handle petabytes of data
In addition, it supports a wide range of data format for reading as well as writing
As a conclusion DataFrame is data organized into named columns

Features Explained
DataFrames are Distributed in Nature, which makes it fault tolerant and highly available data structure.
Lazy Evaluation is an evaluation strategy which will hold the evaluation of an expression until its value is needed.
DataFrames are Immutable in nature which means that it is an object whose state cannot be modified after it is created

For constructing a DataFrame a wide range of sources are available such as:

Structured data files
Tables in Hive
External Databases
Existing RDDs

Spark SQL

Spark introduces a programming module for structured data processing called Spark SQL.

It provides a programming abstraction called DataFrame and can act as distributed SQL query engine.

Features of Spark SQL
The main capabilities of using structured and semi-structured data, by Spark SQL. Such as:

Provides DataFrame abstraction in Scala, Java, and Python.
Spark SQL can read and write data from Hive Tables, JSON, and Parquet in various structured formats.
Data can be queried by using Spark SQL.

Important classes of Spark SQL and DataFrames
pyspark.sql.SparkSession :Main entry point for Dataframe SparkSQL functionality
pyspark.sql.DataFrame :A distributed collection of data grouped into named columns
pyspark.sql.Column : A column expression in a DataFrame.
pyspark.sql.Row : A row of data in a DataFrame.
pyspark.sql.GroupedData :Aggregation methods, returned by DataFrame.groupBy().

pyspark.sql.DataFrameNaFunctions : Methods for handling missing data (null values).
pyspark.sql.DataFrameStatFunctions : Methods for statistics functionality.
pyspark.sql.functions : List of built-in functions available for DataFrame.
pyspark.sql.types : List of data types available.
pyspark.sql.Window : For working with window functions.

Creating a DataFrame demo
The entry point into all functionality in Spark is the SparkSession class.

To create a basic SparkSession, just use SparkSession.builder:

from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("Data Frame Example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()


Import the sql module from pyspark


from pyspark.sql import *
Student = Row("firstName", "lastName", "age", "telephone")
s1 = Student('David', 'Julian', 22, 100000)
s2 = Student('Mark', 'Webb', 23, 658545)
StudentData=[s1,s2]
df=spark.createDataFrame(StudentData)
df.show()

Data Sources
Spark SQL supports operating on a variety of data sources through the DataFrame interface.
A DataFrame can be operated on using relational transformations and can also be used to create a temporary view.
Registering a DataFrame as a temporary view allows you to run SQL queries over its data.
This chapter describes the general methods for loading and saving data using the Spark Data Sources.

Generic Load/Save Functions
In most of the cases, the default data source will be used for all operations.

df = spark.read.load("file path")

# Spark load the data source from the defined file path

df.select("column name", "column name").write.save("file name")

# The DataFrame is saved in the defined format

# By default it is saved in the Spark Warehouse 
File path can be from local machine as well as from HDFS.

Manually Specifying Options
You can also manually specify the data source that will be used along with any extra options that you would like to pass to the data source.

Data sources fully qualified name is used to specify them, but for built-in sources, you can also use their short names (json, parquet, jdbc, orc, libsvm, csv, text)

Specific File Formats
DataFrames which are loaded from any type of data can be converted to other types by using the syntax shown below.

A json file can be loaded:

df = spark.read.load("path of json file", format="json")

Apache Parquet

Apache Parquet is a columnar storage format available to all projects in the Hadoop ecosystem, irrespective of the choice of the framework used for data processing, the model of data or programming language used.
Spark SQL provides support for both reading and writing Parquet files.
Automatic conversion to nullable occurs when one tries to write Parquet files, This is done due to compatibility reasons.

Reading A Parquet File
Here we are loading a json file into a dataframe.

df = spark.read.json("path of the file")
For saving the dataframe into parquet format.

df.write.parquet("parquet file name")

Verifying The Result
We can verify the result by loading in Parquet format.

pf = spark.read.parquet("parquet file name")

Why Parquet File Format ?
Parquet stores nested data structures in a flat columnar format.
On comparing with the traditional way instead of storing in row-oriented way in parquet is more efficient
Parquet is the choice of Big data because it serves both needs, efficient and performance in both storage and processing.

Advanced Concepts in Data Frame

CSV Loading
To load a csv data set user has to make use of spark.read.csv method to load it into a DataFrame.

Here we are loading a football player dataset using the spark csvreader.

df = spark.read.csv("path-of-file/fifa_players.csv", inferSchema = True, header = True)

inferSchema (default false): From the data, it infers the input schema automatically.

header (default false): Using this it inherits the first line as column names.

To verify we can run df.show(2).

Schema of DataFrame
What is meant by schema?

It’s just the structure of the DataFrame.

To check the schema one can make use of printSchema method.

It results in different columns in our DataFrame, along with the datatype and the nullable conditions.

df.printSchema()

Column Names and Count (Rows and Column)
For finding the column names, count of the number of rows and columns we can use the following methods.

For Column names

df.columns
['ID', 'Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value', 'Wage', 'Special']

Row count

df.count()

Column count

len(df.columns)

Describing a Particular Column
To get the summary of any particular column make use of describe method.

This method gives us the statistical summary of the given column, if not specified, it provides the statistical summary of the DataFrame.

df.describe('Name').show()

Selecting Multiple Columns
For selecting particular columns from the DataFrame, one can use the select method.

Syntax for performing selection operation is:

df.select('Column name 1,'Column name 2',......,'Column name n').show()

dfnew=df.select('Column name 1,'Column name 2',......,'Column name n')

Filtering Data
For filtering the data filter command is used.

df.filter(df.Club=='FC Barcelona').show(3)

To Filter our data based on multiple conditions (AND or OR)
df.filter((df.Club=='FC Barcelona') & (df.Nationality=='Spain')).show(3)

Sorting Data (OrderBy)
To sort the data use the OrderBy method.

In pyspark in default, it will sort in ascending order but we can change it into descending order as well.

df.filter((df.Club=='FC Barcelona') & (df.Nationality=='Spain')).orderBy('ID',).show(5)
To sort in descending order:

df.filter((df.Club=='FC Barcelona') & (df.Nationality=='Spain')).orderBy('ID',ascending=False).show(5)






'''