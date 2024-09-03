# Databricks notebook source
# Import necessary libraries
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, monotonically_increasing_id

# Initialize Spark Session
spark = SparkSession.builder.appName("CustomerDuplicateIdentification").getOrCreate()

# Sample Customer Data
data = {
    "CustomerID": [1, 2, 3, 4, 5, 6],
    "Name": ["Sourabh", "Sahil Gupta", "Sourabh", "Raj Sharma", "Sahil Gupta", "Sourabh"],
    "Address": ["123 Elm St", "456 Oak St", "123 Elm St", "789 Pine St", "456 Oak St", "123 Elm St"]
}

# Create DataFrame
customer_df = pd.DataFrame(data)

# Convert to Spark DataFrame
customer_sdf = spark.createDataFrame(customer_df)

# Display the DataFrame
customer_sdf.show()


# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

# Create a window specification
window_spec = Window.partitionBy("Name", "Address").orderBy("CustomerID")

# Add a row number to each group of duplicates
customer_sdf = customer_sdf.withColumn("row_num", row_number().over(window_spec))

# Display the DataFrame with row numbers
customer_sdf.show()


# COMMAND ----------

# Assign Master ID
customer_sdf = customer_sdf.withColumn("MasterID", monotonically_increasing_id())

# Create a MasterID mapping based on the first occurrence of each group
master_id_mapping = customer_sdf.filter(col("row_num") == 1).select("Name", "Address", "MasterID")

# Join the original DataFrame with the MasterID mapping
enriched_df = customer_sdf.join(master_id_mapping, on=["Name", "Address"], how="left")\
    .drop("MasterID")\
    .withColumnRenamed("MasterID_right", "MasterID")\
    .drop("row_num")

# Display the enriched DataFrame
enriched_df.show()

# COMMAND ----------

jdbc_url = "jdbc:sqlserver://<your_server>.database.windows.net:1433;database=<your_database_name>"
jdbc_properties = {
    "user": "<your_username>",
    "password": "<your_password>",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

