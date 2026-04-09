class BudgetManager:
    def __init__(self, limit):
        self.limit = limit

    def check_budget(self, total):
        if total > self.limit:
            return "Over budget"
        else:
            return "Within budget"