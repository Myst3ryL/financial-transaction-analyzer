from transaction_manager import add_transaction, view_transactions

from financial_analysis import (
    show_summary,
    show_category_analysis,
    show_monthly_analysis,
    show_insights
)

from budget_manager import budget_management

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
        print("5. Monthly Analysis")
        print("6. Budget Management")
        print("7. Financial Insights")
        print("8. Exit")

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
            show_monthly_analysis(filename)

        elif choice == "6":
            budget_management(
                filename,
                "data/budgets.csv"
            )

        elif choice == "7":
            show_insights(filename)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-8.")


main()