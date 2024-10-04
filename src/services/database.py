import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('vendas.db')
        self.cursor = self.conn.cursor()

    def criar_tabelas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                categoria TEXT
            );
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS venda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER,
                quantidade INTEGER,
                preco_unitario REAL,
                data_venda TEXT,
                FOREIGN KEY (produto_id) REFERENCES produto (id)
            );
        ''')
        self.conn.commit()

    def inserir_produto(self, nome, categoria):
        self.cursor.execute('''
            INSERT INTO produto (nome, categoria) VALUES (?, ?)
        ''', (nome, categoria))
        self.conn.commit()

    def inserir_venda(self, produto_id, quantidade, preco_unitario, data_venda):
        self.cursor.execute('''
            INSERT INTO venda (produto_id, quantidade, preco_unitario, data_venda)
            VALUES (?, ?, ?, ?)
        ''', (produto_id, quantidade, preco_unitario, data_venda))
        self.conn.commit()

    def gerar_relatorio(self):
        self.cursor.execute('''
            SELECT SUM(venda.quantidade * venda.preco_unitario) as total_geral
            FROM venda;
        ''')
        total_geral = self.cursor.fetchone()[0]
        if total_geral is None:
            return None

        self.cursor.execute('''
            SELECT produto.id, produto.nome, SUM(venda.quantidade) as quantidade, 
            SUM(venda.quantidade * venda.preco_unitario) as total
            FROM venda
            INNER JOIN produto ON venda.produto_id = produto.id
            GROUP BY produto.id;
        ''')
        produtos = self.cursor.fetchall()

        return {
            'total_geral': total_geral,
            'produtos': [{'produto_id': p[0], 'nome': p[1], 'quantidade': p[2], 'total': p[3]} for p in produtos]
        }
