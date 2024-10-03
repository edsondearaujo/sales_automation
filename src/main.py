# main.py
from src.services.database import criar_tabelas, inserir_produto, inserir_venda, gerar_relatorio


def main():
    # Cria as tabelas do banco de dados
    criar_tabelas()

    # Exemplo de como você pode inserir vendas diretamente no banco de dados
    produtos = [
        {"nome": "Produto A", "categoria": "Categoria 1"},
        {"nome": "Produto B", "categoria": "Categoria 2"}
    ]

    for produto in produtos:
        inserir_produto(produto["nome"], produto["categoria"])

    # Inserindo vendas para os produtos
    vendas = [
        {"produto_id": 1, "quantidade": 2, "preco_unitario": 10.0, "data_venda": "2024-10-01"},
        {"produto_id": 2, "quantidade": 1, "preco_unitario": 20.0, "data_venda": "2024-10-02"}
    ]

    for venda in vendas:
        inserir_venda(venda["produto_id"], venda["quantidade"], venda["preco_unitario"], venda["data_venda"])

    # Gera o relatório do banco de dados
    relatorio = gerar_relatorio()

    print(f"Total Geral: R$ {relatorio['total_geral']:.2f}")
    print("Total por Produto:")
    for produto, dados in relatorio['total_por_produto'].items():
        print(f"{produto}: Quantidade: {dados['quantidade']}, Total: R$ {dados['total']:.2f}")


if __name__ == "__main__":
    main()
