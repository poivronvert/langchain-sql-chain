from langchain_openai import OpenAIEmbeddings
from langchain_google_cloud_sql_pg import PostgresVectorStore

from dotenv import load_dotenv

from connection import engine
from config import settings

load_dotenv()

embeddings = OpenAIEmbeddings(
    api_key=settings.OPENAI_API_LANGCHAIN_KEY,
    model=settings.embedding_model,
    dimensions=settings.dimensions,
)

vector_store = PostgresVectorStore.create_sync(
    engine=engine,
    embedding_service=embeddings,
    table_name=settings.vector_table,
)
