class Bank:
    def __init__(self):
        self.bank_name = "SBI"
        self.bank_address = "Main Road"

    def print_bank_name(self):
        print(self.bank_name)

    def print_bank_address(self):
        print(self.bank_address)

    def review(self):
        print("5 Star")

class SavingAccount(Bank):
    def __init__(self):
        super().__init__()
        self.account_number = "9098765654233"
        self.balance = 45000

    def print_account_number(self):
        print(self.account_number)

    def print_balance(self):
        print(self.balance)

    def review(self):
        print("4 Star")

acc1 = SavingAccount()

acc1.print_bank_name()
acc1.print_bank_address()
acc1.print_account_number()
acc1.print_balance()
acc1.review()


        

    
