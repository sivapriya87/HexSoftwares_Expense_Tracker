import datetime

expenses = []
monthly_budget = None

def add_expense():
    amount = float(input("Enter the amount: "))
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    expenses.append({"amount": amount, "date": date, "category": category})
    print("Expense added successfully.")

def view_expenses():
    print("Your expenses:")
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Date: {expense['date']}, Category: {expense['category']}")

def view_summary():
    total_expenses = sum(expense["amount"] for expense in expenses)
    print("Total Expenses:", total_expenses)

    # Expenses by category
    expenses_by_category = {}
    for expense in expenses:
        category = expense["category"]
        if category not in expenses_by_category:
            expenses_by_category[category] = 0
        expenses_by_category[category] += expense["amount"]
    print("Expenses by Category:")
    for category, amount in expenses_by_category.items():
        print(f"{category}: {amount}")

def view_budget_summary():
    global monthly_budget
    if not monthly_budget:
        monthly_budget = float(input("Enter your monthly budget: "))

    today = datetime.date.today()
    last_day_of_month = today + datetime.timedelta(days=31 - today.day)
    days_left = (last_day_of_month - today).days + 1

    total_expenses = sum(expense["amount"] for expense in expenses)
    budget_used = total_expenses
    balance = monthly_budget - budget_used
    daily_budget = balance / days_left

    print("Budget Summary:")
    print("Monthly Budget:", monthly_budget)
    print("Budget Used:", budget_used)
    print("Balance:", balance)
    print("Days Left:", days_left)
    print("Daily Budget:", daily_budget)

    # Save the budget for future use
    with open("budget.txt", "w") as f:
        f.write(str(monthly_budget))

# Load the budget from a file if it exists
try:
    with open("budget.txt", "r") as f:
        monthly_budget = float(f.read())
except FileNotFoundError:
    pass

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. View Budget Summary")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        view_summary()
    elif choice == 4:
        view_budget_summary()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")