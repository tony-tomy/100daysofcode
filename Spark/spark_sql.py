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






'''