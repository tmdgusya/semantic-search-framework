from .SourceData import SourceData

class CralwerInterface:
    """
    This is an interface class for crawler.
    You have to implement this method when you make a new crawler class.
    """
    
    def crawl(self) -> SourceData:
        """
        Load data from external source (e.g. web page, wiki pagem, etc.)

        Returns:
            str: data from external sources that are converted by only one line.
        """
        pass