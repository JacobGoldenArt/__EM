from app.config.config import Config
from rich import print as rprint
from rich.panel import Panel
from dataclasses import dataclass

logging = Config.logging


@dataclass
class Output:
    """Handles all output from AI, text, voice, filesaving, etc."""

    @classmethod
    def cli_out(cls, response: str):
        """Command Line Output from AI"""
        rprint(f"\nAI: {response}")

    @classmethod
    def voice_out(cls):
        """Voice Output from AI"""
        pass

    @classmethod
    def file_out(cls):
        """File Output from AI"""
        pass
