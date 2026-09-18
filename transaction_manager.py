import csv
from datetime import datetime
import os

HEADERS = ["Date", "Category", "Description", "Amount", "Type"]


def ensure_file_exists(filename):
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(HEADERS)


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
            amount,
            transaction_type
        ])

    print("Transaction added successfully!")


def view_transactions(filename):
    ensure_file_exists(filename)

    with open(filename, "r") as file:
        reader = list(csv.DictReader(file))

        print()
        print("===== TRANSACTIONS =====")
        if not reader:
            print("No transactions found.")
            return

        for transaction in reader:
            category = transaction["Category"].strip().title()
            print(
                f"{transaction['Date']} | "
                f"{category:<15} | "
                f"{transaction['Description']:<20} | "
                f"${float(transaction['Amount']):>8.2f} | "
                f"{transaction['Type']}"
            )