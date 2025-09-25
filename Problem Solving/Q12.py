s = "Hello123!"

letters = 0
digits = 0
special = 0
for ch in s:
    if ch.isalpha():
        letters = letters + 1
    elif ch.isnumeric():
        digits = digits + 1
    else:
        special = special + 1

print("Letters:",letters )
print("Digits: ", digits)
print("special", special)