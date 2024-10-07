#src/utils.py
import logging
from googleapiclient.discovery import build
from src.auth import autenticar_google_sheets


def carregar_dados_aba(spreadsheet_id, range_name):
    """Carrega os dados de uma aba da planilha Google Sheets."""
    print(f"Iniciando o carregamento de dados da aba: {range_name}")
    creds = autenticar_google_sheets()
    if not creds:
        logging.error("Erro: Falha na autenticação.")
        print("Erro na autenticação")
        return None

    try:
        print(f"Autenticação bem-sucedida. Tentando acessar a aba {range_name}.")
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        print(f"Acessando a planilha com ID: {spreadsheet_id}, Range: {range_name}")
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()

        values = result.get('values', [])
        if not values:
            logging.info(f"Nenhum dado encontrado na aba {range_name}.")
            print(f"Nenhum dado encontrado na aba {range_name}.")
            return []

        print(f"Dados carregados da aba {range_name}:", values)
        return values
    except Exception as e:
        logging.error(f"Erro ao acessar a API do Google Sheets: {e}")
        print(f"Erro ao acessar a API do Google Sheets: {e}")
        return None
