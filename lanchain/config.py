import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_PROJECT_ID:str=os.environ.get("DATABASE_PROJECT_ID")
    DATABASE_INSTANCE=os.environ.get("DATABASE_INSTANCE")
    DATABASE_REGION:str=os.environ.get("DATABASE_REGION")
    DATABASE_DB:str=os.environ.get("DATABASE_DB")
    DATABASE_USER:str=os.environ.get("DATABASE_USER")
    DATABASE_PASSWORD:str=os.environ.get("DATABASE_PASSWORD")
    OPENAI_API_LANGCHAIN_KEY = os.environ.get("OPENAI_API_LANGCHAIN_KEY")
    vector_table = "news_vector_table"
    table_name = "links"
    embedding_model = "text-embedding-3-small"
    llm_model = "gpt-4o-mini"
    dimensions = 768
    
settings = Settings()