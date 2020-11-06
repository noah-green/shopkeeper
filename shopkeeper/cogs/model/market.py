from .shop import Shop

class Market:
    """Manage a gspread Spreadsheet object representing a market."""

    def __init__(self, spreadsheet):
        self.spreadsheet = spreadsheet

    def get_shop(self, shop_name):
        try:
            return Shop(self.spreadsheet.worksheet(shop_name))
        except:
            return None

    def get_ledger(self):
        return self.spreadsheet.worksheet("Ledger")

    def get_shops(self):
        return [record['shop'] for record in self.spreadsheet.worksheet('Shop List').get_all_records()]

    def get_open_shops(self):
        open_shops = filter(lambda x: x['open'] == "TRUE", self.spreadsheet.worksheet('Shop List').get_all_records())
        return [record['shop'] for record in open_shops]

    def open_shop(self, shop_name):
        row = self.spreadsheet.worksheet('Shop List').find(shop_name).row
        self.spreadsheet.worksheet('Shop List').update_cell(row, 2, 'TRUE')

    def close_shop(self, shop_name):
        row = self.spreadsheet.worksheet('Shop List').find(shop_name).row
        self.spreadsheet.worksheet('Shop List').update_cell(row, 2, 'FALSE')

    def open_all_shops(self):
        pass

    def close_all_shops(self):
        pass
