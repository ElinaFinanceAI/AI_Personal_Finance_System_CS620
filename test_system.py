from expense_tracker import ExpenseTracker
from budget_manager import BudgetManager
from alerts import Alerts

tracker = ExpenseTracker()

tracker.add_expense(200)
tracker.add_expense(150)

total = tracker.show_total()

budget = BudgetManager(300)
alert = Alerts()

print("Total Spending:", total)
print("Budget Status:", budget.check_budget(total))
print("Alert Message:", alert.send_alert(total, 300))