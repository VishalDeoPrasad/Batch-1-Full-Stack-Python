from shop import total_bill
from shop.utils import apply_discount

prices = [100, 130, 140, 160]
total = total_bill(prices)

pay = apply_discount(total, 10)
print(pay)