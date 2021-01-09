import gspread
from tabulate import tabulate

class Shop:
    """Manage a gspread Worksheet object representing a shop."""

    def __init__(self, worksheet):
        self.worksheet = worksheet

    def get_name(self):
        return self.worksheet.title

    def get_stock(self):
        """Return the stock as a list of dicts."""
        return self.worksheet.get_all_records()

    def get_stock_message(self):
        """Return a string listing the stock."""
        stocklist = []
        for record in self.worksheet.get_all_records():
            item = {
                'Item': record['name'],
                'Price': str(record['price']) + ' gp',
                'Stock': record['stock']
            }
            stocklist.append(item)
        table = tabulate(stocklist, headers='keys')
        return f"```{table}```"

    def get_description(self, item_name):
        try:
            row = self.worksheet.find(item_name).row
        except gspread.exceptions.CellNotFound:
            raise ValueError
        return self.worksheet.row_values(row)[3]

    def get_price(self, item_name):
        try:
            row = self.worksheet.find(item_name).row
        except gspread.exceptions.CellNotFound:
            raise ValueError
        return int(self.worksheet.row_values(row, value_render_option='UNFORMATTED_VALUE')[1])

    def buy_item(self, item_name, quantity):
        try:
            row = self.worksheet.find(item_name).row
        except gspread.exceptions.CellNotFound:
            raise ValueError
        in_stock = int(self.worksheet.row_values(row)[2])
        if in_stock >= quantity:
            self.worksheet.update_cell(row, 3, (in_stock - quantity))
        else:
            raise ValueError
