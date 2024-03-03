from dataclasses import dataclass
from typing import Any, Dict
import logging


@dataclass
class Retrievers:
    """Interface for retrieving Memories and for calling tools aka Functions"""

    @classmethod
    def get_memory(cls):
        """Get Memory from Memory class"""
        pass

    @classmethod
    def use_tool(cls, tool: str, params: Dict[str, Any] = {}):
        """Use a Tool from Tools class"""
        if tool == "multiplier":
            tool_result = Tools.multiplier(params["num1"], params["num2"])
            logging.info(f"Result from using tool: {tool_result}")
