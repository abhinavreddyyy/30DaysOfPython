class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    def total_income(self):
        return sum(self.incomes)
    def total_expense(self):
        return sum(self.expenses)
    def account_balance(self):
        return self.total_income() - self.total_expense()

details = PersonAccount('John', 'naidu', [1000, 2000, 3000], [500, 1000, 1500])
print('Total Income:', details.total_income())
print('Total Expense:', details.total_expense())
print('Account Balance:', details.account_balance())