import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def login(username, password):

    return (
        username == USERNAME
        and password == PASSWORD
    )