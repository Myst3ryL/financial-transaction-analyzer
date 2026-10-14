# Financial Transaction Analyzer

A Python-based financial analysis application designed to track income, expenses, budgets, and financial performance.

This project combines accounting concepts with programming and data analysis to provide tools for managing and analyzing personal financial transactions.

## Features

- Add and record income and expense transactions
- Validate transaction dates, amounts, and transaction types
- View stored financial transactions
- Calculate total income and total expenses
- Calculate net income and current balance
- Analyze expenses by category
- Calculate spending percentages by category
- Identify the largest spending category
- Perform monthly financial analysis
- Calculate financial insights such as savings rate and average expense
- Track income and expense transaction counts
- Create and manage spending budgets
- Compare actual spending against budget limits
- Identify categories that are over or under budget
- Store financial data using CSV files
- Expense visualization by category using bar charts
- Income vs. expenses comparison chart
- Monthly expense trend visualization using line charts

## Technologies

- Python
- CSV data storage
- File handling
- Data analysis
- Error handling
- Git & GitHub
- Matplotlib for data visualization

## Project Structure

```text
financial-transaction-analyzer/
│
├── main.py
├── transaction_manager.py
├── financial_analysis.py
├── budget_manager.py
├── README.md
│
└── data/
    ├── transactions.csv
    ├── budgets.csv
    └── settings.csv
File Descriptions
main.py
Runs the main application menu
Connects the different modules
transaction_manager.py
Adds financial transactions
Validates transaction information
Displays stored transactions
financial_analysis.py
Calculates total income and expenses
Calculates net income and current balance
Performs expense category analysis
Performs monthly financial analysis
Generates financial insights
budget_manager.py
Creates and updates budgets
Displays current budgets
Compares spending against budgets
Identifies over-budget categories
data/
Stores transaction, budget, and financial data using CSV files
How to Run
Requirements
Python 3.x
Git (optional, for cloning the repository)
Run the Application

Clone the repository:

git clone https://github.com/Myst3ryL/financial-transaction-analyzer.git

Navigate to the project directory:

cd financial-transaction-analyzer

Run the program:

python3 main.py

The application will display an interactive menu where users can add transactions, analyze financial data, and manage budgets.

========================================
      FINANCIAL TRANSACTION ANALYZER
========================================
1. Transaction Operations (Add/View/Search/Edit/Delete)
2. Financial Summary
3. Expense by Category
4. Monthly Analysis
5. Budget Management
6. Financial Insights
7. Expense Visualization
8. Income vs Expenses Visualization
9. Monthly Trends Visualization
10. Exit

Skills Demonstrated

This project demonstrates practical experience with:

Python programming
Modular program design
CSV file handling
Data validation
Financial calculations
Budget analysis
Data organization
Error handling
Git and GitHub
Financial data analysis
Project Purpose

This project was created to combine my coursework in accounting and computer science by applying programming and data analysis techniques to financial transaction management.

The project demonstrates how accounting data can be organized, analyzed, and transformed into useful financial insights through software.

Future Improvements

Potential future improvements include:

- Interactive dashboards
- More detailed monthly and yearly trend analysis
Spending trend charts
Income vs. expense charts
Improved monthly reporting
Exportable financial reports
More advanced budget alerts
Search and filtering of transactions
Additional financial performance metrics