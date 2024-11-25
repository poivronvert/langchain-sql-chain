import os
import sys
from dotenv import load_dotenv
from pathlib import Path

# 嘗試載入 .env 文件
env_path = Path("./.env")
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

class Settings:
    DATABASE_PROJECT_ID: str = os.getenv("DATABASE_PROJECT_ID", "")
    DATABASE_INSTANCE: str = os.getenv("DATABASE_INSTANCE", "")
    DATABASE_REGION: str = os.getenv("DATABASE_REGION", "")
    DATABASE_DB: str = os.getenv("DATABASE_DB", "")
    DATABASE_USER: str = os.getenv("DATABASE_USER", "")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "")
    OPENAI_API_LANGCHAIN_KEY: str = os.getenv("OPENAI_API_LANGCHAIN_KEY", "")
    VECTOR_TABLE: str = os.getenv("VECTOR_TABLE", "news_vector_table")
    TABLE_NAME: str = os.getenv("TABLE_NAME", "links")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    DIMENSIONS: int = int(os.getenv("DIMENSIONS", 768))
    
    @staticmethod
    def update_from_args(args):
        for key, value in vars(args).items():
            if value:  # 只更新非 None 的值
                setattr(Settings, key.upper(), value)

REQUIRED_ENV_VARS = [
    "DATABASE_PROJECT_ID",
    "DATABASE_INSTANCE",
    "DATABASE_REGION",
    "DATABASE_DB",
    "DATABASE_USER",
    "DATABASE_PASSWORD",
    "OPENAI_API_LANGCHAIN_KEY",
]

def check_required_env_vars():
    missing_vars = []
    for var_name in REQUIRED_ENV_VARS:
        if not getattr(Settings, var_name):
            missing_vars.append(var_name)

    if missing_vars:
        raise ValueError(f"❌ Missing required environment variable: {', '.join(missing_vars)}")

try:        
    check_required_env_vars()
except ValueError as e:
    print(e)    
    sys.exit(1)

settings = Settings()