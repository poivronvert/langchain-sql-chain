from langchain_google_cloud_sql_pg import PostgresLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import uuid
import asyncio

from store import vector_store
from connection import engine
from config import settings

table_name = settings.table_name

async def load_documents():
    loader = await PostgresLoader.create(engine=engine, query=f"SELECT id::TEXT AS id,text FROM {table_name} WHERE created_at::DATE = CURRENT_DATE", content_columns=["text",], metadata_columns=["id"])
    docs = await loader.aload()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    split = text_splitter.split_documents(docs)
    docs_to_load = split

    ids = [str(uuid.uuid4()) for i in range(len(docs_to_load))]
    vector_store.add_documents(docs_to_load, ids)

if __name__ == "__main__":
    asyncio.run(load_documents())