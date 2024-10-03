# models/produto.py

class Produto:
    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco

    def __str__(self):
        """Representação em string do produto."""
        return (f"Produto: {self.nome}, "
                f"Categoria: {self.categoria}, "
                f"Preço: R$ {self.preco:.2f}")
