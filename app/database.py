import sqlite3

class Database:
    def __init__(self, db_name="commands.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS history (command TEXT)")
        self.conn.commit()

    def save_command(self, command):
        self.cursor.execute("INSERT INTO history (command) VALUES (?)", (command,))
        self.conn.commit()

    def get_history(self):
        self.cursor.execute("SELECT command FROM history")
        return [row[0] for row in self.cursor.fetchall()]
