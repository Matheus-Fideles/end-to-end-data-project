from pyspark.sql import SparkSession
from delta import *


def get_spark_session(local, secret_key, api_key, endpoint):
    return (configure_spark_with_delta_pip(
        SparkSession.builder.appName("respiratory_disease_postgres")
        .master(local)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.memory.fraction", "0.8")
        .config("spark.driver.memory", "4g")
        .config("spark.executor.memory", "4g")
        .config("spark.sql.shuffle.partitions", "800")
        .config("spark.memory.offHeap.enabled", "true")
        .config("spark.memory.offHeap.size", "4g")
        .config("spark.executor.heartbeatInterval", "300s")
        .config("spark.network.timeout", "600s")
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
        .config("spark.hadoop.fs.s3a.endpoint", endpoint)
        .config("spark.hadoop.fs.s3a.access.key", api_key)
        .config("spark.hadoop.fs.s3a.secret.key", secret_key)
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
        .config("spark.jars", "../../../../jars/hadoop-mapreduce-client-core-3.2.4.jar,"
                              "../../../../jars/hadoop-common-3.2.4.jar,"
                              "../../../../jars/hadoop-aws-3.2.4.jar,"
                              "../../../../jars/postgresql-42.7.5.jar,"
                              "../../../../jars/aws-java-sdk-bundle-1.11.901.jar")
        ).getOrCreate())

