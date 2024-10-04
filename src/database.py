# src/database.py

import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conexão estabelecida com o banco de dados: {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def fetch_all_produtos(conn):
    """ Fetch all products from the database """
    cur = conn.cursor()
    cur.execute("SELECT * FROM produtos")
    return cur.fetchall()

def fetch_all_vendedores(conn):
    """ Fetch all vendors from the database """
    cur = conn.cursor()
    cur.execute("SELECT * FROM vendedores")
    return cur.fetchall()

def fetch_all_vendas(conn):
    """ Fetch all sales from the database """
    cur = conn.cursor()
    cur.execute("SELECT * FROM vendas")
    return cur.fetchall()

def insert_produto(conn, nome, categoria, preco):
    """ Insert a new product into the produtos table """
    cur = conn.cursor()
    cur.execute("INSERT INTO produtos (nome, categoria, preco) VALUES (?, ?, ?)", (nome, categoria, preco))
    conn.commit()
    print(f"Produto '{nome}' inserido com sucesso!")

def insert_venda(conn, produto_id, vendedor_id, quantidade):
    """ Insert a new sale into the vendas table """
    cur = conn.cursor()
    cur.execute("INSERT INTO vendas (produto_id, vendedor_id, quantidade) VALUES (?, ?, ?)", (produto_id, vendedor_id, quantidade))
    conn.commit()
    print(f"Venda registrada: Produto ID {produto_id}, Vendedor ID {vendedor_id}, Quantidade {quantidade}")

def close_connection(conn):
    """ Close the database connection """
    if conn:
        conn.close()
