from src.main.case.datamaster.application.service.respiratory_disease_service import RespiratoryDiseaseService
from src.main.case.datamaster.infrastructure.config.spark_config import get_spark_session
from src.main.case.datamaster.infrastructure.persistence.respiratory_disease_postgres_reader import RespiratoryDiseasePostgresReader
from src.main.case.datamaster.infrastructure.persistence.respiratory_disease_postgres_writer import RespiratoryDiseasePostgresWriter
import os

if __name__ == '__main__':
    api_key = os.getenv("API_KEY")
    secret_key = os.getenv("SECRET_KEY")
    local = os.getenv("LOCALS")
    endpoint_minio = "http://localhost:9000"

    url = os.getenv("DATABASE_URL")
    properties = {
        "user": os.getenv("DATABASE_USER_NAME"),
        "password": os.getenv("DATABASE_PASSWORD"),
        "driver": "org.postgresql.Driver"
    }

    session = get_spark_session(local, secret_key, api_key, endpoint_minio)
    reader = RespiratoryDiseasePostgresReader(session)
    writer = RespiratoryDiseasePostgresWriter()
    service = RespiratoryDiseaseService(reader, writer)
    service.process_respiratory_disease()

    print("Processo concluido com sucesso!")

