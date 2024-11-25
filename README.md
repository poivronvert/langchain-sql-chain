
# Chatbot for Langchain SQL Chain

This chatbot integrates Langchain and LangGraph with Google Cloud SQL PostgreSQL, OpenAI Embeddings, and LLM.

## Features

- Utilizes Langchain for conversational AI.
- Stores documents in a Google Cloud SQL PostgreSQL database.
- Generates embeddings and vector stores for efficient document search and retrieval.
- Provides a chat interface powered by OpenAI's LLMs.

## Setup

### 1. Database Configuration
1. Create a PostgreSQL database in Google Cloud SQL.
2. Create a table to store your documents and ensure you have the table name, vector store table name, and models set up.
3. Modify the `config.py` file to match your database and model configuration.

### 2. Environment Variables
Create a `.env` file or provide the following variables via the command line:
- **DATABASE_PROJECT_ID**: Google Cloud project ID.
- **DATABASE_INSTANCE**: Name of the Cloud SQL instance.
- **DATABASE_REGION**: Region of the Cloud SQL instance.
- **DATABASE_DB**: Name of the database.
- **DATABASE_USER**: Database username.
- **DATABASE_PASSWORD**: Database password.
- **OPENAI_API_LANGCHAIN_KEY**: API key for OpenAI.

Alternatively, refer to `.env.example` for guidance on creating the `.env` file.

## CLI Commands

The chatbot provides the following commands via `argparse`:

### Command Line Arguments
```text
--database_project_id   (required) Database Project ID
--database_instance     (required) Database Instance Name
--database_region       (required) Region of the Database Instance
--database_db           (required) Database Name
--database_user         (required) Database User
--database_password     (required) Database Password
--openai_api_langchain_key (required) OpenAI API Key
--vector_table          (optional) Vector Table Name (default: "news_vector_table")
--table_name            (optional) Document Table Name (default: "links")
--embedding_model       (optional) Embedding Model Name (default: "text-embedding-3-small")
--llm_model             (optional) LLM Model Name (default: "gpt-4o-mini")
--dimensions            (optional) Embedding Dimensions (default: 768)
```

### Commands
1. **Initialize Vector Store Table**  
   ```bash
   lanchainsql initvec
   ```
   Creates the vector store table in your database.

2. **Load Documents**  
   ```bash
   lanchainsql loaddoc
   ```
   Loads all documents from the document table into the vector store.

3. **Start Chat Interface**  
   ```bash
   lanchainsql chat
   ```
   Launches an interactive chat interface for querying your database.

## Installation and Usage

1. Install dependencies:
   ```bash
   poetry install
   ```
2. Activate the virtual environment:
   ```bash
   poetry shell
   ```
3. Run the commands as described in the CLI section above.

## Example Workflow
1. Initialize the vector store table:
   ```bash
   lanchainsql initvec --database_project_id <PROJECT_ID> --database_instance <INSTANCE> ...
   ```
2. Load documents into the vector store:
   ```bash
   lanchainsql loaddoc --table_name <TABLE_NAME>
   ```
3. Start a chat session:
   ```bash
   lanchainsql chat --llm_model <MODEL_NAME>
   ```

## References

1. [Google Cloud SQL for PostgreSQL](https://python.langchain.com/docs/integrations/vectorstores/google_cloud_sql_pg/#-set-your-google-cloud-project)
2. [Managing Message History in Langchain](https://python.langchain.com/docs/how_to/message_history/#managing-message-history)