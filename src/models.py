# src/models.py

class Produto:
    def __init__(self, produto_id, nome, categoria, preco):
        self.produto_id = produto_id  # Identificador único do produto
        self.nome = nome                # Nome do produto
        self.categoria = categoria      # Categoria do produto
        self.preco = preco              # Preço do produto

class Vendedor:
    def __init__(self, vendedor_id, nome):
        self.vendedor_id = vendedor_id  # Identificador único do vendedor
        self.nome = nome                # Nome do vendedor

class Venda:
    def __init__(self, venda_id, produto_id, vendedor_id, quantidade):
        self.venda_id = venda_id            # Identificador único da venda
        self.produto_id = produto_id        # ID do produto vendido
        self.vendedor_id = vendedor_id      # ID do vendedor que fez a venda
        self.quantidade = quantidade        # Quantidade vendida
