from src.services.database import Database
from src.commands import InserirProdutoCommand, InserirVendaCommand, GerarRelatorioCommand, SairCommand
from src.menu import Menu

class Aplicacao:
    def __init__(self):
        self.database = Database()
        self.database.criar_tabelas()

    def iniciar(self):
        menu = Menu()
        menu.adicionar_opcao("1", "Inserir Produto", InserirProdutoCommand(self.database))
        menu.adicionar_opcao("2", "Inserir Venda", InserirVendaCommand(self.database))
        menu.adicionar_opcao("3", "Gerar Relatório", GerarRelatorioCommand(self.database))
        menu.adicionar_opcao("4", "Sair", SairCommand())

        while True:
            menu.exibir()
            print()
            opcao = input("Escolha uma opção: ")
            print()
            menu.escolher(opcao)
            print()

if __name__ == "__main__":
    app = Aplicacao()
    app.iniciar()
