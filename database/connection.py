from langchain_google_cloud_sql_pg import PostgresEngine
from config import settings

engine = PostgresEngine.from_instance(
    project_id=settings.DATABASE_PROJECT_ID,
    region=settings.DATABASE_REGION,
    instance=settings.DATABASE_INSTANCE,
    database=settings.DATABASE_DB,
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD
)

if __name__ == "__main__":
    engine.init_vectorstore_table(table_name=settings.vector_table, vector_size=768)