import unittest
from app.models.models_ia import SentimentoModel

class TestSentimentClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = SentimentoModel()

    def test_positivo(self):
        texto = "Adorei o meu fim de semana em Paris! O clima estava perfeito, a comida foi deliciosa e os monumentos históricos foram incríveis."
        resultado = self.classifier.classificar(texto)
        self.assertEqual(resultado, "positivo")

    def test_negativo(self):
        texto = "Não gosto nada desse restaurante. A comida é ruim, o serviço é lento e o ambiente é desconfortável."
        resultado = self.classifier.classificar(texto)
        self.assertEqual(resultado, "negativo")

    def test_neutro(self):
        texto = "O serviço do hotel foi bom, a comida foi aceitável e a localização foi conveniente. Nada de muito bom ou muito ruim."
        resultado = self.classifier.classificar(texto)
        self.assertEqual(resultado, "neutro")

    def test_vazio(self):
        texto = ""
        resultado = self.classifier.classificar(texto)
        self.assertEqual(resultado, "neutro")

    def test_nulo(self):
        texto = None
        resultado = self.classifier.classificar(texto)
        self.assertEqual(resultado, "neutro")

if __name__ == "__main__":
    unittest.main()