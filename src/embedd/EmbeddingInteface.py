from typing import List

from src.embedd.EmbeddedModel import EmbeddedModel
from src.crawler.SourceData import SourceData

class EmbeddingInterface:
    """
    Interface for embedding class
    You have to implement this method when you make a new embedding class.
    """
    
    def embed(self, data: SourceData) -> EmbeddedModel:
        """
        Embedding text data into vector

        Args:
            text_data (SourceData): SourceData to be embedded
        """
        pass
    
    
    def embed_simple_text(self, text: str) -> List[float]:
        """
        Embedding text data into vector

        Args:
            text_data (SourceData): SourceData to be embedded
        """
        pass