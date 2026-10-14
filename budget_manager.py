import csv
import os
from datetime import datetime
from financial_analysis import analyze_categories_by_month

BUDGET_HEADERS = ["Month", "Category", "Budget"]

def ensure_budget_file_exists(filename):
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(BUDGET_HEADERS)

def load_all_budgets(filename):
    ensure_budget_file_exists(filename)
    budgets = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                budgets.append({
                    "Month": row["Month"].strip(),
                    "Category": row["Category"].strip().title(),
                    "Budget": float(row["Budget"])
                })
            except (ValueError, KeyError):
                continue

    return budgets

def save_all_budgets(filename, budgets):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(BUDGET_HEADERS)
        for b in sorted(budgets, key=lambda x: (x["Month"], x["Category"])):
            writer.writerow([b["Month"], b["Category"], f"{b['Budget']:.2f}"])

def prompt_month():
    while True:
        month_str = input("Enter Month (YYYY-MM): ").strip()
        try:
            datetime.strptime(month_str, "%Y-%m")
            return month_str
        except ValueError:
            print("Please enter a valid format (YYYY-MM).")

def set_budget(filename):
    ensure_budget_file_exists(filename)
    month = prompt_month()
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

    budgets = load_all_budgets(filename)

    # Check if budget already exists for this month + category, update or insert
    updated = False
    for b in budgets:
        if b["Month"] == month and b["Category"] == category:
            b["Budget"] = budget
            updated = True
            break

    if not updated:
        budgets.append({"Month": month, "Category": category, "Budget": budget})

    save_all_budgets(filename, budgets)
    print(f"Budget for {category} ({month}) saved successfully!")

def view_budgets(filename):
    budgets = load_all_budgets(filename)

    print()
    print("===== CURRENT BUDGETS =====")
    if not budgets:
        print("No budgets set yet.")
        return

    print(f"{'Month':<10} | {'Category':<18} | {'Budget':>10}")
    print("-" * 45)

    for b in sorted(budgets, key=lambda x: (x["Month"], x["Category"])):
        print(f"{b['Month']:<10} | {b['Category']:<18} | ${b['Budget']:>9.2f}")

def show_budget_status(transaction_file, budget_file):
    month = prompt_month()

    # Expenses for that month
    spent_by_category = analyze_categories_by_month(transaction_file, month)

    # Budgets for that month
    all_budgets = load_all_budgets(budget_file)
    monthly_budgets = {
        b["Category"]: b["Budget"]
        for b in all_budgets
        if b["Month"] == month
    }

    all_categories = sorted(set(monthly_budgets.keys()) | set(spent_by_category.keys()))

    print()
    print(f"===== BUDGET STATUS FOR {month} =====")

    if not all_categories:
        print(f"No budgets or expenses found for {month}.")
        return

    print(f"{'Category':<16} | {'Budget':>10} | {'Spent':>10} | {'Remaining':>10} | {'Status'}")
    print("-" * 65)

    for category in all_categories:
        budget = monthly_budgets.get(category, 0.0)
        spent = spent_by_category.get(category, 0.0)
        remaining = budget - spent

        if budget == 0.0:
            status = "NO BUDGET"
        elif remaining >= 0:
            status = "Under Budget"
        else:
            status = "OVER BUDGET"

        print(
            f"{category:<16} | "
            f"${budget:>9.2f} | "
            f"${spent:>9.2f} | "
            f"${remaining:>9.2f} | "
            f"{status}"
        )

def budget_management(transaction_file, budget_file):
    while True:
        print()
        print("===== BUDGET MANAGEMENT =====")
        print("1. Set Monthly Budget")
        print("2. View All Budgets")
        print("3. Monthly Budget Status")
        print("4. Back to Main Menu")

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