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

Statistical and Mathematical Functions with DataFrames in Apache Spark

Random Data Generation
Random Data generation is useful when we want to test algorithms and to implement new ones.

In Spark under sql.functions we have methods to generate random data. e.g., uniform (rand), and standard normal (randn).

from pyspark.sql.functions import rand, randn
df = sqlContext.range(0, 7)
df.show()

By using uniform distribution and normal distribution generate two more columns.

df.select("id", rand(seed=10).alias("uniform"), randn(seed=27).alias("normal")).show()

Summary and Descriptive Statistics
The first operation to perform after importing data is to get some sense of what it looks like.

The function describe returns a DataFrame containing information such as number of non-null entries (count), mean, standard deviation, and minimum and maximum value for each numerical column.

df.describe('uniform', 'normal').show()

Descriptive Statistics
For a quick review of a column describe works fine.

In the same way, we can also make use of some standard statistical functions also.

from pyspark.sql.functions import mean, min, max
df.select([mean('uniform'), min('uniform'), max('uniform')]).show()

Sample Co-Variance and Correlation
In statistics Co-Variance means how one random variable changes with respect to other.

Positive value indicates a trend in increase when the other increases.

Negative value indicates a trend in decrease when the other increases.

from pyspark.sql.functions import rand
df = sqlContext.range(0, 10).withColumn('rand1', rand(seed=10)).withColumn('rand2', rand(seed=27))
df.stat.cov('rand1', 'rand2')

Correlation provides the statistical dependence of two random variables.

df.stat.corr('rand1', 'rand2')

Two randomly generated columns have low correlation value.

Cross Tabulation (Contingency Table)
Cross Tabulation provides a frequency distribution table for a given set of variables.

One of the powerful tool in statistics to observe the statistical independence of variables.

# Create a DataFrame with two columns (name, item)
names = ["Alice", "Bob", "Mike"]
items = ["milk", "bread", "butter", "apples", "oranges"]
df = sqlContext.createDataFrame([(names[i % 3], items[i % 5]) for i in range(100)], ["name", "item"])

For applying the cross tabulation we can make use of the crosstab method.

df.stat.crosstab("name", "item").show()

Lab : Write multi column df to a text file.


import pyspark.sql.functions as F

df = sqlContext.createDataFrame([("foo", "bar"), ("baz", None)], 
                            ('a', 'b'))

def myConcat(*cols):
    concat_columns = []
    for c in cols[:-1]:
        concat_columns.append(F.coalesce(c, F.lit("*")))
        concat_columns.append(F.lit(" "))  
    concat_columns.append(F.coalesce(cols[-1], F.lit("*")))
    return F.concat(*concat_columns)

df_text = df.withColumn("combined", myConcat(*df.columns)).select("combined")

df_text.show()

df_text.coalesce(1).write.format("text").option("header", "false").mode("append").save("output.txt")


Spark SQL brings native support for SQL to Spark.

Spark SQL blurs the lines between RDD's and relational tables.

By integrating these powerful features Spark makes it easy for developers to use SQL commands for querying external data with complex analytics, all within in a single application.

We can also pass SQL queries directly to any DataFrame.

For that, we need to create a table from the DataFrame using the registerTempTable method.

After that use sqlContext.sql() to pass the SQL queries.

Apache Hive

The Apache Hive data warehouse software allows reading, writing, and managing large datasets residing in distributed storage and queried using SQL syntax.

Features of Apache Hive
Apache Hive is built on top of Apache Hadoop.

The below mentioned are the features of Apache Hive.

Apache Hive is having tools to allow easy and quick access to data using SQL, thus enables data warehousing tasks such like extract/transform/load (ETL), reporting, and data analysis.
Mechanisms for imposing structure on a variety of data formats.
Access to files stored either directly in Apache HDFS or in other data storage systems such as Apache HBase.

Features Of Apache Hive
Query execution via Apache Tez,Apache Spark, or MapReduce.
A procedural language with HPL-SQL.
Sub-second query retrieval via Hive LLAP, Apache YARN and Apache Slider

Apache Hive provides the standard SQL functionalities, which includes many of the later SQL:2003 and SQL:2011 features for analytics.

We can extend Hive's SQL with the user code by using user-defined functions (UDFs), user-defined aggregates (UDAFs), and user-defined table functions (UDTFs).

Hive comes with built-in connectors for comma and tab-separated values (CSV/TSV) text files, Apache Parquet,Apache ORC, and other formats.

When working with Hive, one must instantiate SparkSession with Hive support, including connectivity to a persistent Hive metastore, support for Hive serdes, and Hive user-defined functions.

How To Enable Hive Support
from os.path import expanduser, join, abspath

from pyspark.sql import SparkSession
from pyspark.sql import Row

#warehouse_location points to the default location for managed databases and tables

warehouse_location = abspath('spark-warehouse')

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration example") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

Creating Hive Table From Spark
We can easily create a table in hive warehouse programmatically from Spark.

The syntax for creating a table is as follows:

