from pyspark.sql import SparkSession
from delta import *


def get_spark_session():
    return (configure_spark_with_delta_pip(
        SparkSession.builder.appName("respiratory_disease")
        .master("local[*]")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.memory.fraction", "0.8")
        .config("spark.driver.memory", "4g")
        .config("spark.executor.memory", "4g")
        .config("spark.sql.shuffle.partitions", "800")
        .config("spark.memory.offHeap.enabled", "true")
        .config("spark.memory.offHeap.size", "4g")
    ).getOrCreate())
