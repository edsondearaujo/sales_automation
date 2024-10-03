# src/services/database.py
import sqlite3


def criar_tabelas():
    with sqlite3.connect('vendas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER,
                quantidade INTEGER NOT NULL,
                preco_unitario REAL NOT NULL,
                data_venda TEXT NOT NULL,
                FOREIGN KEY (produto_id) REFERENCES produtos (id)
            )
        ''')
        conn.commit()


def inserir_produto(nome, categoria):
    with sqlite3.connect('vendas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produtos (nome, categoria) VALUES (?, ?)', (nome, categoria))
        conn.commit()


def inserir_venda(produto_id, quantidade, preco_unitario, data_venda):
    with sqlite3.connect('vendas.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO vendas (produto_id, quantidade, preco_unitario, data_venda) VALUES (?, ?, ?, ?)',
                       (produto_id, quantidade, preco_unitario, data_venda))
        conn.commit()


def gerar_relatorio():
    with sqlite3.connect('vendas.db') as conn:
        cursor = conn.cursor()

        # Obter total geral e total por produto
        cursor.execute('''
            SELECT p.nome, SUM(v.quantidade) as quantidade, SUM(v.quantidade * v.preco_unitario) as total
            FROM vendas v
            JOIN produtos p ON v.produto_id = p.id
            GROUP BY p.nome
        ''')

        vendas = cursor.fetchall()

        total_geral = sum(venda[2] for venda in vendas)  # Somando os totais
        total_por_produto = {
            venda[0]: {
                'quantidade': venda[1],
                'total': venda[2]
            }
            for venda in vendas
        }

        return {
            'total_geral': total_geral,
            'total_por_produto': total_por_produto
        }
