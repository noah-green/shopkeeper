import gspread
from oauth2client.service_account import ServiceAccountCredentials

from market import Market

class MarketList:
    def __init__(self):
        # use creds to create a client to interact with the Google Drive API
        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        self.client = gspread.authorize(creds)
        self.markets = client.open('SHOPKEEPER')

    def get_market(self, guild_id):
        guild_record = self.markets.sheet1.find(guild_id, in_col=1)
        if not cell:
            return None
        else:
            sheet_id =  markets.sheet1.cell(guild_record.row, 2).value
            market_sheet = client.open(sheet_id)
            return Market(market_sheet)

    def create_market(self, guild_id):
        pass

    def delete_market(self, guild_id):
        pass

    def share_market(self, guild_id, email):
        get_market(guild_id).share(email, perm_type='user', role='writer')
