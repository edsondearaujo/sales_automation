import gspread
from oauth2client.service_account import ServiceAccountCredentials

def carregar_dados_planilha(spreadsheet_id, sheet_range):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('config/credentials_google_api.json', scope)
    client = gspread.authorize(creds)

    # Acessar a planilha
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_range)
    dados = sheet.get_all_records()
    
    return dados
