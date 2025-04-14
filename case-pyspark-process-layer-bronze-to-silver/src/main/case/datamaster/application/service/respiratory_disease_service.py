from src.main.case.datamaster.application.expection.respiratory_disease_exception import RespiratoryDiseaseProcessingException
from src.main.case.datamaster.domain.event.respiratory_disease_event import RespiratoryDiseaseEvent
from pyspark.sql.functions import sum
from pyspark.sql.functions import regexp_replace, col
from pyspark.sql.types import DoubleType

class RespiratoryDiseaseService:

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process_respiratory_disease(self):
        try:
            df = self.reader.read("/case-postgresql/bronze")

            df_clean = df.withColumn("paid", regexp_replace("paid", "[.,]", ""))
            df_clean = df_clean.withColumn("paid", col("paid").cast("double") / 100)
            df_clean = df_clean.withColumn("pledged", regexp_replace("pledged", "[.,]", ""))
            df_clean = df_clean.withColumn("pledged", col("pledged").cast("double") / 100)
            df_clean = df_clean.withColumn("settled", regexp_replace("settled", "[.,]", ""))
            df_clean = df_clean.withColumn("settled", col("settled").cast("double") / 100)

            df_grouped = df_clean.groupBy("actioncode").agg(
                sum("paid").alias("total_paid"),
                sum("pledged").alias("total_pledged"),
                sum("settled").alias("total_settled")
            )
            df_grouped = df_grouped.na.drop()
            df_grouped.show()
            self.writer.write(df_grouped)

        except Exception as e:
            raise RespiratoryDiseaseProcessingException(f"Error processing respiratory diseases: {e}")