from src.main.case.datamaster.application.port.respiratory_disease_reader import RespiratoryDiseaseReader
import os


class RespiratoryDiseaseKafkaReader(RespiratoryDiseaseReader):

    def __init__(self, spark):
        self.spark = spark
        self.bootstrap_server = os.getenv("BOOTSTRAP_SERVER")

    def read(self, topic_name):
        try:

            df = (
                self.spark.readStream
                .format("kafka")
                .option("kafka.bootstrap.servers", self.bootstrap_server)
                .option("subscribe", topic_name)
                .option("startingOffsets", "earliest")
                .option("kafka.client.dns.lookup", "use_all_dns_ips")
                .load()
            )

            df_json = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
            return df_json

        except Exception as e:
            raise RuntimeError(f"Read respiratory disease kafka failed: {e}")
