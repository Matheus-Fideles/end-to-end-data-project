from src.main.case.datamaster.application.port.respiratory_disease_reader import RespiratoryDiseaseReader
import os

class RespiratoryDiseaseDeltaReader(RespiratoryDiseaseReader):

    def __init__(self, spark):
        self.spark = spark
        self.bucket_name = os.getenv("BUCKET_NAME")

    def read(self, folder_path):
        try:
            return (
                self.spark.read
                .format("delta")
                .load( f"s3a://{self.bucket_name}/{folder_path}")
            )
        except Exception as e:
            raise RuntimeError(f"Read respiratory disease delta file failed: {e}")
