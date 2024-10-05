import os
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Defina os escopos necessários
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def autenticar_google_sheets():
    """Autentica na API do Google Sheets usando as credenciais fornecidas."""
    credenciais_path = './data/credentials.json'

    try:
        creds = Credentials.from_service_account_file(credenciais_path, scopes=SCOPES)
        return build("sheets", "v4", credentials=creds)
    except Exception as e:
        return None


def carregar_dados_planilha(nome_planilha, aba):
    """Carrega os dados de uma planilha específica do Google Sheets."""
    try:
        service = autenticar_google_sheets()

        # Faz a requisição para ler os dados da planilha
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=nome_planilha, range=aba).execute()
        values = result.get('values', [])

        return values
    except HttpError as err:
        return None
