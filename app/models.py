from pydantic import BaseModel, validator

class AnalyzeRequest(BaseModel):
    """
    This model is for taking the request and parsing that into an object.
    """
    text: str

    @validator('text')
    def validate_text(cls, text):
        if text == "":
            raise ValueError("Empty string is not allowed")
        return text