''' import providing SQL methods '''
from transactions import Transactions

# implemented by robin
# conformed to pylint - Tal Spector
def print_menu():
    ''' Prints the list of available options '''
    print("0. quit")
    print("1. show transactions")
    print("2. add transaction")
    print("3. delete transaction")
    print("4. summarize transactions by date")
    print("5. summarize transactions by month")
    print("6. summarize transactions by year")
    print("7. summarize transactions by category")
    print("8. print this menu")

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
        elif choice == "1":
            show_transactions(transactions)
        elif choice == "2":
            add_transaction(transactions)
        elif choice == "3":
            delete_transaction(transactions)
        elif choice == "4":
            summarize_transactions_by_date(transactions)
        elif choice == "5":
            summarize_transactions_by_month(transactions)
        elif choice == "6":
            summarize_transactions_by_year(transactions)
        elif choice == "7":
            summarize_transactions_by_category(transactions)
        elif choice == "8":
            print_menu()
        else:
            print("Not a valid input!")

# implemented by robin
# conformed to pylint - Tal Spector
def show_transactions(transaction):
    ''' shows all transactions '''
    print("transactions: ")
    for transaction in transaction.show_transactions():
        print(transaction)

# implemented by robin
# conformed to pylint - Tal Spector
def add_transaction(transaction):
    ''' adds a transaction '''
    item_number = int(input("Item number: "))
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = input("Enter date (yyyy-mm-dd): ")
    description = input("Enter description: ")
    transaction.add_transaction(item_number, amount, category, date, description)

# implemented by robin
# conformed to pylint - Tal Spector
def delete_transaction(transaction):
    ''' deletes a transaction '''
    ident = int(input("Enter ID: "))
    transaction.delete_transaction(ident)

# implemented by robin
# conformed to pylint - Tal Spector
def summarize_transactions_by_date(transaction):
    ''' summarizes transactions by date '''
    for date, total in transaction.summarize_by_date():
        print(f"{date}: {total}")

# implemented by robin
# conformed to pylint - Tal Spector
def summarize_transactions_by_month(transactions):
    ''' summarizes transcations by month '''
    for month, total in transactions.summarize_by_month():
        print(f"{month}: {total}")

# implemented by robin
# conformed to pylint - Tal Spector
def summarize_transactions_by_year(transactions):
    ''' summarizes transactions by year '''
    for year, total in transactions.summarize_by_year():
        print(f"{year}: {total}")

# implemented by robin
# conformed to pylint - Tal Spector
def summarize_transactions_by_category(transactions):
    ''' summarizes transactions by category '''
    for category, total in transactions.summarize_by_category():
        print(f"{category}: {total}")

# implemented by robin
# conformed to pylint - Tal Spector
def main():
    ''' runs tracker '''
    run_tracker()


main()
