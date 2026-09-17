import csv
import matplotlib.pyplot as plt


def plot_expenses_by_category(filename):
    category_totals = {}

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Type"] == "Expense":
                category = row["Category"]
                amount = float(row["Amount"])

                category_totals[category] = (
                    category_totals.get(category, 0) + amount
                )

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts)

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_income_vs_expenses(filename):
    total_income = 0
    total_expenses = 0

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["Amount"])

            if row["Type"] == "Income":
                total_income += amount
            elif row["Type"] == "Expense":
                total_expenses += amount

    categories = ["Income", "Expenses"]
    amounts = [total_income, total_expenses]

    plt.figure(figsize=(8, 6))
    plt.bar(categories, amounts)

    plt.title("Income vs. Expenses")
    plt.xlabel("Type")
    plt.ylabel("Amount ($)")

    plt.tight_layout()
    plt.show()

def plot_monthly_trends(filename):
    monthly_totals = {}

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Type"] == "Expense":
                month = row["Date"][:7]
                amount = float(row["Amount"])

                monthly_totals[month] = (
                    monthly_totals.get(month, 0) + amount
                )

    months = sorted(monthly_totals.keys())
    amounts = [monthly_totals[month] for month in months]

    plt.figure(figsize=(10, 6))
    plt.plot(months, amounts, marker="o")

    plt.title("Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Amount ($)")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    