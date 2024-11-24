from langchain_google_cloud_sql_pg import PostgresLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import uuid
import asyncio

from vector_data_store import vector_store
from connection import engine
from database_config import settings

table_name = settings.table_name

async def load_documents():
    """
    Loads all documents from the database that were created today and adds them
    to the vector store. The documents are split into chunks of 1000 characters
    with a 50 character overlap. A new id is generated for each chunk and the
    chunks are added to the vector store.
    """
    loader = await PostgresLoader.create(engine=engine, query=f"SELECT id::TEXT AS id,text FROM {table_name} AS t WHERE created_at::DATE = CURRENT_DATE AND NOT EXISTS (SELECT 1 FROM {table_name} AS existing WHERE existing.id = t.id)", content_columns=["text",], metadata_columns=["id"])
    docs = await loader.aload()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    split = text_splitter.split_documents(docs)
    docs_to_load = split

    ids = [str(uuid.uuid4()) for i in range(len(docs_to_load))]
    vector_store.add_documents(docs_to_load, ids)

if __name__ == "__main__":
    asyncio.run(load_documents())