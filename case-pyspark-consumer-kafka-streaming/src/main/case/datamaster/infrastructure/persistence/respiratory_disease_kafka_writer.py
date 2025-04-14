import os
from src.main.case.datamaster.application.port.respiratory_disease_writer import RespiratoryDiseaseWriter


class RespiratoryDiseaseKafkaWriter(RespiratoryDiseaseWriter):

    def __init__(self, file_path):
        self.file_path = file_path
        self.bucket_name = os.getenv("BUCKET_NAME")

    def write(self, df):
        try:
            query = (df.writeStream
                     .outputMode("append")
                     .format("delta")
                     .option("path", f"s3a://{self.bucket_name}/case-kafka/bronze")
                     .option("checkpointLocation", f"s3a://{self.bucket_name}/case-kafka/bronze/checkpoint")
                     .trigger(processingTime="10 seconds")
                     .start())
            print("Writing to s3")

            return query
        except Exception as e:
            raise RuntimeError(f"Writer respiratory disease delta file failed: {e}")
