from fastapi import APIRouter, HTTPException
from schemas.schema_api import SentimentoRequest, SentimentoResponse
from services.service_ia import Servico_IA

api_router = APIRouter()

@api_router.post("/sentimento", response_model=SentimentoResponse)
async def classificar_sentimento(request: SentimentoRequest):
    servico_ia = Servico_IA()
    resultado = servico_ia.classificar(request.texto)
    if resultado == 1:
        return {"sentimento": "Positivo"}
    elif resultado == 0:
        return {"sentimento": "Negativo"}
    else:
        raise HTTPException(status_code=400, detail="Erro ao classificar sentimento")