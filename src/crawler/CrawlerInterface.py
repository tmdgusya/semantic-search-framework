

class CralwerInterface:
    """
    This is an interface class for crawler.
    You have to implement this method when you make a new crawler class.
    """
    
    def crawl(self, request) -> str:
        """
        Load data from external source (e.g. web page, wiki pagem, etc.)

        Args:
            request (_type_): any information that is needed to crawl data from external source.

        Returns:
            str: data from external sources that are converted by only one line.
        """
        pass