'''
There should be an __init__ method where you pass in the filename for the database to be used (e.g. tracker.db) 
and each transaction should have the following fields stored in a SQL table called transactions.

'item #',
'amount',
'category',
'date',
'description'


TEMPORARY: (ROBIN) I JUST COPIED THINGS FROM HIS LESSON 19 CODE 
'''
import sqlite3
import os

class tracker():
    def __init__(self):
        return

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/todo.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        # return [toDict(t) for t in tuples]

    
        
