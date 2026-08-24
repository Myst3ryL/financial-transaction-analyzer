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

## Technologies

- Python
- CSV data storage
- File handling
- Data analysis
- Error handling
- Git & GitHub

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

Example
========================================
      FINANCIAL TRANSACTION ANALYZER
========================================
1. Add Transaction
2. View Transactions
3. Financial Summary
4. Expense by Category
5. Monthly Analysis
6. Budget Management
7. Financial Insights
8. Exit


Choose an option: 7


===== FINANCIAL INSIGHTS =====
Savings Rate:          -18.30%
Largest Expense:       $700.00 (Laptop)
Largest Category:      $700.00 (Tech)
Average Expense:       $85.03
Income Transactions:   2
Expense Transactions:  16
Financial Analysis

The application can analyze financial transactions to provide information such as:

Total income
Total expenses
Net income
Current balance
Spending by category
Monthly income and expenses
Savings rate
Average expense
Largest individual expense
Largest spending category
Number of income transactions
Number of expense transactions
Budget Management

Users can create and manage spending limits for different categories.

For example:

===== BUDGET STATUS =====


Food
Budget:     $400.00
Spent:      $153.50
Remaining:  $246.50
Status:     Under Budget


Tech
Budget:     $500.00
Spent:      $700.00
Remaining:  $-200.00
Status:     OVER BUDGET

This allows users to compare actual spending with planned spending limits.

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

Data visualization using Python and Matplotlib
Spending trend charts
Income vs. expense charts
Improved monthly reporting
Exportable financial reports
More advanced budget alerts
Search and filtering of transactions
Additional financial performance metrics