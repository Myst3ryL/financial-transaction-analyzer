import csv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

TRANSACTION_FILE = DATA_DIR / "transactions.csv"
BUDGET_FILE = DATA_DIR / "budgets.csv"
SETTINGS_FILE = DATA_DIR / "settings.csv"

TRANSACTION_HEADERS = ["Date", "Category", "Description", "Amount", "Type"]
BUDGET_HEADERS = ["Month", "Category", "Budget"]
SETTINGS_HEADERS = ["Setting", "Value"]


def init_db():
    """Ensure data directory and required CSV files with headers exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    defaults = [
        (TRANSACTION_FILE, TRANSACTION_HEADERS),
        (BUDGET_FILE, BUDGET_HEADERS),
    ]

    for file_path, headers in defaults:
        if not file_path.exists():
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f, lineterminator="\n")
                writer.writerow(headers)

    # Initialize settings.csv directly to prevent recursion
    if not SETTINGS_FILE.exists():
        with open(SETTINGS_FILE, "w", newline="") as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(SETTINGS_HEADERS)
            writer.writerow(["Starting Balance", "0.00"])


# ===================== TRANSACTIONS =====================

def get_transactions():
    init_db()
    transactions = []
    with open(TRANSACTION_FILE, "r") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):
            try:
                transactions.append({
                    "id": idx,
                    "Date": row.get("Date", "").strip(),
                    "Category": row.get("Category", "Uncategorized").strip().title(),
                    "Description": row.get("Description", "").strip(),
                    "Amount": float(row.get("Amount", 0.0)),
                    "Type": row.get("Type", "").strip().title()
                })
            except (ValueError, KeyError):
                continue
    return transactions


def add_transaction_record(date, category, description, amount, trans_type):
    init_db()
    with open(TRANSACTION_FILE, "a", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow([
            date.strip(),
            category.strip().title(),
            description.strip(),
            f"{float(amount):.2f}",
            trans_type.strip().title()
        ])


def overwrite_transactions(transactions_list):
    """Saves updated transactions back to CSV after edit or delete."""
    init_db()
    with open(TRANSACTION_FILE, "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(TRANSACTION_HEADERS)
        for t in transactions_list:
            writer.writerow([
                t["Date"],
                t["Category"],
                t["Description"],
                f"{t['Amount']:.2f}",
                t["Type"]
            ])


# ===================== BUDGETS =====================

def get_budgets():
    init_db()
    budgets = []
    with open(BUDGET_FILE, "r") as f:
        reader = csv.DictReader(f)
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


def set_budget_record(month, category, budget_amount):
    budgets = get_budgets()
    month = month.strip()
    category = category.strip().title()
    budget_amount = float(budget_amount)

    updated = False
    for b in budgets:
        if b["Month"] == month and b["Category"] == category:
            b["Budget"] = budget_amount
            updated = True
            break

    if not updated:
        budgets.append({"Month": month, "Category": category, "Budget": budget_amount})

    with open(BUDGET_FILE, "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(BUDGET_HEADERS)
        for b in sorted(budgets, key=lambda x: (x["Month"], x["Category"])):
            writer.writerow([b["Month"], b["Category"], f"{b['Budget']:.2f}"])


# ===================== SETTINGS =====================

def get_settings():
    init_db()
    settings = {}
    with open(SETTINGS_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                settings[row["Setting"].strip()] = float(row["Value"])
            except (ValueError, KeyError):
                continue
    return settings


def update_setting(setting_name, value):
    init_db()
    settings = get_settings()
    settings[setting_name.strip()] = float(value)

    with open(SETTINGS_FILE, "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(SETTINGS_HEADERS)
        for k, v in settings.items():
            writer.writerow([k, f"{v:.2f}"])