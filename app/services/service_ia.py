from models.models_ia import SentimentoModel

class Servico_IA:
    def __init__(self):
        self.modelo = SentimentoModel()

    def classificar(self, texto):
        return self.modelo.classificar(texto)
    
 