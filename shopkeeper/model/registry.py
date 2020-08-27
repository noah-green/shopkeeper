from model.utils import get_db
from model.market import Market

class Registry:
    def __init__(self):
        self.conn = get_db()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def create_market(self, guild):
        """Create a Market spreadsheet associated with the given guild id."""
        query = 'INSERT INTO guilds(guild, sheet_id) VALUES (?,?)'
        self.conn.cursor().execute(query, (guild, Market().get_sheet_id()))

    def share_market(self, guild, email):
        query = 'SELECT sheet_id FROM guilds WHERE guild=?'
        cursor = self.conn.cursor()
        sheet_id = cursor.execute(query, (guild,)).fetchone()[0]
        Market(sheet_id).share_sheet(email)

    def get_market(self, guild):
        query = 'SELECT sheet_id FROM guilds WHERE guild=?'
        record = self.conn.cursor().execute(query, (guild,)).fetchone()
        if record:
            return Market(sheet_id[0])
        else:
            return None
