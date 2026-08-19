import csv

from financial_analysis import analyze_categories


def analyze_budgets(transaction_file, budget_file):
    category_totals = analyze_categories(transaction_file)
    budgets = {}

    with open(budget_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            budgets[row["Category"]] = float(row["Budget"])

    return category_totals, budgets


def show_budget_status(transaction_file, budget_file):
    category_totals, budgets = analyze_budgets(
        transaction_file,
        budget_file
    )

    print()
    print("===== BUDGET STATUS =====")

    for category, budget in budgets.items():
        spent = category_totals.get(category, 0)
        remaining = budget - spent

        if remaining >= 0:
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
    category = input("Category: ").strip()

    while True:
        try:
            budget = float(input("Budget Amount: $"))

            if budget <= 0:
                print("Budget must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    budgets = {}

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            budgets[row["Category"]] = float(row["Budget"])

    budgets[category] = budget

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["Category", "Budget"])

        for category_name, amount in budgets.items():
            writer.writerow([category_name, amount])

    print(f"Budget for {category} updated successfully!")


def view_budgets(filename):
    print()
    print("===== CURRENT BUDGETS =====")

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(
                f"{row['Category']:<20} "
                f"${float(row['Budget']):.2f}"
            )


def budget_management(transaction_file, budget_file):
    while True:
        print()
        print("===== BUDGET MANAGEMENT =====")
        print("1. Set Budget")
        print("2. View Budgets")
        print("3. Budget Status")
        print("4. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            set_budget(budget_file)

        elif choice == "2":
            view_budgets(budget_file)

        elif choice == "3":
            show_budget_status(
                transaction_file,
                budget_file
            )

        elif choice == "4":
            break

        else:
            print("Invalid option. Please choose 1-4.")