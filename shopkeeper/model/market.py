from model.utils import get_sheets_client

class Market:
    def __init__(self, sheet_id=None):
        print(sheet_id)
        self.client = get_sheets_client()
        if sheet_id:
            self.sheet = self.client.open_by_key(sheet_id)
        else:
            # copy the template spreadhsheet TODO: make this not hardcoded
            self.sheet = self.client.copy('1SaU9ppkjOSSxhKE0wO1KN7VZQwH7CHMejUVlJ68R1ys', 'Market')

    def share_sheet(self, email):
        self.sheet.share(email, perm_type='user', role='writer')

    def get_sheet_id(self):
        return self.sheet.id

    def get_all_shops(self):
        return self.sheet.worksheet('Shop List').col_values(1)[1:]

    def get_open_shops(self):
        pass

    def get_shop(self, shop):
        pass
