# services/database.py

import sqlite3

# Função para criar as tabelas no banco de dados
def criar_tabelas():
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS venda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_id INTEGER,
        quantidade INTEGER,
        preco_unitario REAL,
        data TEXT,
        FOREIGN KEY (produto_id) REFERENCES produto (id)
    )
    ''')

    conn.commit()
    conn.close()

# Função para inserir um produto no banco de dados
def inserir_produto(nome, categoria):
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO produto (nome, categoria)
    VALUES (?, ?)
    ''', (nome, categoria))

    conn.commit()
    conn.close()

# Função para inserir uma venda no banco de dados
def inserir_venda(produto_id, quantidade, preco_unitario, data):
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO venda (produto_id, quantidade, preco_unitario, data)
    VALUES (?, ?, ?, ?)
    ''', (produto_id, quantidade, preco_unitario, data))

    conn.commit()
    conn.close()

# Função para gerar o relatório de vendas
def gerar_relatorio():
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()

    # Verificando se há produtos e vendas no banco
    cursor.execute('SELECT COUNT(*) FROM venda')
    venda_count = cursor.fetchone()[0]
    if venda_count == 0:
        conn.close()
        print("Nenhuma venda registrada.")
        return None

    # Consulta para obter o total de vendas por produto
    cursor.execute('''
    SELECT p.nome, SUM(v.quantidade) AS total_quantidade, SUM(v.quantidade * v.preco_unitario) AS total_venda
    FROM vendas v
    JOIN produto p ON v.produto_id = p.id
    GROUP BY p.nome
    ''')

    relatorio = cursor.fetchall()

    if len(relatorio) == 0:
        print("Nenhum dado encontrado no relatório.")
        conn.close()
        return None

    total_geral = sum(item[2] for item in relatorio)  # Calculando o total geral

    conn.close()

    return {
        'total_geral': total_geral,
        'total_por_produto': relatorio
    }
