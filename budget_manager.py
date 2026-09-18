import csv
import os
from financial_analysis import analyze_categories

BUDGET_HEADERS = ["Category", "Budget"]


def ensure_budget_file_exists(filename):
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(BUDGET_HEADERS)


def load_budgets(filename):
    ensure_budget_file_exists(filename)
    budgets = {}

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                category = row["Category"].strip().title()
                budgets[category] = float(row["Budget"])
            except (ValueError, KeyError):
                continue

    return budgets


def analyze_budgets(transaction_file, budget_file):
    category_totals = analyze_categories(transaction_file)
    budgets = load_budgets(budget_file)
    return category_totals, budgets


def show_budget_status(transaction_file, budget_file):
    category_totals, budgets = analyze_budgets(transaction_file, budget_file)

    print()
    print("===== BUDGET STATUS =====")

    # Union of all budgeted categories and any spent categories
    all_categories = sorted(set(budgets.keys()) | set(category_totals.keys()))

    if not all_categories:
        print("No budget or transaction data found.")
        return

    for category in all_categories:
        budget = budgets.get(category, 0.0)
        spent = category_totals.get(category, 0.0)
        remaining = budget - spent

        if budget == 0.0:
            status = "NO BUDGET SET"
        elif remaining >= 0:
            status = "Under Budget"
        else:
            status = "OVER BUDGET"

        print()
        print(category)
        print(f"Budget:     ${budget:.2f}")
        print(f"Spent:      ${spent:.2f}")
        print(f"Remaining:  ${remaining:.2f}")
        print(f"Status:     {status}")


def set_budget(filename):
    ensure_budget_file_exists(filename)
    category = input("Category: ").strip().title()

    while True:
        try:
            budget = float(input("Budget Amount: $"))
            if budget <= 0:
                print("Budget must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    budgets = load_budgets(filename)
    budgets[category] = budget

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(BUDGET_HEADERS)
        for category_name, amount in sorted(budgets.items()):
            writer.writerow([category_name, amount])

    print(f"Budget for {category} updated successfully!")


def view_budgets(filename):
    budgets = load_budgets(filename)

    print()
    print("===== CURRENT BUDGETS =====")
    if not budgets:
        print("No budgets set yet.")
        return

    for category, amount in sorted(budgets.items()):
        print(f"{category:<20} ${amount:>8.2f}")


def budget_management(transaction_file, budget_file):
    while True:
        print()
        print("===== BUDGET MANAGEMENT =====")
        print("1. Set Budget")
        print("2. View Budgets")
        print("3. Budget Status")
        print("4. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            set_budget(budget_file)
        elif choice == "2":
            view_budgets(budget_file)
        elif choice == "3":
            show_budget_status(transaction_file, budget_file)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose 1-4.")