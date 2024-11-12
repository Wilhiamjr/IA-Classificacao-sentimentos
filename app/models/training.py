# from data.data_training import X, y
from models_ia import SentimentoModel
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

X = [
    "Eu amo esse produto!",
    "Esse produto é ruim.",
    "Eu não sei o que pensar sobre esse produto.",
    "Eu odeio esse produto!",
    "Esse produto é incrível!",
    "Eu estou muito satisfeito com esse produto.",
    "Esse produto é uma porcaria.",
    "Eu não entendo por que as pessoas gostam desse produto.",
    "Esse produto é muito caro.",
    "Eu recomendaria esse produto para qualquer pessoa.",
    "Eu não gostei da embalagem desse produto.",
    "Esse produto é muito fácil de usar.",
    "Eu não sei se eu gostei desse produto ou não.",
    "Esse produto é muito melhor do que o anterior.",
    "Eu não gostei do sabor desse produto.",
    "Esse produto é muito saudável.",
    "Eu não entendo por que as pessoas não gostam desse produto.",
    "Esse produto é muito divertido.",
    "Eu não gostei da cor desse produto.",
    "Esse produto é muito prático.",
]

y = [
    1,
    0,
    2,
    0,
    1,
    1,
    0,
    2,
    0,
    1,
    0,
    1,
    2,
    1,
    0,
    1,
    2,
    1,
    0,
    1,
]  # 1: positivo, 0: negativo, 2: neutro


class TrainingModel(SentimentoModel):
 def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classificador = MultinomialNB()
        self.model_path = "app/data/sentimento_model.p"

 def treinar(self, texts, labels):
        texts_train, texts_test, labels_train, labels_test = train_test_split(texts, labels, test_size=0.2, random_state=42)
        texts_train_tfidf = self.vectorizer.fit_transform(texts_train)
        self.classificador.fit(texts_train_tfidf, labels_train)
        texts_test_tfidf = self.vectorizer.transform(texts_test)
        print("Precisão:", self.classificador.score(texts_test_tfidf, labels_test))
        self.persist_model()

 def persist_model(self):
        with open(self.model_path, "wb") as f:
            pickle.dump((self.vectorizer, self.classificador), f)

if __name__ == "__main__":

    training_model = TrainingModel()

    training_model.treinar(X, y)
