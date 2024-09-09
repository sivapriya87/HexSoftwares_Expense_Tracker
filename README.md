Overview
This Python program helps users manage their personal expenses by allowing them to:

Add and categorize expenses.
View all their recorded expenses.
View a summary of total expenses and expenses by category.
Set and track a monthly budget, and view how much of the budget has been used, as well as the remaining balance.
Features
Add Expense: Users can add new expenses with the following details:

Amount
Date (in YYYY-MM-DD format)
Category (e.g., groceries, transport, etc.)
View Expenses: Displays a list of all recorded expenses with the amount, date, and category.

View Summary: Provides a summary that shows:

The total amount of expenses.
A breakdown of expenses by category.
View Budget Summary: Users can input a monthly budget, and the program will show:

The total budget.
The amount spent so far.
The remaining balance.
The number of days left in the current month.
The daily budget for the remaining days.
The budget is stored in a budget.txt file for future use and loaded when the program starts.
Exit: Exits the program.

How to Run the Program
Ensure you have Python 3 installed on your system.
Copy the provided code into a Python file (e.g., expense_tracker.py).
Run the script by executing the command:
python expense_tracker.py
Follow the on-screen menu to interact with the program.
Menu Options
Add Expense: Prompts you to input the expense amount, date, and category.
View Expenses: Displays all recorded expenses.
View Summary: Shows the total expenses and a breakdown of expenses by category.
View Budget Summary: Displays your monthly budget status, balance, and a suggested daily budget to stay within the budget for the rest of the month.
Exit: Terminates the program.
Files
budget.txt: This file stores the monthly budget value so that it can be persisted across sessions. If the file is not found, the program will ask the user to input the monthly budget.
Dependencies
Python 3.x (no external libraries required)
Example Usage
bash
1. Add Expense
2. View Expenses
3. View Summary
4. View Budget Summary
5. Exit
Enter your choice: 1
Enter the amount: 50.00
Enter the date (YYYY-MM-DD): 2024-09-09
Enter the category: Groceries
Expense added successfully.

1. Add Expense
2. View Expenses
3. View Summary
4. View Budget Summary
5. Exit
Enter your choice: 4
Enter your monthly budget: 2000
Budget Summary:
Monthly Budget: 2000.0
Budget Used: 50.0
Balance: 1950.0
Days Left: 22
Daily Budget: 88.63636363636364
Notes
The program automatically saves the user's budget to a file (budget.txt) and reloads it upon the next program execution.
The number of days left in the month is calculated dynamically based on the current date.
Future Improvements
Adding the ability to edit or delete expenses.
Supporting multiple users or profiles.
Graphical or tabular views for better insights on spending patterns.
