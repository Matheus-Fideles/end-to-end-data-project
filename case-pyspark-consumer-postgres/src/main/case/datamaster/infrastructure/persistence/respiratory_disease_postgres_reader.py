from src.main.case.datamaster.application.port.respiratory_disease_reader import RespiratoryDiseaseReader
import os

class RespiratoryDiseasePostgresReader(RespiratoryDiseaseReader):

    def __init__(self, spark):
        self.spark = spark

    def read(self):
        try:
            url = os.getenv("DATABASE_URL")
            properties = {
                "user": os.getenv("DATABASE_USER_NAME"),
                "password": os.getenv("DATABASE_PASSWORD"),
                "driver": "org.postgresql.Driver"
            }

            return (
                self.spark.read
                .jdbc(
                    url=f"{url}", #jdbc:postgresql://localhost:5432/gov
                    table="respiratorydiseases",
                    properties=properties)
            )
        except Exception as e:
            raise RuntimeError(f"Read respiratory disease PostgreSQL file failed: {e}")
