import os

file_name = "expenses.txt"

def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open(file_name, "a") as f:
        f.write(f"{name},{amount}\n")

    print("Expense added successfully.\n")


def view_expenses():
    if not os.path.exists(file_name):
        print("No expenses recorded yet.\n")
        return

    total = 0
    print("\nYour Expenses:\n")

    with open(file_name, "r") as f:
        for line in f:
            name, amount = line.strip().split(",")
            amount = float(amount)
            total += amount
            print(f"{name} : ₹{amount}")

    print(f"\nTotal Spent: ₹{total}\n")


while True:
    print("==== Budget Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice\n")