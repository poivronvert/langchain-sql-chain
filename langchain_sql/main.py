import argparse
import asyncio

from langchain_sql import config, connection, document_loader, chat

def initvec():
    connection.init_vectorstore_table()
    print("Vector store table initialized.")

async def loaddoc():
    await document_loader.load_documents()
    print("Documents loaded into vector store.")

def chat_interface():
    chat.start_chat()
    print("Chat interface started.")

def main():
    parser = argparse.ArgumentParser(description="langchainsql CLI")
    parser.add_argument("--database_project_id", help="Database Project ID")
    parser.add_argument("--database_instance", help="Database Instance")
    parser.add_argument("--database_region", help="Database Region")
    parser.add_argument("--database_db", help="Database DB")
    parser.add_argument("--database_user", help="Database User")
    parser.add_argument("--database_password", help="Database Password")
    parser.add_argument("--openai_api_langchain_key", help="OpenAI API Key")
    parser.add_argument("--vector_table", help="Vector Table Name", default="news_vector_table")
    parser.add_argument("--table_name", help="Table Name", default="links")
    parser.add_argument("--embedding_model", help="Embedding Model", default="text-embedding-3-small")
    parser.add_argument("--llm_model", help="LLM Model", default="gpt-4o-mini")
    parser.add_argument("--dimensions", type=int, help="Embedding Dimensions", default=768)
    
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 初始化 vec db
    parser_initvec = subparsers.add_parser("initvec", help="Initialize the vector store table.")
    parser_initvec.set_defaults(func=initvec)

    # 載入文件
    parser_loaddoc = subparsers.add_parser("loaddoc", help="Load documents into the vector store.")
    parser_loaddoc.set_defaults(func=lambda: asyncio.run(loaddoc()))

    # 啟動對話
    parser_chat = subparsers.add_parser("chat", help="Start the chat interface.")
    parser_chat.set_defaults(func=chat_interface)

    args = parser.parse_args()

    # 更新 Settings 類別中的值
    config.Settings.update_from_args(args)

    args.func()

if __name__ == "__main__":
    main()
