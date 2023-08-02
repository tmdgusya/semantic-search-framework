from typing import List


class QueryResultModel:
    
    def __init__(self, embedded_text: List[float], original_text: str, ref: str) -> None:
        self.embedded_text = embedded_text
        self.original_text = original_text
        self.ref = ref
        
    
    def __repr__(self) -> str:
        return f"QueryResultModel(embedded_text={self.embedded_text}, original_text={self.original_text}, ref={self.ref})"
    
    def __str__(self) -> str:
        return f"QueryResultModel(embedded_text={self.embedded_text}, original_text={self.original_text}, ref={self.ref})"