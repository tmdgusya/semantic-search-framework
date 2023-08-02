from src.embedd.EmbeddedModel import EmbeddedModel

class EmbeddingInterface:
    """
    Interface for embedding class
    You have to implement this method when you make a new embedding class.
    """
    
    def embed(self, text_data) -> EmbeddedModel:
        """
        Embedding text data into vector

        Args:
            text_data (_type_): Text data to be embedded
        """
        pass
    