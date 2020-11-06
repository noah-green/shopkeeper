import gspread
import datetime

class Ledger:
    """Manages a gspread.models.Worksheet object representing a ledger."""

    def __init__(self, worksheet):
        self.worksheet = worksheet

    async def record_purchase(self, purchase):
        self.worksheet.append_row((purchase))
