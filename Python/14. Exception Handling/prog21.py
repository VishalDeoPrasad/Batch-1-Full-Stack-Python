class NegativeDiscount(Exception):
    pass

discount = -10
if discount < 0:
    raise NegativeDiscount("Negative Discount Not Allowd!")
else:
    print(discount)