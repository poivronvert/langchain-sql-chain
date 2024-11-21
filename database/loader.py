from langchain_google_cloud_sql_pg import PostgresLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import uuid
import asyncio

from store import vector_store
from connection import engine

table_name = "links"

async def load_documents():
    loader = await PostgresLoader.create(engine=engine, query=f"SELECT id::TEXT AS id,text FROM {table_name} WHERE created_at::DATE = CURRENT_DATE", content_columns=["text",], metadata_columns=["id"])
    docs = await loader.aload()
    docs_to_load = docs

    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    # docs_to_load = text_splitter.split_documents(docs)
    # print(len(docs_to_load))
    ids = [str(uuid.uuid4()) for i in range(len(docs_to_load))]
    vector_store.add_documents(docs_to_load, ids)

if __name__ == "__main__":
    asyncio.run(load_documents())