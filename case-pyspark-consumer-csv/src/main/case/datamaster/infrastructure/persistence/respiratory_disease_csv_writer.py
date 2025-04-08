from src.main.case.datamaster.application.port.respiratory_disease_writer import RespiratoryDiseaseWriter


class RespiratoryDiseaseCsvWriter(RespiratoryDiseaseWriter):

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, df):
        try:
            df.write.format("delta").mode("overwrite").save(self.file_path)
        except Exception as e:
            raise Exception(f"Writer respiratory disease delta file failed: {e}")