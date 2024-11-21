from memory import app

config = {"configurable": {"thread_id": "abc123"}}

result = app.invoke(
    {"input": "Xybion最新的產品是什麼？能帶來什麼效益？"},
    config=config,
)

result = app.invoke(
    {"input": "和Pristima Web有什麼關係？"},
    config=config1,
)

# print(result["answer"])



chat_history = app.get_state(config).values["chat_history"]
for message in chat_history:
    message.pretty_print()

