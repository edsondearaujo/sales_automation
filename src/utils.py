import logging
from googleapiclient.discovery import build
from src.auth_google import autenticar_google_sheets

def carregar_dados_aba(spreadsheet_id, range_name):
    creds = autenticar_google_sheets()
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    
    return values

def processar_dados_e_inserir(conn, dados_produtos, dados_vendedores, dados_vendas):
    for item in dados_produtos[1:]:
        nome, preco, categoria = item[1], float(item[2]), item[3]
        insert_produto(conn, nome, categoria, preco)

    for item in dados_vendedores[1:]:
        nome_vendedor = item[1]
        insert_vendedor(conn, nome_vendedor)

    for item in dados_vendas[1:]:
        produto_id, vendedor_id, quantidade = int(item[1]), int(item[2]), int(item[3])
        insert_venda(conn, produto_id, vendedor_id, quantidade)
