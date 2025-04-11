from pyspark.sql import SparkSession
from pyspark.sql.functions import base64 as spark_base64, col
from src.main.case.datamaster.application.expection.respiratory_disease_exception import \
    RespiratoryDiseaseProcessingException
from src.main.case.datamaster.domain.event.respiratory_disease_event import RespiratoryDiseaseEvent


class RespiratoryDiseaseService:

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process_respiratory_disease(self):
        try:
            df = self.reader.read()

            df_anonymized = df.withColumn("subfunctioncode", spark_base64(col("subfunctioncode")))
            # df_decoded = df_encoded.withColumn("subfunctioncode", unbase64(col("subfunctioncode")).cast("string"))

            self.writer.write(df_anonymized)

            RespiratoryDiseaseEvent.log("respiratory disease successfully filtered and saved!")

        except Exception as e:
            raise RespiratoryDiseaseProcessingException(f"Error processing respiratory diseases: {e}")
