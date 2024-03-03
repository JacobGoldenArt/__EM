from app.api.api import Api as C_Api
from app.memory.memory import Memory as C_Memory
from app.config.config import Config
from dataclasses import dataclass

logging = Config.logging


@dataclass
class Input:
    """Handles all input from user, text, voice, file, etc."""

    @classmethod
    def cli_in(cls):
        while True:
            user_message = input("You: ")
            if user_message.lower() in ["exit", "bye"]:
                C_Memory.end_session()
                break
            else:
                C_Api.query_chat(user_message, Config.chat_config)

    @classmethod
    def voice_in(cls):
        """Voice Input from user"""
        pass

    @classmethod
    def file_in(cls):
        """File Input from user"""
        pass
