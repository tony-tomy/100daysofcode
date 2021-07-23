from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *


if __name__ == "__main__":
    sc = SparkContext(appName="CSV2Parquet")
    sqlContext = SQLContext(sc)
    
    schema = StructType([
            StructField("Date", StringType(), True),
            StructField("Gender", StringType(), True),
            StructField("Race", StringType(), True),
            StructField("Age_at_Booking", IntegerType(), True),
            StructField("Current_Age", IntegerType(), True),
            StructField("DeltaAge", IntegerType(), True)])
    
    rdd = sc.textFile("file_name.csv").map(lambda line: line.split(","))
    df = sqlContext.createDataFrame(rdd, schema)
    df.write.parquet('release_list')