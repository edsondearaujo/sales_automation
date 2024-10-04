class Command:
    def execute(self):
        raise NotImplementedError("Você deve implementar o método execute.")

class InserirProdutoCommand(Command):
    def __init__(self, database):
        self.database = database

    def execute(self):
        nome = input("Nome do Produto: ")
        categoria = input("Categoria do Produto: ")
        self.database.inserir_produto(nome, categoria)
        print(f"Produto '{nome}' inserido com sucesso!")

class InserirVendaCommand(Command):
    def __init__(self, database):
        self.database = database

    def execute(self):
        print()
        produto_id = input("ID do Produto: ")
        quantidade = int(input("Quantidade Vendida: "))
        preco_unitario = float(input("Preço Unitário: "))
        data_venda = input("Data da Venda (YYYY-MM-DD): ")
        self.database.inserir_venda(produto_id, quantidade, preco_unitario, data_venda)
        print()
        print("Venda inserida com sucesso!")

class GerarRelatorioCommand(Command):
    def __init__(self, database):
        self.database = database

    def execute(self):
        relatorio = self.database.gerar_relatorio()
        if relatorio:
            print()
            print(f"Total Geral: R$ {relatorio['total_geral']:.2f}")
            print("Total por Produto:")
            print()
            for produto in relatorio['produtos']:
                print(f"Produto ID {produto['produto_id']}: Quantidade: {produto['quantidade']}, Total: R$ {produto['total']:.2f}")
        else:
            print("Nenhuma venda registrada.")

class SairCommand(Command):
    def execute(self):
        print("Saindo...")
        exit(0)
