@dataclass
class Tools:
    """Functions AKA Tools to be used by Retriever class. These could range from a simple Calculator to Web Scraping, Search, etc."""

    @classmethod
    def multiplier(cls, num1: int, num2: int):
        """Simple Fake Calculator for testing"""
        return num1 * num2
