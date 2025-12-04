import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("EmployeeData").getOrCreate()
print(spark.version)