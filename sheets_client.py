import gspread
from oauth2client.service_account import ServiceAccountCredentials

def sheets_client():
    # use creds to create a client to interact with the Google Drive API
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name('secrets/client_secret.json', scope)
    return gspread.authorize(creds)
