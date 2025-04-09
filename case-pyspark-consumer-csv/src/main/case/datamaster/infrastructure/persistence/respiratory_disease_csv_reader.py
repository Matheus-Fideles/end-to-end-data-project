from src.main.case.datamaster.application.port.respiratory_disease_reader import RespiratoryDiseaseReader
from src.main.case.datamaster.domain.model.respiratory_disease import RESPIRATORY_DISEASE
import os

class RespiratoryDiseaseCsvReader(RespiratoryDiseaseReader):

    def __init__(self, file_path, spark):
        self.file_path = file_path
        self.spark = spark
        self.bucket_name = os.getenv("BUCKET_NAME")

    def read(self):
        try:
            return (
                self.spark.read
                .schema(RESPIRATORY_DISEASE)
                .option("delimiter", ";")
                .csv(
                    f"s3a://{self.bucket_name}/*.csv",
                    header=True)
            )
        except Exception as e:
            raise RuntimeError(f"Read respiratory disease csv file failed: {e}")
