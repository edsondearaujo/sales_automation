import sqlite3

def create_tables(conn):
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

def main():
    database = "data/automacao_vendas.db"
    conn = sqlite3.connect(database)
    
    create_tables(conn)
    conn.close()

if __name__ == '__main__':
    main()
