def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Exit")

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g. food, travel): ")
    note = input("Optional note: ")
    expenses.append({"amount": amount, "category": category, "note": note})

def view_expenses(expenses):
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. ${exp['amount']} - {exp['category']} ({exp['note']})")

def view_total(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spending: ${total}")

import json

def save_expenses(expenses, filename="expenses.txt"):
    with open(filename, "w") as f:
        json.dump(expenses, f)

def load_expenses(filename="expenses.txt"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def main():
    expenses = load_expenses()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


