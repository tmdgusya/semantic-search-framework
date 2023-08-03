from .SourceData import SourceData
from typing import List

class CrawlerInterface:
    """
    This is an interface class for crawler.
    You have to implement this method when you make a new crawler class.
    """
    
    def crawl(self) -> List[SourceData]:
        """
        Load data from external source (e.g. web page, wiki pagem, etc.)

        Returns:
            str: data from external sources that are converted by only one line.
        """
        pass