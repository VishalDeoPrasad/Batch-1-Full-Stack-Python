class BankAccount:
    def __init__(self):
        self.account_number = "876542314527"
        self.__ATM_pin = 2345

    def view_atm_pin(self):
        return self.__ATM_pin
    
    def change_atm_pin(self, new_pin):
        self.__ATM_pin = new_pin

a1 = BankAccount()
print(a1.account_number)
print(a1.view_atm_pin())
a1.change_atm_pin("0000")
print(a1.view_atm_pin())