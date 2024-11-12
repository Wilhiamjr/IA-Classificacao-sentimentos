import pickle
class SentimentoModel:
    def __init__(self):
        self.model_path = "./data/sentimento_model.p"
        self.vectorizer = None
        self.classificador = None
   
    def classificar(self, texto):
        with open(self.model_path, "rb") as f:
            self.classificador = pickle.load(f)
            print(self.classificador)
        self.vectorizer = self.classificador[0]
        text_tfidf = self.vectorizer.transform([texto])
        return self.classificador[1].predict(text_tfidf)