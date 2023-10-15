# Objective: Create a Python program that tracks a user's expenses and generates reports on their spending habits.
# Requirements:
# User should be able to input different expenses with categories (e.g. food, transportation, entertainment, etc.)
# User should be able to view their expenses and the total amount spent in each category
# User should be able to view their overall spending and the total amount saved
# The program should provide a monthly spending report and an annual report
# The program should be able to suggest a budget for each category based on the user's expenses


class expense_Tracker():
    def __init__(self):
        self.expense = {}
        self.budget = {
            'Clothes': 6000,
            'Food': 10000,
            'Transport': 5000,
            'Medical':3000,
            'Insuarance':2000
        }
    def add_expense(self,mode,amount):
        if mode in self.expense:
            self.expense[mode] += amount
        else:
            self.expenses[mode] = amount
    def view_expense(self):
        print('Expenses are:')
        for mode,amount in self.expense.item():
            print(f"{mode.upper()}: ${amount}")
    def view_spending(self):
        total_spending = sum(self.expense.values())
        print(f"Total: ${total_spending}")
    def view_savings(self,income):
        total_saving = income - sum(self.expense.value())
        print(f"Savings: ${total_saving}")
    def generate_report(self):
        self.view_expense()
        self.view_savings()
        self.view_spending
    def generate_annual_report(self):
        print('Anual Report:')
        for month in range(1,12):
            print(f"month {month}")
            self.generate_annual_report()
    def suggest_budget(self):
        print('Suggestions')
        for mode,budget in self.budget.items():
            if mode in self.expense;
                rem_budget = budget - self.expense
                if rem_budget > 0:
                    print(f"${rem_budget}")
                else:
                    print(f" Budget exceeded")

tracker = expense_Tracker()

tracker.add_expense('accessories',2300)
tracker.generate_annual_report()
tracker.generate_report()
tracker.suggest_budget()
        