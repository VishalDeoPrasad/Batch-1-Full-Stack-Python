try:
    file = open("abc.txt", "r")
    print(file)
except FileNotFoundError:
    print("Check your file.")