# models/venda.py

class Venda:
    def __init__(self, id, produto, quantidade, preco_unitario, data_venda):
        self.id = id
        self.produto = produto          # Deve ser um objeto da classe Produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.data_venda = data_venda

    def calcular_total(self):
        """Calcula o total da venda."""
        return self.quantidade * self.preco_unitario

    def __str__(self):
        """Representação em string da venda."""
        return (f"Venda: {self.produto.nome}, " 
                f"Quantidade: {self.quantidade}, "
                f"Preço Unitário: R$ {self.preco_unitario:.2f}, "
                f"Data: {self.data_venda}, "
                f"Total: R$ {self.calcular_total():.2f}")
