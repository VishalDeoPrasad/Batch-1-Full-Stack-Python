class BankAccount:
    def __init__(self):
        self.account_number = 987658902387
        self.account_type = "Saving"
        self.bank_balance = 500000

    def deposit(self):
        print("You have deposited some money!")

    def withdraw(self):
        print("You Withdraw some amount")

obj = BankAccount()
print(obj.account_number)
print(obj.account_type)
print(obj.bank_balance)