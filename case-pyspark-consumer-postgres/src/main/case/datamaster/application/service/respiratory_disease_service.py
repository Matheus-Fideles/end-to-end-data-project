from src.main.case.datamaster.application.expection.respiratory_disease_exception import RespiratoryDiseaseProcessingException
from src.main.case.datamaster.domain.event.respiratory_disease_event import RespiratoryDiseaseEvent


class RespiratoryDiseaseService:

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process_respiratory_disease(self):
        try:
            df = self.reader.read()

            self.writer.write(df)

            RespiratoryDiseaseEvent.log(f"respiratory disease successfully filtered and saved! ")

        except Exception as e:
            raise RespiratoryDiseaseProcessingException(f"Error processing respiratory diseases: {e}")