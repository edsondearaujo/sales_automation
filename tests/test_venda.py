import unittest
from src.models.produto import Produto
from src.models.venda import Venda

class TestVenda(unittest.TestCase):

    def setUp(self):
        self.produto = Produto(nome="Produto A", categoria="Categoria 1", preco=10.00)
        self.venda = Venda(id=1, produto=self.produto, quantidade=2, preco_unitario=10.00, data_venda="2024-10-03")

    def test_calcular_total(self):
        self.assertEqual(self.venda.calcular_total(), 20.00)

    def test_str(self):
        self.assertEqual(str(self.venda), "Venda: Produto A, Quantidade: 2, Preço Unitário: R$ 10.00, Data: 2024-10-03, Total: R$ 20.00")
