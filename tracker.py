''' import providing SQL methods '''
from transactions import Transactions

# implemented by robin
# conformed to pylint - Tal Spector
def print_menu():
    ''' Prints the list of available options '''
    print("0. quit")
    print("1. show categories")
    print("2. add category")
    print("3. modify category")
    print("4. show transactions")
    print("5. add transaction")
    print("6. delete transaction")
    print("7. summarize transactions by date")
    print("8. summarize transactions by month")
    print("9. summarize transactions by year")
    print("10. summarize transactions by category")
    print("11. print this menu")

# implemented by robin
# conformed to pylint - Tal Spector
def run_tracker():
    ''' runs the tracker '''
    db_filename = input("Enter database filename: ")
    transactions = Transactions(db_filename)

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "0":
            break
        if choice == "1":
            show_catagories(transactions)
        if choice == "2":
            add_catagory(transactions)
        if choice == "3":
            modify_catagory(transactions)
        if choice == "4":
            show_transactions(transactions)
        if choice == "5":
            add_transaction(transactions)
        if choice == "6":
            delete_transaction(transactions)
        if choice == "7":
            summarize_transactions_by_date(transactions)
        if choice == "8":
            summarize_transactions_by_month(transactions)
        if choice == "9":
            summarize_transactions_by_year(transactions)
        if choice == "10":
            summarize_transactions_by_category(transactions)
        if choice == "11":
            print_menu()
        else:
            print("Not a valid input!")

# implemented by robin
# conformed to pylint - Tal Spector
def show_catagories(self):
    ''' shows the list of availbale categories '''
    print("Categories: ")
    for category in Transactions.show_categories():
        print(category + "\n")

# implemented by robin
# conformed to pylint - Tal Spector
def add_catagory(transaction):
    ''' adds a category '''
    category = input("Enter category name: ")
    transaction.add_category(category)

# implemented by robin
# conformed to pylint - Tal Spector
def modify_catagory(transaction):
    ''' modify an existing category '''
    previous = input("Previous category: ")
    new = input("New category: ")
    transaction.modify_category(previous, new)

# implemented by robin
# conformed to pylint - Tal Spector
def show_transactions(transaction):
    ''' shows all transactions '''
    print("transactions: ")
    for transaction in transaction.get_transactions():
        print(transaction + "\n")

# implemented by robin
# conformed to pylint - Tal Spector
def add_transaction(transaction):
    ''' adds a transaction '''
    item_number = int(input("Item number: "))
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = input("Enter date (yyyy-mm-dd): ")
    description = input("Enter description: ")
    transaction.add_transaction(
        item_number, amount, category, date, description)

# implemented by robin
# conformed to pylint - Tal Spector
def delete_transaction(transaction):
    ''' deletes a transaction '''
    id = int(input("Enter ID: "))
    transaction.delete_transaction(id)

# implemented by robin
# conformed to pylint - Tal Spector
def summarize_transactions_by_date(transaction):
    ''' summarizes transactions by date '''
    for date, total in transaction.summarize_by_date().items():
        print(f"{date}: {total}")

# implemented by robin
# conformed to pylint - Tal Spector
def summarize_transactions_by_month(transactions):
    ''' summarizes transcations by month '''
    for month, total in transactions.summarize_by_month().items():
        print(f"{month}: {total}")

# implemented by robin
# conformed to pylint - Tal Spector
def summarize_transactions_by_year(transactions):
    ''' summarizes transactions by year '''
    for year, total in transactions.summarize_by_year().items():
        print(f"{year}: {total}")

# implemented by robin
# conformed to pylint - Tal Spector
def summarize_transactions_by_category(transactions):
    ''' summarizes transactions by category '''
    for category, total in transactions.summarize_by_category().items():
        print(f"{category}: {total}")

# implemented by robin
# conformed to pylint - Tal Spector
def main():
    ''' runs tracker '''
    run_tracker()


main()
