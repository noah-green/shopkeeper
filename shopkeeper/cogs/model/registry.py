from .utils import get_db, get_sheets_client
from .market import Market

class Registry:
    """Manage a database connection and a gspread client."""
    def __init__(self):
        self.conn = get_db()
        self.client = get_sheets_client()

    def create_market(self, guild):
        """Create a Market spreadsheet associated with the given guild id."""
        query = 'INSERT INTO guilds(guild, sheet_id) VALUES (?,?)'
        spreadsheet = self.client.copy('1SaU9ppkjOSSxhKE0wO1KN7VZQwH7CHMejUVlJ68R1ys', f'{guild.name} Market')
        self.conn.cursor().execute(query, (guild.id, spreadsheet.id))

    def share_market(self, guild, email):
        """Share the market sheet correspoinding to the current guild."""
        query = 'SELECT sheet_id FROM guilds WHERE guild=?'
        cursor = self.conn.cursor()
        sheet_id = cursor.execute(query, (guild.id,)).fetchone()[0]
        self.client.open_by_key(sheet_id).share(email, perm_type='user', role='writer')

    def get_market(self, guild):
        """Retrieve the market sheet corresponding to the given guild."""
        query = 'SELECT sheet_id FROM guilds WHERE guild=?'
        record = self.conn.cursor().execute(query, (guild.id,)).fetchone()
        if record:
            return Market(self.client.open_by_key(record[0]))
        else:
            return None
