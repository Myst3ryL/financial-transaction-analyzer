import csv
from datetime import datetime


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
    current_balance = (
        starting_balance
        + total_income
        - total_expenses
    )

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


def show_summary(filename):
    starting_balance = get_starting_balance(
        "data/settings.csv"
    )

    income, expenses, net_income, balance = analyze_transactions(
        filename,
        starting_balance
    )

    print()
    print("===== FINANCIAL SUMMARY =====")
    print(f"Starting Balance: ${starting_balance:.2f}")
    print(f"Total Income:     ${income:.2f}")
    print(f"Total Expenses:   ${expenses:.2f}")
    print(f"Net Income:       ${net_income:.2f}")
    print(f"Current Balance:  ${balance:.2f}")


def show_category_analysis(filename):
    category_totals = analyze_categories(filename)

    total_expenses = sum(category_totals.values())

    print()
    print("===== EXPENSE BY CATEGORY =====")

    for category, total in category_totals.items():
        percentage = (total / total_expenses) * 100

        print(
            f"{category:<20} "
            f"${total:>8.2f} "
            f"{percentage:>6.2f}%"
        )

    largest_category = max(
        category_totals,
        key=category_totals.get
    )

    largest_amount = category_totals[largest_category]

    print()
    print(
        f"Largest Category: {largest_category} "
        f"(${largest_amount:.2f})"
    )


def analyze_month(filename, selected_month):
    monthly_income = 0
    monthly_expenses = 0

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for transaction in reader:
            if transaction["Date"].startswith(selected_month):
                amount = float(transaction["Amount"])

                if transaction["Type"] == "Income":
                    monthly_income += amount

                elif transaction["Type"] == "Expense":
                    monthly_expenses += amount

    monthly_net = monthly_income - monthly_expenses

    return monthly_income, monthly_expenses, monthly_net


def show_monthly_analysis(filename):
    while True:
        selected_month = input(
            "Enter month (YYYY-MM): "
        )

        try:
            datetime.strptime(selected_month, "%Y-%m")
            break

        except ValueError:
            print(
                "Please enter a valid month "
                "in YYYY-MM format."
            )

    income, expenses, net_income = analyze_month(
        filename,
        selected_month
    )

    print()
    print("===== MONTHLY ANALYSIS =====")
    print(f"Month:          {selected_month}")
    print(f"Income:         ${income:.2f}")
    print(f"Expenses:       ${expenses:.2f}")
    print(f"Net Income:     ${net_income:.2f}")


def calculate_insights(filename):
    total_income = 0
    total_expenses = 0
    expense_count = 0
    income_count = 0

    largest_expense = 0
    largest_expense_description = ""

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for transaction in reader:
            amount = float(transaction["Amount"])

            if transaction["Type"] == "Income":
                total_income += amount
                income_count += 1

            elif transaction["Type"] == "Expense":
                total_expenses += amount
                expense_count += 1

                if amount > largest_expense:
                    largest_expense = amount
                    largest_expense_description = (
                        transaction["Description"]
                    )

    if total_income > 0:
        savings_rate = (
            (total_income - total_expenses)
            / total_income
        ) * 100
    else:
        savings_rate = 0

    if expense_count > 0:
        average_expense = (
            total_expenses / expense_count
        )
    else:
        average_expense = 0

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
        largest_category = max(
            category_totals,
            key=category_totals.get
        )

        largest_category_amount = (
            category_totals[largest_category]
        )
    else:
        largest_category = "None"
        largest_category_amount = 0

    print()
    print("===== FINANCIAL INSIGHTS =====")
    print(f"Savings Rate:          {savings_rate:.2f}%")
    print(
        f"Largest Expense:       "
        f"${largest_expense:.2f} "
        f"({largest_expense_description})"
    )
    print(
        f"Largest Category:      "
        f"${largest_category_amount:.2f} "
        f"({largest_category})"
    )
    print(f"Average Expense:       ${average_expense:.2f}")
    print(f"Income Transactions:   {income_count}")
    print(f"Expense Transactions:  {expense_count}")