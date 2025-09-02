try:
    age = int(input("Enter Your Age: "))
    print(age)
except ValueError:
    print("Give your age in number only!")