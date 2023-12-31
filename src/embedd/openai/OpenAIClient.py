import os
from typing import List
import openai

from src.embedd.EmbeddedModel import EmbeddedModel
from src.embedd.EmbeddingInteface import EmbeddingInterface
from src.crawler.SourceData import SourceData

class OpenAIClient(EmbeddingInterface):
    
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_EMBEDDING_MODEL")
        pass
    
    
    def embed(self, data: SourceData) -> EmbeddedModel:
        """
        Embedding text data into vector using OpenAI Embedding API

        Args:
            data (SourceData): SourceData to be embedded

        Returns:
            EmbeddedModel: EmbeddedModel
        """
        
        text_data = data.text
        data_ref = data.ref
        
        embedded = self.embed_simple_text(text_data)
        
        return EmbeddedModel(
            embedded_text = embedded,
            original_text=text_data,
            ref=data_ref,
        )
    
    
    def embed_simple_text(self, text: str) -> List[float]:
        """
        Embedding text data into vector using OpenAI Embedding API

        Args:
            text (str): Text to be embedded

        Returns:
            List[float]: Embedded vector
        """
        
        embedded = openai.Embedding.create(
            input=text,
            model=self.model,
        )['data'][0]['embedding']
        
        return embedded
    
    def get_vector_size(self) -> int:
        return 1536

if __name__ == "__main__":
    client = OpenAIClient()
    result = client.embed(SourceData("Hello, world!", "https://www.google.com"))
    print(result)