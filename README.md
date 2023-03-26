# cs103aPA03

# This program is a finance tracker utilizing SQL, pytest, and pylint.  


# We used SQLite to help us write queries to peform the operations create, read, update, and delete. We created a file called Transaction.py in which we stored financial transactions with the fields: 'item #', 'amount', 'category', 'date', 'discrption'. The user is allowed to read and update the database. We also have another file called tracker.py which offers the user to do the follwing options: show transactions, add transactions, delete transactions, summarize transactions by date, summarize transactions by month, summarize transactions by year, summarize transactions by category, and print this menu. We also have a test file called test_transaction.py that provides pytests for the transaction class. 