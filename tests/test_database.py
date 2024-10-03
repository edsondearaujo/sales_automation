# tests/test_database.py
import unittest
from src.services.database import criar_tabelas, inserir_produto, inserir_venda, gerar_relatorio

class TestDatabase(unittest.TestCase):
    def setUp(self):
        criar_tabelas()

    def test_inserir_produto_e_venda(self):
        inserir_produto("Produto A", "Categoria A")
        inserir_venda(1, 10, 5.0, '2024-10-01')

        relatorio = gerar_relatorio()
        self.assertEqual(relatorio['total_geral'], 50.0)
        self.assertEqual(len(relatorio['total_por_produto']), 1)
        self.assertEqual(relatorio['total_por_produto'][0][0], 'Produto A')

if __name__ == '__main__':
    unittest.main()
