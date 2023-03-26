''' testing based imports '''
from transactions import Transactions
import pytest

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

# implemented by dakota
def test_add_transaction():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2023-03-01", "Lunch")
    assert transactions.show_transactions() == [(1, 1, 50.0, "Food", "2023-03-01", "Lunch")]

# implemented by dakota
def test_delete_transaction():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2023-03-01", "Lunch")
    transactions.delete_transaction(1)
    assert transactions.show_transactions() == []

# implemented by dakota
def test_summarize_by_date():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2023-03-01", "Lunch")
    transactions.add_transaction(2, 100, "Shopping", "2023-03-01", "New shoes")
    transactions.add_transaction(3, 25, "Food", "2023-03-02", "Coffee")
    assert transactions.summarize_by_date() == [("2023-03-01", 150.0), ("2023-03-02", 25.0)]

# implemented by dakota
 def test_summarize_by_month():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2023-03-01", "Lunch")
    transactions.add_transaction(2, 100, "Shopping", "2023-03-02", "New shoes")
    transactions.add_transaction(3, 25, "Food", "2023-04-03", "Coffee")
    assert transactions.summarize_by_month() == [("03", 150.0), ("04", 25.0)]

# implemented by dakota
def test_summarize_by_year():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2022-03-01", "Lunch")
    transactions.add_transaction(2, 100, "Shopping", "2022-03-02", "New shoes")
    transactions.add_transaction(3, 25, "Food", "2023-04-03", "Coffee")
    assert transactions.summarize_by_year() == [("2022", 150.0), ("2023", 25.0)]

# implemented by dakota
def test_summarize_by_category():
    transactions = Transactions("test.db")
    transactions.add_transaction(1, 50, "Food", "2023-03-01", "
