from src.main.case.datamaster.application.service.respiratory_disease_service import RespiratoryDiseaseService
from src.main.case.datamaster.infrastructure.config.spark_config import get_spark_session
from src.main.case.datamaster.infrastructure.persistence.respiratory_disease_csv_reader import RespiratoryDiseaseCsvReader
from src.main.case.datamaster.infrastructure.persistence.respiratory_disease_csv_writer import RespiratoryDiseaseCsvWriter
import os

if __name__ == '__main__':
    input_file_path = os.getenv("INPUT_FILE_PATH")
    output_file_path = os.getenv("OUTPUT_FILE_PATH")


    input_file='C:\\case_data_master\\end-to-end-data-project\\docs\\*.csv'
    output_file="C:\\case_data_master\\end-to-end-data-project\\docs\\result"
    session = get_spark_session()
    reader = RespiratoryDiseaseCsvReader(input_file_path, session)
    writer = RespiratoryDiseaseCsvWriter(output_file_path)
    service = RespiratoryDiseaseService(reader, writer)
    service.process_respiratory_disease()


    print("Processo concluido com sucesso!")

