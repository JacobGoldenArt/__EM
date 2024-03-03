from fastapi import FastAPI, Request
from typing import Dict, Any
from dataclasses import dataclass
from app.chat.chat import Chat as A_Chat
from app.config.config import Config

logging = Config.logging

@dataclass
class Api:
    """All FastAPI Endpoints to interact with Chat class"""

    # @app.get("/")
    # def read_root():
    #     return {"Hello": "World"}

    # @app.post("/chat")
    # non fastapi version for local development
    @classmethod
    def query_chat(cls, user_message: str, config: Dict[str, Any] = {}):
        logging.info("API received User Message")
        A_Chat.chat_api(user_message, config)
