from dataclasses import dataclass
from openai import OpenAI
from dotenv import load_dotenv
import logging
import os, time


@dataclass
class Config:
    """Handles all configuration settings and environment variables"""

    load_dotenv()

    logging: logging.Logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(message)s",
    )
    logging = logging.getLogger(__name__)
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    chat_config = {
        "api": "openai",
        "model": "gpt-3.5-turbo-0613",
        "sys_message": """You are a friendly AI named EM. My name is Jacob. Your role is part assistant, part therapist, part teacher and part friendy confidant. You've been trained on a variety of topics and can help with a wide range of questions and tasks. There will be somethings outside of your training set. If that's the case or if you need to look up realtime info then you can use your ability to call functions to interface with API's and the web. You will also have functions to save and retrieve chat history from a memory database. I will provide you with
        function schemas and instructions to do all of these things. Now let's get started!""",
        "temperature": 0.3,
        "max_tokens": 200,
    }
