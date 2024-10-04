class Produto:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria

class Venda:
    def __init__(self, produto_id, quantidade, preco_unitario, data_venda):
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.data_venda = data_venda
