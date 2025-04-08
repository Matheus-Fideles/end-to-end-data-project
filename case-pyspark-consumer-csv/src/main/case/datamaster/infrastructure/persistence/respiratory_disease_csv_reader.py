from src.main.case.datamaster.application.port.respiratory_disease_reader import RespiratoryDiseaseReader
from src.main.case.datamaster.domain.model.respiratory_disease import RESPIRATORY_DISEASE


class RespiratoryDiseaseCsvReader(RespiratoryDiseaseReader):

    def __init__(self, file_path, spark):
        self.file_path = file_path
        self.spark = spark

    def read(self):
        try:
            return (
                self.spark.read
                .schema(RESPIRATORY_DISEASE)
                .option("delimiter", ";")
                .csv(
                    self.file_path,
                    header=True)
            )
        except Exception as e:
            raise BufferError(f"Read respiratory disease csv file failed: {e}")
