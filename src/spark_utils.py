"""
Spark session utilities for MLApp pipeline.
"""
from pyspark.sql import SparkSession


$ Your version of get_spark_session()
def get_spark_session(app_name="MLApp"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.shuffle.partitions", "400") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.default.parallelism", "400") \
        .getOrCreate()
    return spark


def stop_spark_session(spark):
    """Cleanly stop the Spark session."""
    if spark is not None:
        spark.stop()