spark.sql("CREATE TABLE IF NOT EXISTS table_name(column_name_1 DataType,column_name_2 DataType,......,column_name_n DataType) USING hive")

To load a DataFrame into a table.

df.write.insertInto("table name",overwrite = True)

External tables are used to store data outside the hive.
Data needs to remain in the underlying location even after the user drop the table.

Handling External Hive Tables From Apache Spark
First, create an external table in the hive by specifying the location.

One can create an external table in the hive by running the following query on hive shell.

hive> create external table table_name(column_name1 DataType,column_name2 DataType,......,column_name_n DataType) STORED AS Parquet location ' path of external table';

The table is created in Parquet schema.
The table is saved in the hdfs directory.

Loading Data From Spark To The Hive Table
We can load data to hive table from the DataFrame.

For doing the same schema of both hive table and the DataFrame should be equal.

Let us take a sample CSV file.

We can read the csv the file by making use of spark csv reader.

df = spark.read.csv("path-of-file", inferSchema = True, header = True)
The schema of the DataFrame will be same as the schema of the CSV file itself.

Data Loading To External Table
For loading the data we have to save the dataframe in external hive table location.

df.write.mode('overwrite').format("format").save("location")
Since our hive external table is in parquet format in place of format we have to mention 'parquet'.

The location should be same as the hive external table location in hdfs directory.

If the schema is matching then data will load automatically to the hive table.

HBASE 

HBase is a distributed column-oriented data store built on top of HDFS.

HBase is an Apache open source project whose goal is to provide storage for the Hadoop Distributed Computing.

Data is logically organized into tables, rows and columns.

HBase features compression, in-memory operation, and Bloom filters on a per-column basis as outlined in the original Bigtable paper.
Tables in HBase can serve as the input and output for Map Reduce jobs run in Hadoop, and may be accessed through the Java API but also through REST, Avro or Thrift gateway APIs.
It is a column-oriented key-value data store and has been idolized widely because of its lineage with Hadoop and HDFS.
HBase runs on top of HDFS and is well-suited for faster read and write operations on large datasets with high throughput and low input/output latency.

How To Connect Spark and HBase
To connect we require hdfs,Spark and HBase installed in the local machine.
Make sure that your versions are matching with each other.
Copy all the HBase jar files to the Spark lib folder.
Once done set the SPARK_CLASSPATH in spark-env.sh with lib.

Real time pipeline using HBASE

It has 4 main stages which includes:

Transformation
Cleaning
Validation
Writing of the data received from the various sources

Data Transformation

This is an entry point for the streaming application.
Here the operations related to normalization of data are performed.
Transformation of data can be performed by using built-in functions like map, filter, foreachRDD etc.

Data Cleaning

During preprocessing cleaning is very important.
In this stage, we can use custom built libraries for cleaning the data

Data Validation

In this stage, we can validate the data with respect to some standard validations such as length, patterns and so on.

Writing

At last, data passed from the previous three stages is passed on to the writing application which simply writes this final set of data to HBase for further data analysis.

Spark In Real World
Uber – the online taxi company is an apt example for Spark. They are gathering terabytes of event data from its various users.

Uses Kafka, Spark Streaming, and HDFS, to build a continuous ETL pipeline.
Convert raw unstructured data into structured data as it is collected.
Uses it further complex analytics and optimization of operations.

Pinterest – Uses a Spark ETL pipeline

Leverages Spark Streaming to gain immediate insight into how users all over the world are engaging with Pins in real time.
Can make more relevant recommendations as people navigate the site.
Recommends related Pins.
Determine which products to buy, or destinations to visit.

Conviva – 4 million video feeds per month.

Conviva is using Spark for reducing the customer churn by managing live video traffic and optimizing video streams.
They maintain a consistently smooth high-quality viewing experience.

Capital One – makes use of Spark and data science algorithms for a better understanding of its customers.

Developing the next generation of financial products and services.
Find attributes and patterns of increased probability for fraud.

Netflix – Movie recommendation engine from user data.

User data is also used for content creation.

Final Lab :

Entering PySpark Shell
Enter the pyspark shell:

pyspark

Import the Spark session package:

from __future__ import print_function

from pyspark.sql import *

from pyspark import SparkContext

from pyspark.sql.readwriter import DataFrameWriter

from pyspark.sql import SparkSession

Create the Spark session:

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

Create a DataFrame:

df = spark.createDataFrame([("1","Jack", 22,"Data Science"), ("2","Luke", 21,"Data Analytics"),("3","Leo", 24,"Micro Services"),("4","Mark", 21,"Data Analytics")],["ID", "Name","Age","Area of Intrest"])

Display the schema:

df.printSchema()

Describe the column 'Age', and observe the various statistical parameters:

df.describe('Age').show()

Select the columns ID, Name, and Age, and display the result in descending order:

df.select('ID','Name','Age').orderBy('Name',ascending=False).show()

Stop the Spark environment:

spark.stop()

Exit from the shell:

exit()













'''