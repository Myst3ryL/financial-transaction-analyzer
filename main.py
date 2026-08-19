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

def get_starting_balance(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Setting"] == "Starting Balance":
                return float(row["Value"])

    return 0.0

def analyze_transactions(filename, starting_balance):
    total_income = 0
    total_expenses = 0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for transaction in reader:
            amount = float(transaction["Amount"])

            if transaction["Type"] == "Income":
                total_income += amount
            elif transaction["Type"] == "Expense":
                total_expenses += amount

    net_income = total_income - total_expenses
    current_balance = starting_balance + total_income - total_expenses

    return total_income, total_expenses, net_income, current_balance

def analyze_categories(filename):
    category_totals = {}

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for transaction in reader:
            if transaction["Type"] == "Expense":
                category = transaction["Category"]
                amount = float(transaction["Amount"])

                if category not in category_totals:
                    category_totals[category] = 0

                category_totals[category] += amount

    return category_totals

def show_category_analysis(filename):
    category_totals = analyze_categories(filename)

    total_expenses = sum(category_totals.values())

    print()
    print("===== EXPENSE BY CATEGORY =====")

    for category, total in category_totals.items():
        percentage = (total / total_expenses) * 100
        print(f"{category:<20} ${total:>8.2f}   {percentage:>6.2f}%")

    largest_category = max(category_totals, key=category_totals.get)
    largest_amount = category_totals[largest_category]

    print()
    print(
        f"Largest Category: {largest_category} "
        f"(${largest_amount:.2f})"
    )

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

def show_summary(filename):
    starting_balance = get_starting_balance("data/settings.csv")
    income, expenses, net_income, balance = analyze_transactions(
        filename,
        starting_balance
    )

    print()
    print("===== FINANCIAL SUMMARY =====")
    print(f"Starting Balance: ${starting_balance:.2f}")
    print(f"Total Income:    ${income:.2f}")
    print(f"Total Expenses:  ${expenses:.2f}")
    print(f"Net Income:      ${net_income:.2f}")
    print(f"Current Balance: ${balance:.2f}")
    


def main():
    filename = "data/transactions.csv"

    while True:
        print()
        print("========================================")
        print("      FINANCIAL TRANSACTION ANALYZER")
        print("========================================")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Financial Summary")
        print("4. Expense by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(filename)

        elif choice == "2":
            view_transactions(filename)

        elif choice == "3":
            show_summary(filename)

        elif choice == "4":
            show_category_analysis(filename)
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.")


main()