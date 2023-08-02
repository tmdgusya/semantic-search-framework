from src.embedd.EmbeddedModel import EmbeddedModel
from src.storage.QueryResultModel import QueryResultModel

class StorageInterface:
    """
    Interface for storage classes
    You have to implement this method when you make a new storage class.
    """
    
    def save(self, data: EmbeddedModel) -> bool:
        """
        Save data to storage

        Args:
            data (_type_): Data to be saved
            
        Returns:
            bool: True if data is saved successfully, False otherwise.
        """
        pass
    
    def query(self, query: str) -> QueryResultModel:
        """
        Query data from storage        

        Args:
            query (str): Query string
        """