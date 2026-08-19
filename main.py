import csv


def add_transaction(filename):
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    description = input("Description: ")
    amount = float(input("Amount: $"))
    transaction_type = input("Type (Income/Expense): ")

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


def analyze_transactions(filename):
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
    current_balance = total_income - total_expenses

    return total_income, total_expenses, net_income, current_balance

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
    income, expenses, net_income, balance = analyze_transactions(filename)

    print()
    print("===== FINANCIAL SUMMARY =====")
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
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(filename)

        elif choice == "2":
            view_transactions(filename)

        elif choice == "3":
            show_summary(filename)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


main()