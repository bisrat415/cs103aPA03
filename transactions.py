''' allows access to sqlite3 '''
import sqlite3

class Transactions():
    ''' class to handle all transactions in given data set '''
    # implemented by robin
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS transactions
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             item_no INTEGER NOT NULL,
                             amount REAL NOT NULL,
                             category TEXT NOT NULL,
                             date TEXT NOT NULL,
                             description TEXT NOT NULL)''')
        self.conn.commit()

    def get_categories(self):
        ''' not yet implemented '''

    def add_categories(self, category):
        ''' not yet implemented '''

    def modify_category(self, previous, new):
        ''' not yet implemented '''

    def get_transactions(self):
        ''' not yet implemented '''

    def add_transaction(self, item_number, amount, category, date, description):
        ''' not yet implemented '''

    def delete_transaction(self, item_number):
        ''' not yet implemented '''

    def summarize_by_date(self):
        ''' not yet implemented '''

    def summarize_by_month(self):
        ''' not yet implemented '''

    def summarize_by_year(self):
        ''' not yet implemented '''

    def summarize_by_category(self):
        ''' not yet implemented '''