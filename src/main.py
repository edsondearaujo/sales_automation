# src/main.py
from src.services.database import criar_tabelas, inserir_produto, inserir_venda, gerar_relatorio

def menu():
    print("\nMenu:")
    print("1. Inserir Produto")
    print("2. Inserir Venda")
    print("3. Gerar Relatório")
    print("4. Sair")

    return input("Escolha uma opção: ")

def main():
    criar_tabelas()

    while True:
        opcao = menu()

        if opcao == '1':
            nome = input("Nome do Produto: ")
            categoria = input("Categoria do Produto: ")
            inserir_produto(nome, categoria)
            print(f"Produto '{nome}' inserido com sucesso!")

        elif opcao == '2':
            produto_id = int(input("ID do Produto: "))
            quantidade = int(input("Quantidade Vendida: "))
            preco_unitario = float(input("Preço Unitário: "))
            data_venda = input("Data da Venda (YYYY-MM-DD): ")
            inserir_venda(produto_id, quantidade, preco_unitario, data_venda)
            print("Venda inserida com sucesso!")

        elif opcao == '3':
            relatorio = gerar_relatorio()
            print(f"Total Geral: R$ {relatorio['total_geral']:.2f}")
            print("Total por Produto:")
            for produto, dados in relatorio['total_por_produto'].items():
                print(f"Produto {produto}: Quantidade: {dados['quantidade']}, Total: R$ {dados['total']:.2f}")

        elif opcao == '4':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
