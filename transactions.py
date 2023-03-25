''' allows access to sqlite3 '''
import sqlite3

class Transactions():
    ''' class to handle all transactions in given data set '''
    # implemented by robin
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.conn.execute('''CREATE TABLE IF NOT EXISTS transactions
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             item_no INTEGER NOT NULL,
                             amount REAL NOT NULL,
                             category TEXT NOT NULL,
                             date TEXT NOT NULL,
                             description TEXT NOT NULL)''')
        self.conn.commit()

    def show_transactions(self):
        ''' not yet implemented '''

    # implemented by robin
    def add_transaction(self, item_number, amount, category, date, description):
        self.cur.execute("INSERT INTO transactions VALUES (NULL,?,?,?,?,?)", (item_number, amount, category, date, description))
        self.conn.commit()

    # implemented by robin
    def delete_transaction(self, id):
        self.cur.execute("DELETE FROM transactions WHERE id=?", (id,))
        self.conn.commit()

    # implemented by robin
    def summarize_by_date(self):
        self.cur.execute("SELECT date, SUM(amount) FROM transactions GROUP BY date")
        return self.cur.fetchall()

    # implemented by robin
    def summarize_by_month(self):
        self.cur.execute("SELECT strftime('%m', date) AS month, SUM(amount) FROM transactions GROUP BY month")
        return self.cur.fetchall()

    # implemented by robin
    def summarize_by_year(self):
        self.cur.execute("SELECT strftime('%Y', date) AS year, SUM(amount) FROM transactions GROUP BY year")
        return self.cur.fetchall()

    # implemented by robin
    def summarize_by_category(self):
        self.cur.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
        return self.cur.fetchall()

    