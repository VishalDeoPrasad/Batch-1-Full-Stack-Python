class Bank:
    def __init__(self, bank_name, bank_add):
        self.bank_name = bank_name
        self.bank_address = bank_add

    def print_bank_name(self):
        print(self.bank_name)

    def print_bank_address(self):
        print(self.bank_address)

class SavingAccount(Bank):
    def __init__(self, bank_name, bank_add, acc_no, bal):
        super().__init__(bank_name, bank_add)
        self.account_number = acc_no
        self.balance = bal

    def print_account_number(self):
        print(self.account_number)

    def print_balance(self):
        print(self.balance)

acc1 = SavingAccount("SBI", "HYD", "123454565656", 4500)

acc1.print_bank_name()
acc1.print_bank_address()
acc1.print_account_number()
acc1.print_balance()


        

    
