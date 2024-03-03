from typing import Any, ClassVar, Dict
from dataclasses import dataclass
from app.memory.memory import Memory as C_Memory
from app.cli.output import Output as M_Output
from app.config.config import Config
from rich import print as rprint


@dataclass
class Chat:
    """Master Chat class to make calls to External AI APIs"""

    client = Config.client
    logging = Config.logging

    @classmethod
    def chat_api(cls, user_message: str, config: Dict[str, Any] = {}):
        """Query the AI for a response"""
        api = config.get("api")
        model = config.get("model")
        sys_message = config.get("sys_message")
        temperature = config.get("temperature")
        max_tokens = config.get("max_tokens")

        # Set the system message in Memory
        if len(C_Memory.chat_history) == 0:
            C_Memory.set_sys_message(sys_message)

        # Add the latest user message to the conversation history
        C_Memory.add_message_to_context("user", user_message)
        # Add user's message to the save to database
        C_Memory.add_message_to_db("user", user_message)

        # Retrieve the conversation history from Memory
        chat_history = C_Memory.chat_history.copy()

        rprint("chat_history", chat_history)

        # Query the OpenAI API
        chat_completion = cls.client.chat.completions.create(
            model=model,
            messages=chat_history,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        assistant_message = chat_completion.choices[0].message.content

        # Add the assistant's response to the conversation history
        C_Memory.add_message_to_context("assistant", assistant_message)
        # Add assistant's response to the save to database
        C_Memory.add_message_to_db("assistant", assistant_message)

        M_Output.cli_out(assistant_message)
        # rprint(Panel(json.dumps(session_chat_history, indent=2)))

        # Return the assistant's response
        return assistant_message
