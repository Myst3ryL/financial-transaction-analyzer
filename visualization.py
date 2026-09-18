import csv
import os
import matplotlib.pyplot as plt
from financial_analysis import analyze_categories


def plot_expenses_by_category(filename):
    category_totals = analyze_categories(filename)

    if not category_totals:
        print("\nNo expense data available to plot.")
        return

    # Sort categories by descending total for cleaner visualization
    sorted_items = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
    categories = [item[0] for item in sorted_items]
    amounts = [item[1] for item in sorted_items]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, amounts, color="#4A90E2")

    # Add numeric labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.annotate(
            f"${height:.2f}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.title("Expenses by Category", fontsize=14, pad=15)
    plt.xlabel("Category", fontsize=11)
    plt.ylabel("Amount ($)", fontsize=11)
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


def plot_income_vs_expenses(filename):
    total_income = 0.0
    total_expenses = 0.0

    if not os.path.exists(filename):
        print("\nNo transaction file found.")
        return

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                amount = float(row["Amount"])
            except (ValueError, KeyError):
                continue

            trans_type = row.get("Type", "").strip().title()
            if trans_type == "Income":
                total_income += amount
            elif trans_type == "Expense":
                total_expenses += amount

    if total_income == 0 and total_expenses == 0:
        print("\nNo income or expense data found to plot.")
        return

    labels = ["Income", "Expenses"]
    amounts = [total_income, total_expenses]
    colors = ["#2ECC71", "#E74C3C"]

    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, amounts, color=colors, width=0.5)

    for bar in bars:
        height = bar.get_height()
        plt.annotate(
            f"${height:.2f}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )

    plt.title("Income vs. Expenses", fontsize=14, pad=15)
    plt.ylabel("Amount ($)", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


def plot_monthly_trends(filename):
    monthly_totals = {}

    if not os.path.exists(filename):
        print("\nNo transaction file found.")
        return

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            trans_type = row.get("Type", "").strip().title()
            if trans_type == "Expense":
                date_val = row.get("Date", "").strip()
                if len(date_val) >= 7:
                    month = date_val[:7]
                    try:
                        amount = float(row["Amount"])
                    except (ValueError, KeyError):
                        continue

                    monthly_totals[month] = monthly_totals.get(month, 0.0) + amount

    if not monthly_totals:
        print("\nNo monthly expense data found to plot.")
        return

    months = sorted(monthly_totals.keys())
    amounts = [monthly_totals[m] for m in months]

    plt.figure(figsize=(10, 6))
    plt.plot(months, amounts, marker="o", color="#E67E22", linewidth=2, markersize=6)

    for x, y in zip(months, amounts):
        plt.annotate(
            f"${y:.2f}",
            (x, y),
            textcoords="offset points",
            xytext=(0, 8),
            ha="center",
            fontsize=9
        )

    plt.title("Monthly Expense Trends", fontsize=14, pad=15)
    plt.xlabel("Month", fontsize=11)
    plt.ylabel("Total Expenses ($)", fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()