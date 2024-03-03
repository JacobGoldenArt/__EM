from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.messages_db import SessionLocal, Message, ChatSession
from app.config.config import Config
from typing import List, Dict, ClassVar
import time, sys, os, json

logging = Config.logging


@dataclass
class Memory:
    """Handles all chat history, summarization, keyword extraction, and saving to both Standard and Vector Database"""

    session_id: ClassVar[str] = time.strftime("%Y%m%d-%H%M%S")

    chat_history: ClassVar[List[Dict[str, str]]] = []

    @classmethod
    def set_sys_message(cls, sys_message: str):
        cls.chat_history.append({"role": "system", "content": sys_message})
        # Add the system message to the database
        cls.add_message_to_db("system", sys_message)

    @classmethod
    def add_message_to_context(cls, role: str, content: str):
        cls.chat_history.append({"role": role, "content": content})

    @classmethod
    def add_message_to_db(cls, role: str, content: str):
        """Add a message to the chat history"""
        with SessionLocal() as db_session:  # Automatically disposes the session after use
            logging.info("Saving to database...")
            new_message = Message(
                session_id=cls.session_id,  # Ensure this is the ID of the current chat session
                role=role,
                content=content,
            )
            db_session.add(new_message)
            db_session.commit()  # The session is not closed here, it's just committed
            logging.info("Saved to database")
