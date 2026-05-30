import os
import json

CHAT_FOLDER = "saved_chats"

os.makedirs(
    CHAT_FOLDER,
    exist_ok=True
)

def save_chat(name, messages):

    filepath = os.path.join(
        CHAT_FOLDER,
        f"{name}.json"
    )

    with open(filepath, "w") as f:

        json.dump(messages, f)

def load_chat(name):

    filepath = os.path.join(
        CHAT_FOLDER,
        f"{name}.json"
    )

    if os.path.exists(filepath):

        with open(filepath, "r") as f:

            return json.load(f)

    return []

def get_chat_list():

    chats = []

    for file in os.listdir(CHAT_FOLDER):

        if file.endswith(".json"):

            chats.append(
                file.replace(".json", "")
            )

    chats.sort(reverse=True)

    return chats