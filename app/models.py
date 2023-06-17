from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    """
    This model is for taking the request and parsing that into an object.
    """
    text: str