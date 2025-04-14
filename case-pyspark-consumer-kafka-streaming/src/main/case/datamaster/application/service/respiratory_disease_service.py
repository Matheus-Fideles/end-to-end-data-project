from src.main.case.datamaster.application.expection.respiratory_disease_exception import RespiratoryDiseaseProcessingException
from src.main.case.datamaster.domain.event.respiratory_disease_event import RespiratoryDiseaseEvent


class RespiratoryDiseaseService:

    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process_respiratory_disease(self):
        try:
            df = self.reader.read("cdc.public.respiratorydisease")

            query = self.writer.write(df)

            print("Monitoring Kafka Topic...")
            while query.isActive:
                try:
                    query.status
                except Exception as e:
                    print(f"Err: {e}")
                    query.stop()
                    break

        except Exception as e:
            raise RespiratoryDiseaseProcessingException(f"Error processing respiratory diseases: {e}")