import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def autenticar_google_sheets():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None

    if os.path.exists('config/credentials_google_api.json'):
        creds = Credentials.from_authorized_user_file('config/credentials_google_api.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('config/credentials_google_api.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
    return creds
