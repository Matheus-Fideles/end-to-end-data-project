from src.main.case.datamaster.application.service.respiratory_disease_service import RespiratoryDiseaseService
from src.main.case.datamaster.infrastructure.config.spark_config import get_spark_session
from src.main.case.datamaster.infrastructure.persistence.respiratory_disease_delta_reader import RespiratoryDiseaseDeltaReader
from src.main.case.datamaster.infrastructure.persistence.respiratory_disease_delta_writer import RespiratoryDiseaseDeltaWriter
import os

if __name__ == '__main__':
    api_key = os.getenv("API_KEY")
    secret_key = os.getenv("SECRET_KEY")
    local = os.getenv("LOCALS")
    endpoint_minio = os.getenv("MINIO_ENDPOINT")

    session = get_spark_session(local, secret_key, api_key, endpoint_minio)
    reader = RespiratoryDiseaseDeltaReader(session)
    writer = RespiratoryDiseaseDeltaWriter("/case-postgresql/silver")
    service = RespiratoryDiseaseService(reader, writer)
    service.process_respiratory_disease()


    print("Processo concluido com sucesso!")

