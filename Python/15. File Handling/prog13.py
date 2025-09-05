file = open('demo.txt', 'r')
print(file.read())

file.close()

print(file.read()) #error: becz file is closed