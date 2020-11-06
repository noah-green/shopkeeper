import sqlite3
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_db():
    return sqlite3.connect('../../../var/shopkeeper.sqlite3', isolation_level=None)

def get_sheets_client():
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name('../../../secrets/client_secret.json', scopes)
    return gspread.authorize(creds)
