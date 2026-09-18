from pathlib import Path

from transaction_manager import add_transaction, view_transactions
from visualization import (
    plot_expenses_by_category,
    plot_income_vs_expenses,
    plot_monthly_trends,
)
from financial_analysis import (
    show_summary,
    show_category_analysis,
    show_monthly_analysis,
    show_insights,
)
from budget_manager import budget_management


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

TRANSACTION_FILE = DATA_DIR / "transactions.csv"
BUDGET_FILE = DATA_DIR / "budgets.csv"
SETTINGS_FILE = DATA_DIR / "settings.csv"


def init_environment():
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def main():
    init_environment()

    while True:
        print()
        print("========================================")
        print("      FINANCIAL TRANSACTION ANALYZER")
        print("========================================")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Financial Summary")
        print("4. Expense by Category")
        print("5. Monthly Analysis")
        print("6. Budget Management")
        print("7. Financial Insights")
        print("8. Expense Visualization")
        print("9. Income vs Expenses Visualization")
        print("10. Monthly Trends Visualization")
        print("11. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_transaction(TRANSACTION_FILE)

        elif choice == "2":
            view_transactions(TRANSACTION_FILE)

        elif choice == "3":
            show_summary(TRANSACTION_FILE, SETTINGS_FILE)

        elif choice == "4":
            show_category_analysis(TRANSACTION_FILE)

        elif choice == "5":
            show_monthly_analysis(TRANSACTION_FILE)

        elif choice == "6":
            budget_management(TRANSACTION_FILE, BUDGET_FILE)

        elif choice == "7":
            show_insights(TRANSACTION_FILE)

        elif choice == "8":
            plot_expenses_by_category(TRANSACTION_FILE)

        elif choice == "9":
            plot_income_vs_expenses(TRANSACTION_FILE)

        elif choice == "10":
            plot_monthly_trends(TRANSACTION_FILE)

        elif choice == "11":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-11.")


if __name__ == "__main__":
    main()