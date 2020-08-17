from model.utils import get_sheets_client

class Market:
    def __init__(self, sheet_id=None):
        self.client = get_sheets_client()
        if sheets_id:
            self.sheet = client.open(sheet_id)
        else:
            # create new market sheet
            pass

    def get_all_shops(self):
        pass

    def get_open_shops(self):
        pass

    def get_shop(self, shop):
        pass
