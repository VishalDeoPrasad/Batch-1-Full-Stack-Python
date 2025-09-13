class BankAccount:
    bank_name = "SBI Bank"
    
    def __init__(self, acc, bal):
        self.account_number = acc
        self.balance = bal

    def show_info(self):
        print("Bank : ", BankAccount.bank_name)
        print("Account Number : ", self.account_number)
        print("Balance : ", self.balance)


account1 = BankAccount("987678987698", 5000)
account2 = BankAccount("876567898763", 10000)

account2.show_info()
