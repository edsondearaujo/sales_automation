import sqlite3


def conectar_banco():
    conn = sqlite3.connect('automacao_vendas.db')
    print("Conexão estabelecida com o banco de dados.")
    return conn


def inserir_produto(conn, nome, preco, categoria):
    cur = conn.cursor()
    cur.execute("INSERT INTO produtos (nome, preco, categoria) VALUES (?, ?, ?)", (nome, preco, categoria))
    conn.commit()
    print(f"Produto '{nome}' registrado com sucesso!")


def inserir_venda(conn, produto_id, vendedor_id, quantidade):
    cur = conn.cursor()
    cur.execute("INSERT INTO vendas (produto_id, vendedor_id, quantidade) VALUES (?, ?, ?)",
                (produto_id, vendedor_id, quantidade))
    conn.commit()
    print(f"Venda registrada: Produto ID {produto_id}, Vendedor ID {vendedor_id}, Quantidade {quantidade}")


def gerar_relatorio(conn):
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


def main():
    conn = conectar_banco()

    while True:
        print("\n       MENU")
        print("1. Inserir Produto")
        print("2. Inserir Venda")
        print("3. Gerar Relatório")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: R$ "))
            categoria = input("Digite a categoria do produto: ")  # Nova entrada para categoria
            inserir_produto(conn, nome, preco, categoria)

        elif opcao == '2':
            produto_id = int(input("Digite o ID do produto: "))
            vendedor_id = int(input("Digite o ID do vendedor: "))
            quantidade = int(input("Digite a quantidade vendida: "))
            inserir_venda(conn, produto_id, vendedor_id, quantidade)

        elif opcao == '3':
            gerar_relatorio(conn)

        elif opcao == '4':
            break

        else:
            print("Opção inválida. Tente novamente.")

    conn.close()


if __name__ == "__main__":
    main()
