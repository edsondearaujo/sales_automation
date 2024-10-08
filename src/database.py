import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conexão com o banco de dados {db_file} estabelecida com sucesso.")
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def insert_produto(conn, nome, categoria, preco):
    cur = conn.cursor()
    cur.execute("INSERT INTO produtos (nome, categoria, preco) VALUES (?, ?, ?)", (nome, categoria, preco))
    conn.commit()

def insert_vendedor(conn, nome):
    cur = conn.cursor()
    cur.execute("INSERT INTO vendedores (nome) VALUES (?)", (nome,))
    conn.commit()

def insert_venda(conn, produto_id, vendedor_id, quantidade):
    cur = conn.cursor()
    cur.execute("INSERT INTO vendas (produto_id, vendedor_id, quantidade) VALUES (?, ?, ?)", (produto_id, vendedor_id, quantidade))
    conn.commit()
