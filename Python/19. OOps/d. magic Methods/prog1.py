class Bank:
    def __init__(self, name, bank_account, branch):
        self.name = name
        self.bank_account = bank_account
        self.branch = branch

    def __str__(self):
        return f"{self.name} {self.bank_account}"
    
acc1 = Bank("Vishal","101", "HYD")
acc2 = Bank("Amit","102", "HYD")
acc3 = Bank("Charan","103", "HYD")

print(acc3)