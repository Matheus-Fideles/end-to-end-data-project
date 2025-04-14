import os

from src.main.case.datamaster.application.port.respiratory_disease_writer import RespiratoryDiseaseWriter


class RespiratoryDiseaseDeltaWriter(RespiratoryDiseaseWriter):

    def __init__(self, file_path):
        self.file_path = file_path
        self.bucket_name = os.getenv("BUCKET_NAME")

    def write(self, df):
        try:
            df.write.format("delta").mode("overwrite").save(f"s3a://{self.bucket_name}/case-postgresql/silver",)
        except Exception as e:
            raise RuntimeError(f"Writer respiratory disease delta file failed: {e}")