import sqlite3
import gspread
import from oauth2client.service_account import ServiceAccountCredentials


def get_db():
    pass


def get_sheets_client():
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    return = gspread.authorize(creds)
