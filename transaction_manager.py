import csv
from datetime import datetime


def add_transaction(filename):
    while True:
        date = input("Date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")

    category = input("Category: ")
    description = input("Description: ")

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
        transaction_type = input(
            "Type (Income/Expense): "
        ).strip().title()

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
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        print()
        print("===== TRANSACTIONS =====")

        for transaction in reader:
            print(
                f"{transaction['Date']} | "
                f"{transaction['Category']} | "
                f"{transaction['Description']} | "
                f"${float(transaction['Amount']):.2f} | "
                f"{transaction['Type']}"
            )