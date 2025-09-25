n = 12345

rev_n = 0
while n > 0:
    l = n % 10
    rev_n = rev_n*10 + l
    n = n // 10

print(rev_n)


