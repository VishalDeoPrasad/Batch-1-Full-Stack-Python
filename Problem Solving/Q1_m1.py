num = 1234

num = str(num)

res = 0
for i in range(len(num)):
    res = res + int(num[i])

print(res)
