"""
Personal Finance Ledger
------------------------
A file-backed CLI tool to log and analyse personal expenses.
Transactions persist in a local JSON file between sessions.

No external libraries — pure Python only.
"""

import json
import os
from datetime import datetime

LEDGER_FILE = "ledger.json"

CATEGORIES = [
    "Food & Dining",
    "Transport",
    "Shopping",
    "Entertainment",
    "Utilities",
    "Health",
    "Education",
    "Rent",
    "Other",
]


# ── Storage helpers ───────────────────────────────────────────────────────────

def load_ledger():
    """Load transactions from the JSON file. Returns an empty list if none."""
    if not os.path.exists(LEDGER_FILE):
        return []
    with open(LEDGER_FILE, "r") as f:
        return json.load(f)


def save_ledger(transactions):
    """Persist the transactions list to disk."""
    with open(LEDGER_FILE, "w") as f:
        json.dump(transactions, f, indent=2)


# ── Core operations ───────────────────────────────────────────────────────────

def add_transaction(transactions):
    print("\n--- Add Transaction ---")
    description = input("Description: ").strip()

    # Amount
    while True:
        try:
            amount = float(input("Amount (₹): ").strip())
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    # Category
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    while True:
        try:
            cat_choice = int(input("Choose category (1-9): ").strip())
            if 1 <= cat_choice <= len(CATEGORIES):
                category = CATEGORIES[cat_choice - 1]
                break
            else:
                print(f"Enter a number between 1 and {len(CATEGORIES)}.")
        except ValueError:
            print("Enter a valid number.")

    # Date — default to today
    date_input = input(f"Date (DD-MM-YYYY) [press Enter for today]: ").strip()
    if not date_input:
        date = datetime.today().strftime("%d-%m-%Y")
    else:
        try:
            datetime.strptime(date_input, "%d-%m-%Y")
            date = date_input
        except ValueError:
            print("Invalid date format. Using today's date.")
            date = datetime.today().strftime("%d-%m-%Y")

    entry = {
        "id": len(transactions) + 1,
        "description": description,
        "amount": round(amount, 2),
        "category": category,
        "date": date,
    }
    transactions.append(entry)
    save_ledger(transactions)
    print(f"\nAdded: {description} | ₹{amount:.2f} | {category} | {date}\n")


def view_all(transactions):
    if not transactions:
        print("\nNo transactions yet.\n")
        return

    print(f"\n{'ID':<5}{'Date':<14}{'Description':<25}{'Category':<18}{'Amount (₹)':>10}")
    print("-" * 72)
    for t in transactions:
        print(f"{t['id']:<5}{t['date']:<14}{t['description'][:24]:<25}"
              f"{t['category']:<18}{t['amount']:>10.2f}")
    total = sum(t["amount"] for t in transactions)
    print("-" * 72)
    print(f"{'Total spend':<62}₹{total:>9.2f}\n")


def monthly_summary(transactions):
    if not transactions:
        print("\nNo transactions to summarise.\n")
        return

    # Collect all months present in the data
    months_available = sorted(
        set(t["date"][3:] for t in transactions), reverse=True
    )

    print("\nMonths available:")
    for i, m in enumerate(months_available, 1):
        print(f"  {i}. {m}")

    try:
        choice = int(input("Select month (number): ").strip())
        selected_month = months_available[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.\n")
        return

    monthly = [t for t in transactions if t["date"][3:] == selected_month]
    if not monthly:
        print(f"No transactions for {selected_month}.\n")
        return

    total = sum(t["amount"] for t in monthly)

    # Aggregate by category
    cat_data = {}
    for t in monthly:
        cat = t["category"]
        if cat not in cat_data:
            cat_data[cat] = {"total": 0.0, "biggest": ("", 0.0)}
        cat_data[cat]["total"] += t["amount"]
        if t["amount"] > cat_data[cat]["biggest"][1]:
            cat_data[cat]["biggest"] = (t["description"], t["amount"])

    # Sort by spend descending
    sorted_cats = sorted(cat_data.items(), key=lambda x: x[1]["total"], reverse=True)

    print(f"\n=== Monthly Summary: {selected_month} ===")
    print(f"{'Category':<20}{'Spent (₹)':>10}{'% of total':>12}  Biggest expense")
    print("-" * 72)
    for cat, data in sorted_cats:
        pct = (data["total"] / total) * 100
        desc, amt = data["biggest"]
        print(f"{cat:<20}{data['total']:>10.2f}{pct:>11.1f}%  {desc} (₹{amt:.2f})")
    print("-" * 72)
    print(f"{'Total':<20}{total:>10.2f}\n")


def delete_transaction(transactions):
    if not transactions:
        print("\nNo transactions to delete.\n")
        return

    view_all(transactions)
    try:
        del_id = int(input("Enter ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.\n")
        return

    match = [t for t in transactions if t["id"] == del_id]
    if not match:
        print(f"No transaction with ID {del_id}.\n")
        return

    entry = match[0]
    confirm = input(
        f"Delete '{entry['description']}' (₹{entry['amount']:.2f}) on {entry['date']}? (y/n): "
    ).strip().lower()

    if confirm == "y":
        transactions.remove(entry)
        save_ledger(transactions)
        print("Deleted.\n")
    else:
        print("Cancelled.\n")


def load_sample_data(transactions):
    """Pre-load a handful of sample entries to explore the tool without real data."""
    if transactions:
        print("Ledger already has entries — sample data not loaded.\n")
        return

    samples = [
        ("Swiggy dinner", 320.0, "Food & Dining", "01-07-2026"),
        ("Ola cab to college", 85.0, "Transport", "02-07-2026"),
        ("Amazon headphones", 1499.0, "Shopping", "02-07-2026"),
        ("Netflix subscription", 199.0, "Entertainment", "03-07-2026"),
        ("Electricity bill", 750.0, "Utilities", "04-07-2026"),
        ("Pharmacy", 230.0, "Health", "04-07-2026"),
        ("Domino's pizza", 450.0, "Food & Dining", "05-07-2026"),
        ("Rapido bike", 45.0, "Transport", "06-07-2026"),
        ("Udemy course", 499.0, "Education", "07-07-2026"),
        ("Zepto groceries", 860.0, "Food & Dining", "07-07-2026"),
    ]

    for i, (desc, amt, cat, date) in enumerate(samples, 1):
        transactions.append({
            "id": i, "description": desc,
            "amount": amt, "category": cat, "date": date
        })

    save_ledger(transactions)
    print(f"Loaded {len(samples)} sample transactions for July 2026.\n")


def print_menu():
    print("=" * 45)
    print("     PERSONAL FINANCE LEDGER")
    print("=" * 45)
    print("1. Add a transaction")
    print("2. View all transactions")
    print("3. Monthly summary by category")
    print("4. Delete a transaction")
    print("5. Load sample data (first run)")
    print("6. Exit")
    print("=" * 45)


def main():
    transactions = load_ledger()
    print(f"\nLedger loaded — {len(transactions)} transaction(s) on file.\n")

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_all(transactions)
        elif choice == "3":
            monthly_summary(transactions)
        elif choice == "4":
            delete_transaction(transactions)
        elif choice == "5":
            load_sample_data(transactions)
        elif choice == "6":
            print("Ledger saved. Goodbye!\n")
            break
        else:
            print("Invalid choice. Select 1-6.\n")


if __name__ == "__main__":
    main()
