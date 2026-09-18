import csv
from datetime import datetime
import os


def get_starting_balance(filename="data/settings.csv"):
    if not os.path.exists(filename):
        return 0.0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get("Setting") == "Starting Balance":
                try:
                    return float(row.get("Value", 0))
                except ValueError:
                    return 0.0

    return 0.0


def analyze_transactions(filename, starting_balance):
    total_income = 0.0
    total_expenses = 0.0

    if not os.path.exists(filename):
        return total_income, total_expenses, 0.0, starting_balance

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for transaction in reader:
            try:
                amount = float(transaction["Amount"])
            except (ValueError, KeyError):
                continue

            trans_type = transaction.get("Type", "").strip().title()
            if trans_type == "Income":
                total_income += amount
            elif trans_type == "Expense":
                total_expenses += amount

    net_income = total_income - total_expenses
    current_balance = starting_balance + net_income

    return total_income, total_expenses, net_income, current_balance


def analyze_categories(filename):
    category_totals = {}

    if not os.path.exists(filename):
        return category_totals

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for transaction in reader:
            trans_type = transaction.get("Type", "").strip().title()
            if trans_type == "Expense":
                category = transaction.get("Category", "Uncategorized").strip().title()
                try:
                    amount = float(transaction["Amount"])
                except (ValueError, KeyError):
                    continue

                category_totals[category] = category_totals.get(category, 0.0) + amount

    return category_totals


def show_summary(filename, settings_file="data/settings.csv"):
    starting_balance = get_starting_balance(settings_file)
    income, expenses, net_income, balance = analyze_transactions(filename, starting_balance)

    print()
    print("===== FINANCIAL SUMMARY =====")
    print(f"Starting Balance: ${starting_balance:.2f}")
    print(f"Total Income:     ${income:.2f}")
    print(f"Total Expenses:   ${expenses:.2f}")
    print(f"Net Income:       ${net_income:.2f}")
    print(f"Current Balance:  ${balance:.2f}")


def show_category_analysis(filename):
    category_totals = analyze_categories(filename)

    print()
    print("===== EXPENSE BY CATEGORY =====")
    if not category_totals:
        print("No expenses recorded.")
        return

    total_expenses = sum(category_totals.values())

    for category, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        percentage = (total / total_expenses) * 100 if total_expenses > 0 else 0.0
        print(f"{category:<20} ${total:>8.2f} {percentage:>6.2f}%")

    largest_category = max(category_totals, key=category_totals.get)
    largest_amount = category_totals[largest_category]

    print()
    print(f"Largest Category: {largest_category} (${largest_amount:.2f})")


def analyze_month(filename, selected_month):
    monthly_income = 0.0
    monthly_expenses = 0.0

    if not os.path.exists(filename):
        return monthly_income, monthly_expenses, 0.0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for transaction in reader:
            date_val = transaction.get("Date", "").strip()
            if date_val.startswith(selected_month):
                try:
                    amount = float(transaction["Amount"])
                except (ValueError, KeyError):
                    continue

                trans_type = transaction.get("Type", "").strip().title()
                if trans_type == "Income":
                    monthly_income += amount
                elif trans_type == "Expense":
                    monthly_expenses += amount

    monthly_net = monthly_income - monthly_expenses
    return monthly_income, monthly_expenses, monthly_net


def show_monthly_analysis(filename):
    while True:
        selected_month = input("Enter month (YYYY-MM): ").strip()
        try:
            datetime.strptime(selected_month, "%Y-%m")
            break
        except ValueError:
            print("Please enter a valid month in YYYY-MM-DD/YYYY-MM format.")

    income, expenses, net_income = analyze_month(filename, selected_month)

    print()
    print("===== MONTHLY ANALYSIS =====")
    print(f"Month:          {selected_month}")
    print(f"Income:         ${income:.2f}")
    print(f"Expenses:       ${expenses:.2f}")
    print(f"Net Income:     ${net_income:.2f}")


def calculate_insights(filename):
    total_income = 0.0
    total_expenses = 0.0
    expense_count = 0
    income_count = 0

    largest_expense = 0.0
    largest_expense_description = "None"

    if not os.path.exists(filename):
        return 0.0, 0.0, "None", 0.0, 0, 0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for transaction in reader:
            try:
                amount = float(transaction["Amount"])
            except (ValueError, KeyError):
                continue

            trans_type = transaction.get("Type", "").strip().title()
            if trans_type == "Income":
                total_income += amount
                income_count += 1
            elif trans_type == "Expense":
                total_expenses += amount
                expense_count += 1

                if amount > largest_expense:
                    largest_expense = amount
                    largest_expense_description = transaction.get("Description", "").strip()

    savings_rate = ((total_income - total_expenses) / total_income * 100) if total_income > 0 else 0.0
    average_expense = (total_expenses / expense_count) if expense_count > 0 else 0.0

    return (
        savings_rate,
        largest_expense,
        largest_expense_description,
        average_expense,
        income_count,
        expense_count
    )


def show_insights(filename):
    (
        savings_rate,
        largest_expense,
        largest_expense_description,
        average_expense,
        income_count,
        expense_count
    ) = calculate_insights(filename)

    category_totals = analyze_categories(filename)

    if category_totals:
        largest_category = max(category_totals, key=category_totals.get)
        largest_category_amount = category_totals[largest_category]
    else:
        largest_category = "None"
        largest_category_amount = 0.0

    print()
    print("===== FINANCIAL INSIGHTS =====")
    print(f"Savings Rate:          {savings_rate:.2f}%")
    print(f"Largest Expense:       ${largest_expense:.2f} ({largest_expense_description})")
    print(f"Largest Category:      ${largest_category_amount:.2f} ({largest_category})")
    print(f"Average Expense:       ${average_expense:.2f}")
    print(f"Income Transactions:   {income_count}")
    print(f"Expense Transactions:  {expense_count}")