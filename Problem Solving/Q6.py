nums = [2, 5, 1, 2, 3, 5]

unique_num = set()
for n in nums:
    if n in unique_num:
        print(n)
        break
    else:
        unique_num.add(n)



