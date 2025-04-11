import os

from src.main.case.datamaster.application.port.respiratory_disease_writer import RespiratoryDiseaseWriter


class RespiratoryDiseasePostgresWriter(RespiratoryDiseaseWriter):

    def __init__(self):
        self.bucket_name = os.getenv("BUCKET_NAME")

    def write(self, df):
        try:
            df.write.format("delta").mode("overwrite").save(f"s3a://{self.bucket_name}/case-postgresql/bronze",)
        except Exception as e:
            raise RuntimeError(f"Writer respiratory disease delta file failed: {e}")