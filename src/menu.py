class Menu:
    def __init__(self):
        self.opcoes = {}

    def adicionar_opcao(self, chave, descricao, comando):
        self.opcoes[chave] = (descricao, comando)

    def exibir(self):
        print("\nMenu:")
        for chave, (descricao, _) in self.opcoes.items():
            print(f"{chave}. {descricao}")

    def escolher(self, chave):
        comando = self.opcoes.get(chave)
        if comando:
            descricao, acao = comando
            acao.execute()
        else:
            print("Opção inválida.")
