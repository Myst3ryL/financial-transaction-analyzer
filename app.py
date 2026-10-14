from flask import Flask, render_template, request, redirect, url_for
import database
from datetime import datetime

app = Flask(__name__)


def calculate_summary():
    transactions = database.get_transactions()
    settings = database.get_settings()
    starting_balance = settings.get("Starting Balance", 0.0)

    total_income = sum(t["Amount"] for t in transactions if t["Type"] == "Income")
    total_expenses = sum(t["Amount"] for t in transactions if t["Type"] == "Expense")
    net_income = total_income - total_expenses
    current_balance = starting_balance + net_income

    return {
        "starting_balance": starting_balance,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_income": net_income,
        "current_balance": current_balance,
    }


@app.route("/")
def dashboard():
    summary = calculate_summary()
    transactions = database.get_transactions()
    # Show the 5 most recent transactions
    recent_transactions = sorted(
        transactions, key=lambda x: x["Date"], reverse=True
    )[:5]
    return render_template(
        "dashboard.html", summary=summary, transactions=recent_transactions
    )


@app.route("/transactions", methods=["GET", "POST"])
def transactions_page():
    if request.method == "POST":
        date = request.form.get("date", datetime.today().strftime("%Y-%m-%d"))
        category = request.form.get("category", "General")
        description = request.form.get("description", "")
        amount = float(request.form.get("amount", 0.0))
        trans_type = request.form.get("type", "Expense")

        database.add_transaction_record(
            date, category, description, amount, trans_type
        )
        return redirect(url_for("transactions_page"))

    all_transactions = sorted(
        database.get_transactions(), key=lambda x: x["Date"], reverse=True
    )
    return render_template("transactions.html", transactions=all_transactions)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)