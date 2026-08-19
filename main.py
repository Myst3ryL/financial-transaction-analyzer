import csv


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

    return total_income, total_expenses, net_income


print("Financial Transaction Analyzer")

income, expenses, net_income = analyze_transactions(
    "data/transactions.csv"
)

print()
print("===== FINANCIAL SUMMARY =====")
print(f"Total Income:   ${income:.2f}")
print(f"Total Expenses: ${expenses:.2f}")
print(f"Net Income:     ${net_income:.2f}")