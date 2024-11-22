import sys
from memory import app

human_inputs = []
thread_id = "abc123"

def create_chat(thread_id, human_input):
    config = {"configurable": {"thread_id": thread_id}}
    result = app.invoke({"input": human_input}, config)
    print(result["answer"])

def append_and_create_chat():
    new_input = input("Enter your input (or type 'exit' to quit): ")
    if new_input.lower() == 'exit':
        sys.exit(0)
    create_chat(thread_id, new_input)

while True:
    append_and_create_chat()
