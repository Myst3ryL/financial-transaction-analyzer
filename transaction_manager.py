import csv
from datetime import datetime
import os

HEADERS = ["Date", "Category", "Description", "Amount", "Type"]


def ensure_file_exists(filename):
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(HEADERS)


def load_all_transactions(filename):
    ensure_file_exists(filename)
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_all_transactions(filename, transactions):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(HEADERS)
        for t in transactions:
            writer.writerow([
                t["Date"],
                t["Category"],
                t["Description"],
                t["Amount"],
                t["Type"]
            ])


def add_transaction(filename):
    ensure_file_exists(filename)

    while True:
        date = input("Date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")

    category = input("Category: ").strip().title()
    description = input("Description: ").strip()

    while True:
        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        transaction_type = input("Type (Income/Expense): ").strip().title()
        if transaction_type in ["Income", "Expense"]:
            break
        print("Please enter either Income or Expense.")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow([
            date,
            category,
            description,
            f"{amount:.2f}",
            transaction_type
        ])

    print("Transaction added successfully!")


def view_transactions(filename, transactions=None):
    if transactions is None:
        transactions = load_all_transactions(filename)

    print()
    print("===== TRANSACTIONS =====")
    if not transactions:
        print("No transactions found.")
        return

    print(f"{'#':<4} | {'Date':<10} | {'Category':<15} | {'Description':<20} | {'Amount':>10} | {'Type'}")
    print("-" * 75)

    for idx, t in enumerate(transactions, start=1):
        category = t["Category"].strip().title()
        print(
            f"{idx:<4} | "
            f"{t['Date']} | "
            f"{category:<15} | "
            f"{t['Description']:<20} | "
            f"${float(t['Amount']):>9.2f} | "
            f"{t['Type']}"
        )


def search_transactions(filename):
    transactions = load_all_transactions(filename)
    if not transactions:
        print("\nNo transactions available to search.")
        return

    keyword = input("\nEnter search keyword (category or description): ").strip().lower()

    matches = [
        t for t in transactions
        if keyword in t["Category"].lower() or keyword in t["Description"].lower()
    ]

    print(f"\nFound {len(matches)} match(es) for '{keyword}':")
    view_transactions(filename, transactions=matches)


def edit_transaction(filename):
    transactions = load_all_transactions(filename)
    if not transactions:
        print("\nNo transactions available to edit.")
        return

    view_transactions(filename, transactions)

    while True:
        choice = input("\nEnter transaction # to edit (or 'c' to cancel): ").strip()
        if choice.lower() == 'c':
            return
        if choice.isdigit() and 1 <= int(choice) <= len(transactions):
            idx = int(choice) - 1
            break
        print("Invalid number. Please enter a listed index.")

    target = transactions[idx]
    print(f"\nEditing: {target['Date']} | {target['Category']} | {target['Description']} | ${target['Amount']} | {target['Type']}")
    print("Press Enter on any prompt to keep the existing value.")

    # 1. Date
    new_date = input(f"Date [{target['Date']}]: ").strip()
    if new_date:
        while True:
            try:
                datetime.strptime(new_date, "%Y-%m-%d")
                target["Date"] = new_date
                break
            except ValueError:
                new_date = input("Invalid format. Date (YYYY-MM-DD): ").strip()

    # 2. Category
    new_cat = input(f"Category [{target['Category']}]: ").strip()
    if new_cat:
        target["Category"] = new_cat.title()

    # 3. Description
    new_desc = input(f"Description [{target['Description']}]: ").strip()
    if new_desc:
        target["Description"] = new_desc

    # 4. Amount
    new_amt = input(f"Amount [${target['Amount']}]: ").strip().replace("$", "")
    if new_amt:
        while True:
            try:
                val = float(new_amt)
                if val <= 0:
                    raise ValueError
                target["Amount"] = f"{val:.2f}"
                break
            except ValueError:
                new_amt = input("Please enter a valid positive number: ").strip().replace("$", "")

    # 5. Type
    new_type = input(f"Type [{target['Type']}]: ").strip().title()
    if new_type:
        while new_type not in ["Income", "Expense"]:
            new_type = input("Must be 'Income' or 'Expense': ").strip().title()
        target["Type"] = new_type

    transactions[idx] = target
    save_all_transactions(filename, transactions)
    print("Transaction updated successfully!")


def delete_transaction(filename):
    transactions = load_all_transactions(filename)
    if not transactions:
        print("\nNo transactions available to delete.")
        return

    view_transactions(filename, transactions)

    while True:
        choice = input("\nEnter transaction # to delete (or 'c' to cancel): ").strip()
        if choice.lower() == 'c':
            return
        if choice.isdigit() and 1 <= int(choice) <= len(transactions):
            idx = int(choice) - 1
            break
        print("Invalid number. Please enter a listed index.")

    target = transactions[idx]
    confirm = input(f"Are you sure you want to delete '{target['Description']}' (${target['Amount']})? (y/n): ").strip().lower()

    if confirm == "y":
        deleted = transactions.pop(idx)
        save_all_transactions(filename, transactions)
        print(f"Deleted transaction: {deleted['Description']} (${deleted['Amount']})")
    else:
        print("Deletion cancelled.")


def transaction_operations_menu(filename):
    while True:
        print()
        print("===== TRANSACTION OPERATIONS =====")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. Search Transactions")
        print("4. Edit Transaction")
        print("5. Delete Transaction")
        print("6. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_transaction(filename)
        elif choice == "2":
            view_transactions(filename)
        elif choice == "3":
            search_transactions(filename)
        elif choice == "4":
            edit_transaction(filename)
        elif choice == "5":
            delete_transaction(filename)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose 1-6.")