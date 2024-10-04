# src/setup.py

import sqlite3
import random

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_tables(conn):
    # Criar tabelas de produtos, vendedores e vendas
    create_produtos_table = '''CREATE TABLE IF NOT EXISTS produtos (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    categoria TEXT NOT NULL,
                                    preco REAL NOT NULL
                                );'''

    create_vendedores_table = '''CREATE TABLE IF NOT EXISTS vendedores (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL
                                );'''

    create_vendas_table = '''CREATE TABLE IF NOT EXISTS vendas (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                produto_id INTEGER,
                                vendedor_id INTEGER,
                                quantidade INTEGER,
                                FOREIGN KEY (produto_id) REFERENCES produtos (id),
                                FOREIGN KEY (vendedor_id) REFERENCES vendedores (id)
                            );'''

    conn.execute(create_produtos_table)
    conn.execute(create_vendedores_table)
    conn.execute(create_vendas_table)

def insert_produto(conn, nome, categoria, preco):
    sql = '''INSERT INTO produtos(nome, categoria, preco) VALUES(?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (nome, categoria, preco))
    conn.commit()

def insert_vendedor(conn, nome):
    sql = '''INSERT INTO vendedores(nome) VALUES(?)'''
    cur = conn.cursor()
    cur.execute(sql, (nome,))
    conn.commit()

def insert_venda(conn, produto_id, vendedor_id, quantidade):
    sql = '''INSERT INTO vendas(produto_id, vendedor_id, quantidade) VALUES(?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, (produto_id, vendedor_id, quantidade))
    conn.commit()

def fetch_all_produtos(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM produtos")
    return cur.fetchall()

def fetch_all_vendedores(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM vendedores")
    return cur.fetchall()

def insert_vendas_aleatorias(conn, num_vendas):
    produtos = fetch_all_produtos(conn)
    vendedores = fetch_all_vendedores(conn)

    for _ in range(num_vendas):
        produto = random.choice(produtos)
        vendedor = random.choice(vendedores)
        quantidade = random.randint(1, 10)  # Vendas entre 1 e 10 unidades

        # Inserir venda no banco de dados
        insert_venda(conn, produto[0], vendedor[0], quantidade)

    print(f"{num_vendas} vendas aleatórias inseridas com sucesso!")

def main():
    database = "automacao_vendas.db"
    conn = create_connection(database)

    if conn:
        create_tables(conn)

        # Exemplo de produtos e vendedores
        produtos = [
            ("Curso de Informática Básica", "Informática", 100.0),
            ("Curso de Programação Python para Análise de Dados", "Curso", 200.0),
            ("Curso de Java Avançado", "Curso", 250.0),
            ("Curso de Marketing Digital", "Marketing", 150.0),
            ("Curso de Design Gráfico", "Design", 180.0),
        ]

        vendedores = [
            "Alice",
            "Bob",
            "Carlos",
            "Diana",
            "Eva",
        ]

        # Inserir produtos
        for nome, categoria, preco in produtos:
            insert_produto(conn, nome, categoria, preco)

        # Inserir vendedores
        for nome in vendedores:
            insert_vendedor(conn, nome)

        # Inserir vendas aleatórias
        insert_vendas_aleatorias(conn, 100)  # Insere 100 vendas aleatórias

        print("Banco de dados e tabelas criados e dados inseridos com sucesso!")

    if conn:
        conn.close()

if __name__ == "__main__":
    main()
