import sqlite3
import os

class transactions():
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


    

    
        
