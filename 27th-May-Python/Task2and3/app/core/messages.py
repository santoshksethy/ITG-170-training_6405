import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MESSAGE_FILE = os.path.join(BASE_DIR, "messages.json")

with open(MESSAGE_FILE, "r") as f:
    MESSAGES = json.load(f)


def get_message(key: str) -> str:
    return MESSAGES.get(key, "Message not found")