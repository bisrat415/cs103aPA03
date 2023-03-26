''' testing based imports '''
from transactions import Transactions
import pytest
import os


# implemented by dakota
def test_init():
    transactions = Transactions("test.db")
    assert transactions is not None

# implemented by dakota
def test_show_transactions():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2023-03-01", "Lunch")
    transactions.add_transaction(2, 100, "Shopping", "2023-03-02", "New shoes")
    assert transactions.show_transactions() == [(1, 1, 50.0, "Food", "2023-03-01", "Lunch"),(2, 2, 100.0, "Shopping", "2023-03-02", "New shoes")]
    os.remove("test.db")

# implemented by dakota
# bug fixed by bisrat
def test_add_transaction():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2023-03-01", "Lunch")
    assert transactions.show_transactions() == [(1, 1, 50.0, "Food", "2023-03-01", "Lunch")]
    os.remove("test.db")

# implemented by dakota
# bug fixed by bisrat
def test_delete_transaction():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2023-03-01", "Lunch")
    transactions.delete_transaction(1)
    assert transactions.show_transactions() == []
    os.remove("test.db")

# implemented by dakota
# bug fixed by bisrat
def test_summarize_by_date():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2023-03-01", "Lunch")
    transactions.add_transaction(2, 100, "Shopping", "2023-03-01", "New shoes")
    transactions.add_transaction(3, 25, "Food", "2023-03-02", "Coffee")
    assert transactions.summarize_by_date() == [("2023-03-01", 150.0), ("2023-03-02", 25.0)]
    os.remove("test.db")

# implemented by dakota
# bug fixed by bisrat
def test_summarize_by_month():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2023-03-01", "Lunch")
    transactions.add_transaction(2, 100, "Shopping", "2023-03-02", "New shoes")
    transactions.add_transaction(3, 25, "Food", "2023-04-03", "Coffee")
    assert transactions.summarize_by_month() == [("03", 150.0), ("04", 25.0)]
    os.remove("test.db")

# implemented by dakota
# bug fixed by bisrat
def test_summarize_by_year():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2022-03-01", "Lunch")
    transactions.add_transaction(2, 100, "Shopping", "2022-03-02", "New shoes")
    transactions.add_transaction(3, 25, "Food", "2023-04-03", "Coffee")
    assert transactions.summarize_by_year() == [("2022", 150.0), ("2023", 25.0)]
    os.remove("test.db")

# implemented by dakota
# bug fixed by bisrat
def test_summarize_by_category():
    # Create a Transactions object and add some transactions
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 10.0, 'groceries', '2022-03-24', 'Bought some food')
    transactions.add_transaction(2, 20.0, 'entertainment', '2022-03-25', 'Bought movie tickets')
    transactions.add_transaction(3, 5.0, 'groceries', '2022-03-25', 'Bought some milk')
    
    # Call the summarize_by_category() method
    summary = transactions.summarize_by_category()
    
    # Check that the result is a list of tuples
    assert isinstance(summary, list)
    assert all(isinstance(item, tuple) for item in summary)
    
    # Check that the summary includes the expected categories and amounts
    expected = [('groceries', 15.0), ('entertainment', 20.0)]
    assert set(summary) == set(expected)
    
    # Clean up the test database
    os.remove('test.db')

