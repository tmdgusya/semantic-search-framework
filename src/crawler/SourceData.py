

class SourceData:
    """
    This class is a data class for source data.
    """

    def __init__(self, text: str, ref: str) -> None:
        self.text = text
        self.ref = ref
    
    def __repr__(self) -> str:
        return f"SourceData(text={self.text}, ref={self.ref})"
    
    def __str__(self) -> str:
        return f"SourceData(text={self.text}, ref={self.ref})"