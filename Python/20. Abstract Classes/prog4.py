from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def processing(self):
        pass

class UPIPayment(Payment):
    def processing(self):
        print("Payment Via: UPI")

class CreditCard(Payment):
    def processing(self):
        print("Payment Via: Credit Card")

class Cash(Payment):
    def processing(self):
        print("Payment Via: Cash")

obj1 = UPIPayment()
obj2 = CreditCard()
obj3 = Cash()
obj1.processing()
obj2.processing()
obj3.processing()