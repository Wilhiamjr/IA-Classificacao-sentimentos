from pydantic import BaseModel

class SentimentoRequest(BaseModel):
    texto: str

class SentimentoResponse(BaseModel):
    sentimento: str