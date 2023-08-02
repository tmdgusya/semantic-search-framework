

class EmbeddedModel:
    """
    EmbeddedModel is a class that represents the embedded text, original text and the reference of the text.
    """
    
    def __init__(self, embedded_text, original_text, ref) -> None:
        self.embedded_text = embedded_text
        self.original_text = original_text
        self.ref = ref
        
    def __repr__(self) -> str:
        return f"EmbeddedModel(embedded_text={self.embedded_text}, original_text={self.original_text}, ref={self.ref})"
    
    def __str__(self) -> str:
        return f"EmbeddedModel(embedded_text={self.embedded_text}, original_text={self.original_text}, ref={self.ref})"