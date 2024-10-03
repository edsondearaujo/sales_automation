import unittest
from src.models.produto import Produto

class TestProduto(unittest.TestCase):

    def setUp(self):
        self.produto = Produto(nome="Produto A", categoria="Categoria 1", preco=10.00)

    def test_inicializacao(self):
        self.assertEqual(self.produto.nome, "Produto A")
        self.assertEqual(self.produto.categoria, "Categoria 1")
        self.assertEqual(self.produto.preco, 10.00)

    def test_str(self):
        self.assertEqual(str(self.produto), "Produto: Produto A, Categoria: Categoria 1, Preço: R$ 10.00")
