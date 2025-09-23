class Python:
    def __init__(self, n):
        self.n = n

    def even_odd_checker(self):
        if self.n % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")

    def pos_neg_checker(self):
        if self.n > 0:
            print("Positive Number")
        elif self.n < 0:
            print("Negative Number")
        else:
            print("Number is Zero")

    def table_of_digit(self):
        for i in range(1, 11):
            print(f"{self.n} x {i} = {self.n * i}", end=", ")  

    def factorial(self):
        fact = 1
        for i in range(1, self.n+1):
            fact = fact * i
        print(f"Factorial of {self.n} : {fact}")

    def square_of_digit(self):
        print(f"Square of {self.n} : {self.n**2}")

p = Python(5)
p.even_odd_checker()
p.pos_neg_checker()
p.table_of_digit()
p.factorial()
p.square_of_digit()



    

    

    