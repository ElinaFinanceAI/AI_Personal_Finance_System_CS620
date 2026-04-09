class ExpenseTracker:
    def __init__(self):
        self.total = 0

    def add_expense(self, amount):
        self.total = self.total + amount

    def show_total(self):
        return self.total