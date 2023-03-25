import os
from transactions import transactions

# implemented by robin
def print_menu():
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
def run_tracker():
    db_filename = input("Enter database filename: ")
    transactions = transactions(db_filename)

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            show_catagories(transactions)
        elif choice == "2":
            add_catagory(transactions)
        elif choice == "3":
            modify_catagory(transactions)
        elif choice == "4":
            show_transactions(transactions)
        elif choice == "5":
            add_transaction(transactions)
        elif choice == "6":
            delete_transaction(transactions)
        elif choice == "7":
            summarize_transactions_by_date(transactions)
        elif choice == "8":
            summarize_transactions_by_month(transactions)
        elif choice == "9":
            summarize_transactions_by_year(transactions)
        elif choice == "10":
            summarize_transactions_by_category
        elif choice == "11":
            print_menu()
        else:
            print("Not a valid input!")
            run_tracker()
    
# implemented by robin
def show_catagories(transaction):
    print("Categories: ")
    for category in transactions.get_categories():
        print(category + "\n")

# implemented by robin
def add_catagory(transaction):
    category = input("Enter category name: ")
    transactions.add_category(category)

# implemented by robin
def modify_catagory(transaction):
    previous = input("Previous category: ")
    new = input("New category: ")
    transactions.modify_category(previous, new)

# implemented by robin
def show_transactions(transaction):
    print("Transactions: ")
    for transaction in transactions.get_transactions():
        print(transaction + "\n")

# implemented by robin
def add_transaction(transaction):
    item_number = int(input("Item number: "))
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = input("Enter date (yyyy-mm-dd): ")
    description = input("Enter description: ")
    transactions.add_transaction(item_number, amount, category, date, description)

# implemented by robin
def delete_transaction(transaction):
    item_number = int(input("Enter item number to delete: "))
    transactions.delete_transaction(item_number)

# implemented by robin
def summarize_transactions_by_date(transaction):
    for date, total in transactions.summarize_by_date().items():
        print(f"{date}: {total}")

# implemented by robin
def summarize_transactions_by_month(transactions):
    for month, total in transactions.summarize_by_month().items():
        print(f"{month}: {total}")

# implemented by robin
def summarize_transactions_by_year(transactions):
    for year, total in transactions.summarize_by_year().items():
        print(f"{year}: {total}")

# implemented by robin
def summarize_transactions_by_category(transactions):
    for category, total in transactions.summarize_by_category().items():
        print(f"{category}: {total}")

# implemented by robin
def main():
    run_tracker()

main()