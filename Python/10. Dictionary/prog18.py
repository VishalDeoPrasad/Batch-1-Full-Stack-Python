dict1 = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4
}
for key, val in dict1.items():
    # dict1[key] = dict1[key] + 100
    dict1[key] += 100

print(dict1)