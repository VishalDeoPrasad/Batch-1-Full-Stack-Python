n = 1234

res = 0
while n > 0:
    l = n % 10
    res = res + l
    n = n // 10

print(res)

