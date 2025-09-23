class BankAccount:
    def __init__(self, acc_no, bal):
        self.account_number = acc_no
        self.balance = bal

    def deposit(self, amount):
        self.balance = self.balance + amount

class SavingAccount(BankAccount):
    def __init__(self, acc_no, bal, rate):
        super().__init__(acc_no, bal)
        self.interest_rate = rate
    
    def add_interest(self):
        I = self.balance * self.interest_rate / 100
        self.balance = self.balance + I

    def show_balance(self):
        print("Account Balance:", self.balance)

acc1 = SavingAccount(12345678, 1000, 3)
acc1.deposit(5000)
acc1.show_balance()
acc1.add_interest()
acc1.show_balance()

