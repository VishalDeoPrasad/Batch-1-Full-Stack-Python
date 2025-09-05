try:
    file = open("demo3.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File is not available sir!")