# Chatbot for Lanchain SQL Chain

This chatbot integrates Langchain and LangGraph with Google Cloud SQL Postgres and OpenAI Embeddings and LLM.

## Setup

1. Run `poetry install` to install the dependencies.
2. Create a Postgres database in Google Cloud SQL and create a table where stores your documents.
3. Change the names of the table and the vector table and models in `config.py` to match your setup.
4. Create a `.env` file with the following variables or follow `.env.example`:
   - DATABASE_PROJECT_ID
   - DATABASE_INSTANCE
   - DATABASE_REGION
   - DATABASE_DB
   - DATABASE_USER
   - DATABASE_PASSWORD
   - OPENAI_API_LANGCHAIN_KEY
5. Run `python lanchain/connection.py` to create the vector store table.
6. Run `python lanchain/loader.py` to load all documents from the table into the vector store. Note: it is set only to load today's documents. Change the parameters such as `query`, `content`, `metadata_columns` as appropriate.

## Usage

1. Run `python lanchain/chat.py` to start a chat interface.
2. Type a message and press enter to get a response.
3. Type 'exit' to quit.

## Reference

1. [Google Cloud SQL for PostgreSQL](https://python.langchain.com/docs/integrations/vectorstores/google_cloud_sql_pg/#-set-your-google-cloud-project)
2. [How to add message history](https://python.langchain.com/docs/how_to/message_history/#managing-message-history)