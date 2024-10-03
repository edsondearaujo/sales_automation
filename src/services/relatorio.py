# services/relatorio.py

from models.venda import Venda
from models.produto import Produto


class Relatorio:
    def __init__(self, vendas):
        """
        Inicializa o relatório com uma lista de vendas.
        :param vendas: Lista de objetos Venda
        """
        self.vendas = vendas

    def gerar_relatorio(self):
        """
        Gera um resumo das vendas, incluindo total por produto e total geral.
        :return: Dicionário com totais por produto e total geral
        """
        total_geral = 0
        total_por_produto = {}

        for venda in self.vendas:
            total_geral += venda.calcular_total()
            produto_nome = venda.produto.nome

            if produto_nome not in total_por_produto:
                total_por_produto[produto_nome] = {
                    'quantidade': 0,
                    'total': 0
                }
            total_por_produto[produto_nome]['quantidade'] += venda.quantidade
            total_por_produto[produto_nome]['total'] += venda.calcular_total()

        return {
            'total_geral': total_geral,
            'total_por_produto': total_por_produto
        }

    def __str__(self):
        """Representação em string do relatório."""
        relatorio = self.gerar_relatorio()
        report_str = f"Total Geral: R$ {relatorio['total_geral']:.2f}\n\n"
        report_str += "Total por Produto:\n"

        for produto, dados in relatorio['total_por_produto'].items():
            report_str += (f"{produto}: "
                           f"Quantidade: {dados['quantidade']}, "
                           f"Total: R$ {dados['total']:.2f}\n")

        return report_str
