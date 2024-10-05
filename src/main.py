from utils import carregar_dados_planilha
from database import create_connection, insert_produto
import sqlite3


def gerar_relatorio(conn):
    """Gera um relatório de vendas consolidado."""
    cur = conn.cursor()
    cur.execute("""
        SELECT p.nome, SUM(v.quantidade) AS total_vendas,
               SUM(v.quantidade * p.preco) AS lucro_total,
               ve.nome AS vendedor_nome, 
               SUM(v.quantidade) AS total_vendas_vendedor
        FROM vendas v
        JOIN produtos p ON v.produto_id = p.id
        JOIN vendedores ve ON v.vendedor_id = ve.id
        GROUP BY p.id, ve.nome
    """)

    relatorios = cur.fetchall()

    print("Relatório de Vendas")
    print("---------------------")
    for row in relatorios:
        produto, total_vendas, lucro_total, vendedor_nome, total_vendas_vendedor = row
        print(f"Produto: {produto}")
        print(f"Total Vendas: {total_vendas}")
        print(f"Lucro Total: R$ {lucro_total:.2f}")
        print(f"Vendedor: {vendedor_nome}")
        print(f"Quantidade: {total_vendas_vendedor}")
        print("---------------------")


def processar_dados_e_inserir(conn, dados_produtos):
    """Processa os dados da planilha e insere os produtos no banco de dados."""
    for item in dados_produtos[1:]:  # Ignora a primeira linha (cabeçalho)
        nome, categoria, preco = item[0], item[1], float(item[2])
        insert_produto(conn, nome, categoria, preco)


def main():
    # Carrega os dados da planilha do Google
    dados_produtos = carregar_dados_planilha('11v6MHigHbyEYJ1WqSAZr9pbKGgapXMzS70oKK-HSPvA', 'produtos!A1:D6')

    # Conectar ao banco de dados
    conn = create_connection('data/automacao_vendas.db')
    if not conn:
        return

    # Processar os dados e inserir no banco de dados
    processar_dados_e_inserir(conn, dados_produtos)

    # Gerar relatório de vendas
    gerar_relatorio(conn)

    # Fechar a conexão com o banco de dados
    if conn:
        conn.close()


if __name__ == "__main__":
    main()
