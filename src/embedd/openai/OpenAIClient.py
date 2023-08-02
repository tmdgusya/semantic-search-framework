import os
import openai

from src.embedd.EmbeddedModel import EmbeddedModel
from src.embedd.EmbeddingInteface import EmbeddingInterface
from src.crawler.SourceData import SourceData

class OpenAIClient(EmbeddingInterface):
    
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_EMBEDDING_MODEL")
        print(openai.api_key)
        print(self.model)
        pass
    
    
    def embed(self, data: SourceData) -> EmbeddedModel:
        """
        Embedding text data into vector using OpenAI Embedding API

        Args:
            data (SourceData): SourceData to be embedded

        Returns:
            EmbeddedModel: EmbeddedModel
        """
        
        print(f"Will be embedded: {data}")
        
        text_data = data.text
        data_ref = data.ref
        
        embedded = openai.Embedding.create(
            input=text_data,
            model=self.model,
        )['data'][0]['embedding']
        
        print(f"Embedded by OpenAI: {embedded}")
        
        return EmbeddedModel(
            embedded_text = embedded,
            original_text=text_data,
            ref=data_ref,
        )
    

if __name__ == "__main__":
    client = OpenAIClient()
    result = client.embed(SourceData("Hello, world!", "https://www.google.com"))
    print(result)